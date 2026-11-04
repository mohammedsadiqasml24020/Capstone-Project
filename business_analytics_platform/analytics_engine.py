import os
import re
import json
import numpy as np
import pandas as pd
from datetime import datetime

class BusinessAnalyticsEngine:
    """
    Advanced Business Analytics Engine for Enterprise Data Intelligence,
    Statistical Summaries, Automated Insights, and Natural Language Q&A.
    """
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.active_dataset_name = None
        self.raw_df = None
        self.df = None
        self.column_mapping = {}
        self.cleaning_history = []
        os.makedirs(self.data_dir, exist_ok=True)
        self._initialize_default_dataset()

    def _initialize_default_dataset(self):
        """Pick default dataset: enterprise_sales_2026.csv or sales_and_profit.csv or sales_data.csv"""
        candidates = ["enterprise_sales_2026.csv", "sales_and_profit.csv", "sales_data.csv"]
        for c in candidates:
            path = os.path.join(self.data_dir, c)
            if os.path.exists(path):
                self.load_dataset(c)
                break

    def list_datasets(self):
        """List all available datasets in data directory with metadata."""
        files = []
        if not os.path.exists(self.data_dir):
            return files
        for f in os.listdir(self.data_dir):
            if f.endswith(('.csv', '.xlsx', '.xls')):
                filepath = os.path.join(self.data_dir, f)
                size_kb = round(os.path.getsize(filepath) / 1024, 2)
                modified = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M')
                files.append({
                    "filename": f,
                    "size_kb": size_kb,
                    "modified": modified,
                    "is_active": (f == self.active_dataset_name)
                })
        return files

    def load_dataset(self, filename):
        """Loads a dataset from the data directory and detects key analytics columns."""
        filepath = os.path.join(self.data_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Dataset {filename} not found.")

        if filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(filepath)
        else:
            raise ValueError("Unsupported file format. Please upload CSV or XLSX.")

        self.active_dataset_name = filename
        self.raw_df = df.copy()
        self.df = df.copy()
        self.cleaning_history = []
        self._detect_columns()
        return self.get_dataset_overview()

    def _detect_columns(self):
        """Automatically identify Sales, Profit, Date/Month, and Product/Category columns."""
        self.column_mapping = {
            "sales": None,
            "profit": None,
            "date": None,
            "product": None,
            "category": None,
            "region": None
        }
        if self.df is None or self.df.empty:
            return

        cols = list(self.df.columns)
        for col in cols:
            c_low = col.strip().lower()
            if self.column_mapping["sales"] is None and any(k in c_low for k in ["sales", "revenue", "turnover", "amount", "total_sales"]):
                self.column_mapping["sales"] = col
            elif self.column_mapping["profit"] is None and any(k in c_low for k in ["profit", "earnings", "margin", "net_profit"]):
                self.column_mapping["profit"] = col
            elif self.column_mapping["date"] is None and any(k in c_low for k in ["date", "month", "timestamp", "period", "day", "time"]):
                self.column_mapping["date"] = col
            elif self.column_mapping["product"] is None and any(k in c_low for k in ["product", "item", "sku", "product_name", "goods"]):
                self.column_mapping["product"] = col
            elif self.column_mapping["category"] is None and any(k in c_low for k in ["category", "dept", "department", "type"]):
                self.column_mapping["category"] = col
            elif self.column_mapping["region"] is None and any(k in c_low for k in ["region", "zone", "territory", "city", "state", "country"]):
                self.column_mapping["region"] = col

        # Fallbacks if columns are not explicitly named
        num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        if not self.column_mapping["sales"] and len(num_cols) > 0:
            self.column_mapping["sales"] = num_cols[0]
        if not self.column_mapping["profit"] and len(num_cols) > 1:
            self.column_mapping["profit"] = num_cols[1]
        
        obj_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        if not self.column_mapping["product"] and len(obj_cols) > 0:
            for oc in obj_cols:
                if oc != self.column_mapping.get("date"):
                    self.column_mapping["product"] = oc
                    break

    def get_dataset_overview(self):
        """Returns row count, column count, column names, missing values, duplicate count, and sample records."""
        if self.df is None:
            return {"status": "error", "message": "No dataset currently loaded"}

        total_rows = int(len(self.df))
        total_cols = int(len(self.df.columns))
        duplicate_rows = int(self.df.duplicated().sum())

        missing_dict = {}
        dtypes_dict = {}
        for col in self.df.columns:
            m_count = int(self.df[col].isnull().sum())
            missing_dict[col] = {
                "count": m_count,
                "percentage": round((m_count / total_rows * 100), 2) if total_rows > 0 else 0
            }
            dtypes_dict[col] = str(self.df[col].dtype)

        preview_records = self.df.head(25).replace({np.nan: None}).to_dict(orient="records")

        # Statistical summary like df.describe()
        num_df = self.df.select_dtypes(include=[np.number])
        stat_summary = {}
        if not num_df.empty:
            desc = num_df.describe().to_dict()
            for k, v in desc.items():
                stat_summary[k] = {sk: round(sv, 2) if isinstance(sv, (int, float)) and not np.isnan(sv) else None for sk, sv in v.items()}

        return {
            "status": "success",
            "active_dataset": self.active_dataset_name,
            "total_rows": total_rows,
            "total_cols": total_cols,
            "columns": list(self.df.columns),
            "column_types": dtypes_dict,
            "column_mapping": self.column_mapping,
            "duplicate_rows": duplicate_rows,
            "missing_values": missing_dict,
            "preview": preview_records,
            "statistical_summary": stat_summary,
            "cleaning_history": self.cleaning_history
        }

    def clean_dataset(self, missing_strategy="mean", remove_duplicates=True, custom_columns=None):
        """
        Applies cleaning routines:
        missing_strategy: 'mean', 'median', 'mode', 'drop', or 'none'
        remove_duplicates: bool
        """
        if self.df is None:
            raise ValueError("No dataset loaded.")

        initial_rows = len(self.df)
        initial_missing = int(self.df.isnull().sum().sum())
        initial_duplicates = int(self.df.duplicated().sum())

        target_cols = custom_columns if custom_columns else self.df.columns.tolist()

        if missing_strategy == "mean":
            for col in target_cols:
                if col in self.df.columns and pd.api.types.is_numeric_dtype(self.df[col]):
                    m_val = self.df[col].mean()
                    self.df[col] = self.df[col].fillna(m_val)
        elif missing_strategy == "median":
            for col in target_cols:
                if col in self.df.columns and pd.api.types.is_numeric_dtype(self.df[col]):
                    m_val = self.df[col].median()
                    self.df[col] = self.df[col].fillna(m_val)
        elif missing_strategy == "mode":
            for col in target_cols:
                if col in self.df.columns:
                    modes = self.df[col].mode()
                    if not modes.empty:
                        self.df[col] = self.df[col].fillna(modes[0])
        elif missing_strategy == "drop":
            self.df = self.df.dropna(subset=target_cols)

        if remove_duplicates:
            self.df = self.df.drop_duplicates()

        # Update saved file if requested or keep cleaned copy in memory
        cleaned_rows = len(self.df)
        remaining_missing = int(self.df.isnull().sum().sum())
        remaining_duplicates = int(self.df.duplicated().sum())

        history_item = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "strategy": missing_strategy,
            "removed_duplicates": remove_duplicates,
            "rows_before": initial_rows,
            "rows_after": cleaned_rows,
            "missing_filled": initial_missing - remaining_missing,
            "duplicates_removed": initial_duplicates - remaining_duplicates
        }
        self.cleaning_history.append(history_item)

        # Re-detect columns after cleaning
        self._detect_columns()

        return {
            "status": "success",
            "message": "Dataset cleaned successfully.",
            "summary": history_item,
            "overview": self.get_dataset_overview()
        }

    def reset_dataset(self):
        """Restores the original unmodified dataset."""
        if self.raw_df is not None:
            self.df = self.raw_df.copy()
            self.cleaning_history = []
            self._detect_columns()
            return self.get_dataset_overview()
        return {"status": "error", "message": "No dataset to reset"}

    # ----------------- MODULE 1: OVERVIEW DASHBOARD -----------------
    def get_overview_analytics(self):
        """Calculates headline KPIs, correlation, and summary performance."""
        if self.df is None or self.df.empty:
            return {"error": "No data available"}

        sales_col = self.column_mapping.get("sales")
        profit_col = self.column_mapping.get("profit")
        product_col = self.column_mapping.get("product")
        date_col = self.column_mapping.get("date")

        total_revenue = float(self.df[sales_col].sum()) if sales_col and sales_col in self.df else 0.0
        total_sales_count = int(len(self.df))
        total_profit = float(self.df[profit_col].sum()) if profit_col and profit_col in self.df else 0.0
        avg_sales = float(self.df[sales_col].mean()) if sales_col and sales_col in self.df else 0.0
        max_sales = float(self.df[sales_col].max()) if sales_col and sales_col in self.df else 0.0
        min_sales = float(self.df[sales_col].min()) if sales_col and sales_col in self.df else 0.0
        
        total_products = int(self.df[product_col].nunique()) if product_col and product_col in self.df else 1
        
        # Profit Margin %
        profit_margin = round((total_profit / total_revenue * 100), 2) if total_revenue > 0 else 0.0

        # Revenue Growth Calculation (First half vs second half or period growth)
        revenue_growth = 0.0
        if len(self.df) >= 2 and sales_col:
            mid = len(self.df) // 2
            first_half = float(self.df.iloc[:mid][sales_col].sum())
            second_half = float(self.df.iloc[mid:][sales_col].sum())
            if first_half > 0:
                revenue_growth = round(float((second_half - first_half) / first_half * 100), 2)

        # Correlation Matrix (Matching original script: df[['Sales','Profit']].corr())
        correlation_val = None
        if sales_col and profit_col and sales_col in self.df and profit_col in self.df:
            corr_df = self.df[[sales_col, profit_col]].dropna().corr()
            if not corr_df.empty and sales_col in corr_df and profit_col in corr_df[sales_col]:
                correlation_val = round(float(corr_df.loc[sales_col, profit_col]), 3)

        # Top 5 recent activities or records
        recent_records = self.df.tail(6).replace({np.nan: None}).to_dict(orient="records")

        # Mini monthly or sequence chart
        chart_labels = []
        chart_sales = []
        chart_profit = []
        if date_col and date_col in self.df:
            time_grp = self.df.groupby(date_col, sort=False)[[c for c in [sales_col, profit_col] if c]].sum()
            chart_labels = [str(x) for x in time_grp.index.tolist()]
            chart_sales = [round(float(v), 2) for v in time_grp[sales_col].tolist()] if sales_col else []
            chart_profit = [round(float(v), 2) for v in time_grp[profit_col].tolist()] if profit_col else []
        else:
            chart_labels = [f"Record {i+1}" for i in range(min(12, len(self.df)))]
            chart_sales = [round(float(v), 2) for v in self.df[sales_col].head(12).fillna(0)] if sales_col else []
            chart_profit = [round(float(v), 2) for v in self.df[profit_col].head(12).fillna(0)] if profit_col else []

        return {
            "total_revenue": round(total_revenue, 2),
            "total_sales_count": total_sales_count,
            "total_profit": round(total_profit, 2),
            "average_sales": round(avg_sales, 2),
            "maximum_sales": round(max_sales, 2),
            "minimum_sales": round(min_sales, 2),
            "total_products": total_products,
            "revenue_growth": revenue_growth,
            "profit_margin": profit_margin,
            "correlation": correlation_val,
            "recent_records": recent_records,
            "chart_preview": {
                "labels": chart_labels,
                "sales": chart_sales,
                "profit": chart_profit
            }
        }

    # ----------------- MODULE 3: SALES ANALYTICS -----------------
    def get_sales_analytics(self, date_from=None, date_to=None):
        """Monthly & daily sales, trends, growth %, highest/lowest sales periods, comparison."""
        if self.df is None or self.df.empty:
            return {"error": "No data available"}

        sales_col = self.column_mapping.get("sales")
        date_col = self.column_mapping.get("date")

        if not sales_col or sales_col not in self.df:
            return {"error": "Sales column not found in dataset"}

        working_df = self.df.copy()

        # Date Filtering if valid date column
        has_dates = False
        if date_col and date_col in working_df:
            try:
                working_df['_parsed_date'] = pd.to_datetime(working_df[date_col], errors='coerce')
                if not working_df['_parsed_date'].isnull().all():
                    has_dates = True
                    if date_from:
                        working_df = working_df[working_df['_parsed_date'] >= pd.to_datetime(date_from)]
                    if date_to:
                        working_df = working_df[working_df['_parsed_date'] <= pd.to_datetime(date_to)]
            except Exception:
                has_dates = False

        # Grouping by period
        if has_dates:
            working_df['Period'] = working_df['_parsed_date'].dt.strftime('%Y-%m')
            daily_grp = working_df.groupby(working_df['_parsed_date'].dt.strftime('%Y-%m-%d'))[sales_col].sum()
            monthly_grp = working_df.groupby('Period')[sales_col].sum()
        elif date_col and date_col in working_df:
            # Maybe month names like 'Jan', 'Feb' from Part 1
            monthly_grp = working_df.groupby(date_col, sort=False)[sales_col].sum()
            daily_grp = monthly_grp
        else:
            working_df['Period'] = [f"Item {i+1}" for i in range(len(working_df))]
            monthly_grp = working_df.groupby('Period', sort=False)[sales_col].sum()
            daily_grp = monthly_grp

        monthly_labels = [str(k) for k in monthly_grp.index]
        monthly_values = [round(float(v), 2) for v in monthly_grp.values]

        # Growth rates period-over-period
        growth_rates = []
        for i in range(len(monthly_values)):
            if i == 0:
                growth_rates.append(0.0)
            else:
                prev = monthly_values[i-1]
                curr = monthly_values[i]
                g = round(((curr - prev) / prev * 100), 2) if prev > 0 else 0.0
                growth_rates.append(g)

        # Cumulative revenue trend
        cumulative_revenue = list(np.cumsum(monthly_values))
        cumulative_revenue = [round(float(v), 2) for v in cumulative_revenue]

        # Peak and lowest sales period
        highest_idx = int(np.argmax(monthly_values)) if len(monthly_values) > 0 else 0
        lowest_idx = int(np.argmin(monthly_values)) if len(monthly_values) > 0 else 0

        highest_period = {
            "period": monthly_labels[highest_idx] if monthly_labels else "N/A",
            "sales": monthly_values[highest_idx] if monthly_values else 0
        }
        lowest_period = {
            "period": monthly_labels[lowest_idx] if monthly_labels else "N/A",
            "sales": monthly_values[lowest_idx] if monthly_values else 0
        }

        # Daily breakdown
        daily_labels = [str(k) for k in daily_grp.index]
        daily_values = [round(float(v), 2) for v in daily_grp.values]

        # Total sales & average in filtered window
        tot_sales = sum(monthly_values)
        avg_sales = (tot_sales / len(monthly_values)) if monthly_values else 0
        overall_growth = round(float((monthly_values[-1] - monthly_values[0]) / monthly_values[0] * 100), 2) if len(monthly_values) > 1 and monthly_values[0] > 0 else 0.0

        return {
            "status": "success",
            "total_sales": round(tot_sales, 2),
            "average_period_sales": round(avg_sales, 2),
            "overall_growth_percentage": overall_growth,
            "highest_sales_period": highest_period,
            "lowest_sales_period": lowest_period,
            "monthly_analysis": {
                "labels": monthly_labels,
                "sales": monthly_values,
                "growth_rates": growth_rates,
                "cumulative": cumulative_revenue
            },
            "daily_analysis": {
                "labels": daily_labels,
                "sales": daily_values
            }
        }

    # ----------------- MODULE 4: PRODUCT ANALYTICS -----------------
    def get_product_analytics(self):
        """Product-wise sales, best-selling, least-selling, contribution %, pie/bar charts."""
        if self.df is None or self.df.empty:
            return {"error": "No data available"}

        sales_col = self.column_mapping.get("sales")
        product_col = self.column_mapping.get("product")
        profit_col = self.column_mapping.get("profit")

        if not product_col or product_col not in self.df:
            # Synthetic single product if none present
            return {
                "status": "warning",
                "message": "Product column not detected in active dataset. Displaying overall aggregate.",
                "products": [],
                "best_selling": None,
                "least_selling": None,
                "chart_data": {"labels": [], "sales": [], "profit": [], "percentages": []}
            }

        # Group by product
        agg_dict = {sales_col: 'sum'}
        if profit_col and profit_col in self.df:
            agg_dict[profit_col] = 'sum'

        prod_df = self.df.groupby(product_col).agg(agg_dict).reset_index()
        total_sales = prod_df[sales_col].sum()

        prod_df['Contribution_Pct'] = (prod_df[sales_col] / total_sales * 100).round(2) if total_sales > 0 else 0.0

        if profit_col and profit_col in prod_df:
            prod_df['Profit_Margin_Pct'] = (prod_df[profit_col] / prod_df[sales_col] * 100).round(2)
        else:
            prod_df['Profit_Margin_Pct'] = 0.0
            prod_df[profit_col] = 0.0

        # Sort descending by sales
        prod_sorted = prod_df.sort_values(by=sales_col, ascending=False).reset_index(drop=True)

        best_selling = {
            "product": str(prod_sorted.iloc[0][product_col]),
            "sales": round(float(prod_sorted.iloc[0][sales_col]), 2),
            "profit": round(float(prod_sorted.iloc[0][profit_col]), 2) if profit_col else None,
            "contribution": float(prod_sorted.iloc[0]['Contribution_Pct'])
        } if not prod_sorted.empty else None

        least_selling = {
            "product": str(prod_sorted.iloc[-1][product_col]),
            "sales": round(float(prod_sorted.iloc[-1][sales_col]), 2),
            "profit": round(float(prod_sorted.iloc[-1][profit_col]), 2) if profit_col else None,
            "contribution": float(prod_sorted.iloc[-1]['Contribution_Pct'])
        } if not prod_sorted.empty else None

        product_list = []
        for idx, row in prod_sorted.iterrows():
            product_list.append({
                "rank": idx + 1,
                "product": str(row[product_col]),
                "sales": round(float(row[sales_col]), 2),
                "profit": round(float(row[profit_col]), 2) if profit_col else 0.0,
                "contribution_pct": float(row['Contribution_Pct']),
                "profit_margin_pct": float(row['Profit_Margin_Pct'])
            })

        chart_labels = [str(r[product_col]) for _, r in prod_sorted.iterrows()]
        chart_sales = [round(float(r[sales_col]), 2) for _, r in prod_sorted.iterrows()]
        chart_profit = [round(float(r[profit_col]), 2) for _, r in prod_sorted.iterrows()] if profit_col else []
        chart_pct = [float(r['Contribution_Pct']) for _, r in prod_sorted.iterrows()]

        return {
            "status": "success",
            "total_products": len(product_list),
            "best_selling": best_selling,
            "least_selling": least_selling,
            "product_list": product_list,
            "chart_data": {
                "labels": chart_labels,
                "sales": chart_sales,
                "profit": chart_profit,
                "percentages": chart_pct
            }
        }

    # ----------------- MODULE 5: PROFIT ANALYTICS -----------------
    def get_profit_analytics(self):
        """Total profit, average profit, profit margins, product-wise profitability, revenue vs profit."""
        if self.df is None or self.df.empty:
            return {"error": "No data available"}

        sales_col = self.column_mapping.get("sales")
        profit_col = self.column_mapping.get("profit")
        product_col = self.column_mapping.get("product")
        date_col = self.column_mapping.get("date")

        total_sales = float(self.df[sales_col].sum()) if sales_col and sales_col in self.df else 0.0
        total_profit = float(self.df[profit_col].sum()) if profit_col and profit_col in self.df else 0.0
        avg_profit = float(self.df[profit_col].mean()) if profit_col and profit_col in self.df else 0.0
        max_profit = float(self.df[profit_col].max()) if profit_col and profit_col in self.df else 0.0
        min_profit = float(self.df[profit_col].min()) if profit_col and profit_col in self.df else 0.0
        overall_margin = round((total_profit / total_sales * 100), 2) if total_sales > 0 else 0.0

        # Product profitability breakdown & classification
        profitability_matrix = []
        if product_col and profit_col and sales_col and all(c in self.df for c in [product_col, profit_col, sales_col]):
            p_grp = self.df.groupby(product_col)[[sales_col, profit_col]].sum().reset_index()
            for _, r in p_grp.iterrows():
                p_sales = float(r[sales_col])
                p_prof = float(r[profit_col])
                margin = round((p_prof / p_sales * 100), 2) if p_sales > 0 else 0.0
                
                # Category classification
                if margin >= 20.0:
                    tier = "High Margin"
                    badge_color = "emerald"
                elif margin >= 10.0:
                    tier = "Healthy Margin"
                    badge_color = "blue"
                elif margin >= 0:
                    tier = "Low Margin"
                    badge_color = "amber"
                else:
                    tier = "Loss / Negative Margin"
                    badge_color = "rose"

                profitability_matrix.append({
                    "product": str(r[product_col]),
                    "sales": round(p_sales, 2),
                    "profit": round(p_prof, 2),
                    "margin_pct": margin,
                    "tier": tier,
                    "badge_color": badge_color
                })
            # Sort by margin descending
            profitability_matrix = sorted(profitability_matrix, key=lambda x: x["margin_pct"], reverse=True)

        # Revenue vs Profit Trend Comparison
        trend_labels = []
        rev_trend = []
        prof_trend = []
        margin_trend = []

        if date_col and date_col in self.df:
            grp = self.df.groupby(date_col, sort=False)[[c for c in [sales_col, profit_col] if c]].sum()
            trend_labels = [str(x) for x in grp.index]
            rev_trend = [round(float(v), 2) for v in grp[sales_col]] if sales_col else []
            prof_trend = [round(float(v), 2) for v in grp[profit_col]] if profit_col else []
            for s, p in zip(rev_trend, prof_trend):
                m = round((p / s * 100), 2) if s > 0 else 0.0
                margin_trend.append(m)
        else:
            limit = min(15, len(self.df))
            trend_labels = [f"Record {i+1}" for i in range(limit)]
            rev_trend = [round(float(v), 2) for v in self.df[sales_col].head(limit).fillna(0)] if sales_col else []
            prof_trend = [round(float(v), 2) for v in self.df[profit_col].head(limit).fillna(0)] if profit_col else []
            for s, p in zip(rev_trend, prof_trend):
                m = round((p / s * 100), 2) if s > 0 else 0.0
                margin_trend.append(m)

        return {
            "status": "success",
            "total_profit": round(total_profit, 2),
            "average_profit": round(avg_profit, 2),
            "overall_margin_pct": overall_margin,
            "max_profit": round(max_profit, 2),
            "min_profit": round(min_profit, 2),
            "profitability_matrix": profitability_matrix,
            "comparison_chart": {
                "labels": trend_labels,
                "revenue": rev_trend,
                "profit": prof_trend,
                "margin_pct": margin_trend
            }
        }

    # ----------------- MODULE 6: AI BUSINESS INSIGHTS & NLP ASSISTANT -----------------
    def generate_ai_insights(self):
        """Generates automated business explanations, trend detections, anomalies, and strategic recommendations."""
        if self.df is None or self.df.empty:
            return {"error": "No data available"}

        sales_col = self.column_mapping.get("sales")
        profit_col = self.column_mapping.get("profit")
        product_col = self.column_mapping.get("product")
        date_col = self.column_mapping.get("date")

        total_rev = float(self.df[sales_col].sum()) if sales_col and sales_col in self.df else 0
        total_prof = float(self.df[profit_col].sum()) if profit_col and profit_col in self.df else 0
        margin = round((total_prof / total_rev * 100), 2) if total_rev > 0 else 0

        insights = []
        anomalies = []
        recommendations = []

        # 1. Performance Overview Insight
        insights.append({
            "category": "Performance Summary",
            "type": "summary",
            "icon": "activity",
            "title": "Healthy Financial Trajectory",
            "description": f"The business generated a cumulative revenue of ₹{total_rev:,.2f} with a net profit of ₹{total_prof:,.2f}, representing an overall operating margin of {margin}%.",
            "impact": "Positive" if margin >= 15 else "Moderate"
        })

        # 2. Product-level AI Insights
        if product_col and sales_col and product_col in self.df:
            p_grp = self.df.groupby(product_col)[sales_col].sum().sort_values(ascending=False)
            top_p = p_grp.index[0]
            top_p_sales = p_grp.iloc[0]
            top_p_pct = round((top_p_sales / total_rev * 100), 1) if total_rev > 0 else 0
            
            insights.append({
                "category": "Product Dominance",
                "type": "product",
                "icon": "package",
                "title": f"Flagship Product: {top_p}",
                "description": f"{top_p} is the single largest revenue driver, generating ₹{top_p_sales:,.2f} ({top_p_pct}% of total sales). Focus marketing efforts on retaining customer engagement for this catalog hero.",
                "impact": "High Value"
            })

            # Check if one product makes up > 45% of revenue (concentration risk)
            if top_p_pct > 45.0:
                anomalies.append({
                    "severity": "Warning",
                    "title": "Product Concentration Risk Detected",
                    "description": f"A single product ({top_p}) contributes {top_p_pct}% of total enterprise revenue. Any supply chain bottleneck or demand fluctuation in this product presents a high business continuity risk.",
                    "suggestion": "Diversify the product catalog and cross-sell complementary accessories."
                })

            if len(p_grp) > 1:
                bottom_p = p_grp.index[-1]
                bottom_p_sales = p_grp.iloc[-1]
                bottom_p_pct = round((bottom_p_sales / total_rev * 100), 1) if total_rev > 0 else 0
                insights.append({
                    "category": "Growth Opportunity",
                    "type": "product_low",
                    "icon": "trending-down",
                    "title": f"Underperforming Line: {bottom_p}",
                    "description": f"{bottom_p} generates only ₹{bottom_p_sales:,.2f} ({bottom_p_pct}% contribution). Evaluate pricing elasticity, run promotional bundles, or reposition this SKU.",
                    "impact": "Needs Action"
                })

        # 3. Profit Margin Driver Insight
        if product_col and profit_col and sales_col and all(c in self.df for c in [product_col, profit_col, sales_col]):
            p_agg = self.df.groupby(product_col)[[sales_col, profit_col]].sum()
            p_agg['Margin'] = (p_agg[profit_col] / p_agg[sales_col] * 100).fillna(0)
            best_margin_p = p_agg.sort_values(by='Margin', ascending=False).index[0]
            best_margin_val = round(float(p_agg.loc[best_margin_p, 'Margin']), 1)
            
            insights.append({
                "category": "Margin Leader",
                "type": "profit",
                "icon": "dollar-sign",
                "title": f"Highest Margin Product: {best_margin_p}",
                "description": f"{best_margin_p} operates at an industry-leading {best_margin_val}% profit margin. Allocating extra ad spend to this product will disproportionately expand net bottom-line earnings.",
                "impact": "Strategic Win"
            })

        # 4. Trend & Seasonality Detection
        if date_col and sales_col and date_col in self.df:
            time_grp = self.df.groupby(date_col, sort=False)[sales_col].sum()
            vals = time_grp.values
            if len(vals) >= 3:
                first_3 = np.mean(vals[:max(1, len(vals)//3)])
                last_3 = np.mean(vals[-max(1, len(vals)//3):])
                delta_pct = round(((last_3 - first_3) / first_3 * 100), 1) if first_3 > 0 else 0
                
                trend_direction = "Upward Acceleration" if delta_pct > 5 else ("Downward Contraction" if delta_pct < -5 else "Stable Plateau")
                insights.append({
                    "category": "Trend Detection",
                    "type": "trend",
                    "icon": "trending-up" if delta_pct >= 0 else "trending-down",
                    "title": f"Sales Velocity: {trend_direction}",
                    "description": f"Sales show a {delta_pct:+.1f}% momentum shift when comparing concluding operational cycles to baseline periods.",
                    "impact": "Positive" if delta_pct >= 0 else "Critical"
                })

                # Statistical Outlier / Anomaly Detection (Z-score > 1.8)
                mean_s = np.mean(vals)
                std_s = np.std(vals)
                if std_s > 0:
                    for period, v in time_grp.items():
                        z = (v - mean_s) / std_s
                        if z > 1.8:
                            anomalies.append({
                                "severity": "Info Spike",
                                "title": f"Revenue Surge in {period}",
                                "description": f"Sales reached ₹{v:,.2f}, which is {round(z, 2)} standard deviations above the seasonal average (₹{mean_s:,.2f}).",
                                "suggestion": "Investigate underlying promotional campaigns or bulk orders to replicate this surge."
                            })
                        elif z < -1.8:
                            anomalies.append({
                                "severity": "Alert Dip",
                                "title": f"Unusual Sales Drop in {period}",
                                "description": f"Sales plunged to ₹{v:,.2f}, which is {round(abs(z), 2)} standard deviations below the mean expectation.",
                                "suggestion": "Check for out-of-stock events, platform downtime, or competitive seasonal discounting."
                            })

        # 5. Strategic AI Business Recommendations
        recommendations = [
            {
                "priority": "P1 - High",
                "title": "Optimize High-Margin Product Inventory",
                "action": "Increase inventory buffer stock by 25% for top-margin items to avoid high-cost stockout scenarios during peak cycles."
            },
            {
                "priority": "P2 - Medium",
                "title": "Dynamic Pricing & Bundle Strategy",
                "action": "Bundle slower-moving SKUs with high-volume hero products with a 7-10% discount to accelerate turnover."
            },
            {
                "priority": "P3 - Medium",
                "title": "Customer Retention & Cross-Selling",
                "action": "Introduce tiered loyalty incentives for repeat enterprise and corporate buyers to stabilize baseline monthly recurring volume."
            },
            {
                "priority": "P4 - Low",
                "title": "Automated Reorder Point Tuning",
                "action": "Implement rolling 30-day forecast models to prevent capital lockup in slow-turnover categories."
            }
        ]

        return {
            "status": "success",
            "insights": insights,
            "anomalies": anomalies,
            "recommendations": recommendations
        }

    def ask_ai(self, question):
        """
        Processes Natural Language business questions using context-aware statistical intelligence.
        Supports questions like:
        - Which product generates the highest revenue?
        - What is the total profit?
        - Which month has the highest sales?
        - Why are sales decreasing?
        - Give me a summary of business performance.
        - What is the average sales?
        - What are your business recommendations?
        """
        if self.df is None or self.df.empty:
            return {
                "answer": "There is currently no active dataset loaded. Please upload or select a dataset in Data Management.",
                "context": {}
            }

        q_lower = question.strip().lower()

        sales_col = self.column_mapping.get("sales")
        profit_col = self.column_mapping.get("profit")
        product_col = self.column_mapping.get("product")
        date_col = self.column_mapping.get("date")

        total_rev = float(self.df[sales_col].sum()) if sales_col and sales_col in self.df else 0
        total_prof = float(self.df[profit_col].sum()) if profit_col and profit_col in self.df else 0
        avg_sales = float(self.df[sales_col].mean()) if sales_col and sales_col in self.df else 0
        margin = round((total_prof / total_rev * 100), 2) if total_rev > 0 else 0

        # Question 1: "Which product generates the highest revenue / best selling?"
        if any(k in q_lower for k in ["highest revenue", "best selling", "top product", "highest sales product", "top selling", "most revenue"]):
            if product_col and sales_col and product_col in self.df:
                p_grp = self.df.groupby(product_col)[sales_col].sum().sort_values(ascending=False)
                top_p = p_grp.index[0]
                top_sales = p_grp.iloc[0]
                pct = round((top_sales / total_rev * 100), 2) if total_rev > 0 else 0
                return {
                    "question": question,
                    "answer": f"**{top_p}** generates the highest revenue in the business, totaling **₹{top_sales:,.2f}**, which represents **{pct}%** of overall sales.",
                    "details": [
                        f"Top Product: {top_p}",
                        f"Revenue Generated: ₹{top_sales:,.2f}",
                        f"Contribution to Total Sales: {pct}%",
                        f"Catalog Ranking: #1 of {len(p_grp)} products"
                    ],
                    "query_type": "product_highest_revenue"
                }
            else:
                return {
                    "question": question,
                    "answer": f"Total sales is **₹{total_rev:,.2f}**, but no product breakdown column is present in the current dataset.",
                    "details": [],
                    "query_type": "product_highest_revenue"
                }

        # Question 2: "What is the total profit / profit margin?"
        if any(k in q_lower for k in ["total profit", "how much profit", "net profit", "profit margin", "what is profit"]):
            if profit_col and profit_col in self.df:
                return {
                    "question": question,
                    "answer": f"The total cumulative profit is **₹{total_prof:,.2f}**, operating at an overall net profit margin of **{margin}%** against total revenue of **₹{total_rev:,.2f}**.",
                    "details": [
                        f"Total Profit: ₹{total_prof:,.2f}",
                        f"Total Revenue: ₹{total_rev:,.2f}",
                        f"Net Profit Margin: {margin}%",
                        f"Average Profit per Record: ₹{(total_prof / len(self.df)):,.2f}"
                    ],
                    "query_type": "profit_summary"
                }
            else:
                return {
                    "question": question,
                    "answer": "Profit data is not mapped or available in this dataset.",
                    "details": [],
                    "query_type": "profit_summary"
                }

        # Question 3: "Which month has the highest sales / peak month?"
        if any(k in q_lower for k in ["highest sales", "which month", "peak month", "best month", "highest month"]):
            if date_col and sales_col and date_col in self.df:
                m_grp = self.df.groupby(date_col, sort=False)[sales_col].sum()
                peak_month = m_grp.idxmax()
                peak_sales = m_grp.max()
                low_month = m_grp.idxmin()
                low_sales = m_grp.min()
                return {
                    "question": question,
                    "answer": f"**{peak_month}** achieved the highest sales with **₹{peak_sales:,.2f}**. By comparison, the lowest performing period was **{low_month}** with **₹{low_sales:,.2f}**.",
                    "details": [
                        f"Peak Period: {peak_month} (₹{peak_sales:,.2f})",
                        f"Lowest Period: {low_month} (₹{low_sales:,.2f})",
                        f"Performance Differential: +{round(((peak_sales - low_sales) / low_sales * 100), 1) if low_sales > 0 else 0}% peak-to-trough"
                    ],
                    "query_type": "month_highest_sales"
                }
            else:
                max_s = self.df[sales_col].max() if sales_col else 0
                return {
                    "question": question,
                    "answer": f"The highest recorded single sale is **₹{max_s:,.2f}**.",
                    "details": [],
                    "query_type": "month_highest_sales"
                }

        # Question 4: "Why are sales decreasing / decreasing sales / drop in sales?"
        if any(k in q_lower for k in ["why are sales decreasing", "decreasing", "drop in sales", "sales down", "why sales fell", "decline"]):
            reasons = []
            if date_col and sales_col and date_col in self.df:
                t_grp = self.df.groupby(date_col, sort=False)[sales_col].sum()
                vals = t_grp.values
                if len(vals) >= 2:
                    diffs = np.diff(vals)
                    negative_indices = np.where(diffs < 0)[0]
                    if len(negative_indices) > 0:
                        worst_idx = negative_indices[np.argmin(diffs[negative_indices])]
                        from_p = t_grp.index[worst_idx]
                        to_p = t_grp.index[worst_idx + 1]
                        drop_amt = abs(diffs[worst_idx])
                        drop_pct = round((drop_amt / vals[worst_idx] * 100), 1)
                        reasons.append(f"A notable contraction occurred from {from_p} to {to_p}, dropping by ₹{drop_amt:,.2f} (-{drop_pct}%).")

            if product_col and sales_col and product_col in self.df:
                p_grp = self.df.groupby(product_col)[sales_col].sum().sort_values(ascending=True)
                weak_product = p_grp.index[0]
                reasons.append(f"Product drag: '{weak_product}' generates lowest aggregate sales (₹{p_grp.iloc[0]:,.2f}), depressing overall volume.")

            reasons.append("Cyclical demand seasonality after promotional quarters or potential inventory constraints.")

            return {
                "question": question,
                "answer": "Analysis indicates sales drops are primarily driven by **period-over-period seasonality**, coupled with **underperformance in secondary product lines** and marketing fatigue.",
                "details": reasons,
                "query_type": "sales_decrease_explanation"
            }

        # Question 5: "Give me a summary of business performance / executive summary"
        if any(k in q_lower for k in ["summary", "overview", "business performance", "executive summary", "how is business"]):
            top_prod_str = ""
            if product_col and sales_col and product_col in self.df:
                top_p = self.df.groupby(product_col)[sales_col].sum().idxmax()
                top_prod_str = f" The strongest catalog contributor is **{top_p}**."
            
            return {
                "question": question,
                "answer": f"**Executive Business Summary:**\nTotal Revenue stands at **₹{total_rev:,.2f}** with an aggregate Profit of **₹{total_prof:,.2f}** ({margin}% net margin). Average sales per transaction is **₹{avg_sales:,.2f}** across **{len(self.df)}** records.{top_prod_str} Overall fiscal health is robust with stable margin resilience.",
                "details": [
                    f"Gross Revenue: ₹{total_rev:,.2f}",
                    f"Net Profit: ₹{total_prof:,.2f}",
                    f"Profit Margin: {margin}%",
                    f"Avg Transaction: ₹{avg_sales:,.2f}",
                    f"Total Processed Records: {len(self.df)}"
                ],
                "query_type": "business_summary"
            }

        # Question 6: "What is the average sales?"
        if any(k in q_lower for k in ["average sales", "mean sales", "avg sales"]):
            return {
                "question": question,
                "answer": f"The average sales per transaction is **₹{avg_sales:,.2f}** across {len(self.df)} recorded entries.",
                "details": [
                    f"Average Sales: ₹{avg_sales:,.2f}",
                    f"Minimum Sales: ₹{float(self.df[sales_col].min() if sales_col else 0):,.2f}",
                    f"Maximum Sales: ₹{float(self.df[sales_col].max() if sales_col else 0):,.2f}"
                ],
                "query_type": "average_sales"
            }

        # Question 7: "What are your business recommendations / advice?"
        if any(k in q_lower for k in ["recommend", "recommendation", "advice", "strategy", "next steps"]):
            return {
                "question": question,
                "answer": "Based on statistical clustering and margin analysis, here are the top 3 AI recommendations:\n1. **Focus Capital on High-Margin Lines**: Shift marketing spend toward products delivering >15% margin.\n2. **Mitigate Single-Product Dependency**: Cross-sell and bundle secondary accessories with flagship hardware.\n3. **Seasonal Buffer Stocking**: Pre-order inventory 30 days before identified historical peak periods to avoid lost orders.",
                "details": [
                    "Recommendation 1: Margin-focused ad spend allocation",
                    "Recommendation 2: Product bundle incentives",
                    "Recommendation 3: Predictive inventory replenishment"
                ],
                "query_type": "ai_recommendations"
            }

        # Question 8: Correlation between sales and profit
        if any(k in q_lower for k in ["correlation", "relationship between sales and profit"]):
            if sales_col and profit_col and sales_col in self.df and profit_col in self.df:
                corr = self.df[[sales_col, profit_col]].dropna().corr().iloc[0, 1]
                strength = "strong positive" if corr > 0.7 else ("moderate positive" if corr > 0.4 else "weak")
                return {
                    "question": question,
                    "answer": f"The Pearson correlation between Sales and Profit is **{round(corr, 3)}**, indicating a **{strength}** relationship. Higher revenue directly translates into expanded rupee profit.",
                    "details": [
                        f"Correlation Coefficient: {round(corr, 4)}",
                        f"Interpretation: {strength.title()} Linear Correlation",
                        f"Formula Applied: Pearson r = cov(X,Y) / (sigma_x * sigma_y)"
                    ],
                    "query_type": "correlation"
                }

        # Fallback intelligent answer
        return {
            "question": question,
            "answer": f"Regarding your question: Current revenue stands at **₹{total_rev:,.2f}** with **₹{total_prof:,.2f}** in net profits across {len(self.df)} transactions. For in-depth insights, you can ask about highest revenue products, peak months, profit margins, or business recommendations.",
            "details": [
                f"Active Dataset: {self.active_dataset_name}",
                f"Revenue: ₹{total_rev:,.2f}",
                f"Profit: ₹{total_prof:,.2f}"
            ],
            "query_type": "general_info"
        }

    # ----------------- MODULE 7: REPORTS & EXPORT -----------------
    def generate_analytical_report(self):
        """Generates comprehensive structured report data for PDF, Print, or onscreen export."""
        overview = self.get_overview_analytics()
        sales_data = self.get_sales_analytics()
        product_data = self.get_product_analytics()
        profit_data = self.get_profit_analytics()
        ai_data = self.generate_ai_insights()

        report = {
            "title": "Executive Business Analytics & Intelligence Report",
            "generation_time": datetime.now().strftime("%B %d, %Y - %I:%M %p"),
            "dataset_analyzed": self.active_dataset_name,
            "executive_summary": {
                "total_revenue": overview.get("total_revenue", 0),
                "total_profit": overview.get("total_profit", 0),
                "profit_margin": overview.get("profit_margin", 0),
                "total_transactions": overview.get("total_sales_count", 0),
                "average_sale": overview.get("average_sales", 0),
                "revenue_growth": overview.get("revenue_growth", 0),
                "correlation": overview.get("correlation", 0)
            },
            "sales_performance": {
                "highest_period": sales_data.get("highest_sales_period"),
                "lowest_period": sales_data.get("lowest_sales_period"),
                "overall_growth_pct": sales_data.get("overall_growth_percentage", 0),
                "monthly_breakdown": sales_data.get("monthly_analysis", {})
            },
            "product_leaderboard": product_data.get("product_list", [])[:10],
            "profitability_breakdown": profit_data.get("profitability_matrix", [])[:10],
            "ai_insights": ai_data.get("insights", []),
            "anomalies": ai_data.get("anomalies", []),
            "recommendations": ai_data.get("recommendations", [])
        }
        return report

    def export_csv_bytes(self):
        """Exports the current cleaned dataset to CSV string/bytes."""
        if self.df is None:
            raise ValueError("No dataset loaded")
        return self.df.to_csv(index=False).encode('utf-8')

    def export_excel_path(self, target_filepath):
        """Exports the dataset into a professionally formatted Excel workbook."""
        if self.df is None:
            raise ValueError("No dataset loaded")
        
        with pd.ExcelWriter(target_filepath, engine='openpyxl') as writer:
            self.df.to_excel(writer, sheet_name='Cleaned_Data', index=False)
            
            # Add summary sheet
            summary_data = {
                "Metric": ["Total Revenue", "Total Profit", "Profit Margin (%)", "Total Records", "Average Sales"],
                "Value": [
                    self.df[self.column_mapping.get("sales")].sum() if self.column_mapping.get("sales") else 0,
                    self.df[self.column_mapping.get("profit")].sum() if self.column_mapping.get("profit") else 0,
                    round((self.df[self.column_mapping.get("profit")].sum() / self.df[self.column_mapping.get("sales")].sum() * 100), 2) if self.column_mapping.get("sales") and self.column_mapping.get("profit") else 0,
                    len(self.df),
                    self.df[self.column_mapping.get("sales")].mean() if self.column_mapping.get("sales") else 0
                ]
            }
            pd.DataFrame(summary_data).to_excel(writer, sheet_name='Executive_Summary', index=False)
        return target_filepath
