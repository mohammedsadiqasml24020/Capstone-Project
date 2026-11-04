# NexusBI: AI-Based Business Analytics Dashboard
## Complete Modern Web Application & Capstone Project

NexusBI is a modern, responsive, SaaS-style Business Analytics and Intelligence web application built with **Python (Flask, Pandas, NumPy, OpenPyXL)** and modern frontend technologies (**Tailwind CSS, Chart.js, Lucide Icons, Glassmorphism UI**). 

This platform transforms standard static Python/Matplotlib scripts into an enterprise-grade analytics suite suitable for college capstone projects, startup business analytics, and executive decision-making.

---

## 🌟 Key Architecture & Highlights

- **Full-Stack Separation**: Decoupled Python REST API (`analytics_engine.py` & `app.py`) with a reactive Single-Page Application (SPA) frontend.
- **Dynamic Dataset Switching**: Pre-loaded with:
  1. `enterprise_sales_2026.csv`: 12-month enterprise multi-product dataset for deep capstone demonstration.
  2. `sales_and_profit.csv`: The original multi-record dataset with null values and duplicates for demonstrating live data cleaning.
  3. `sales_data.csv`: Monthly baseline sales dataset.
  4. Any user-uploaded CSV or Excel (.xlsx) file via drag-and-drop.
- **SaaS UI/UX Design**: Inspired by Microsoft Power BI, Tableau, Stripe, and Vercel. Features light/dark theme toggle, glassmorphic cards, sparklines, responsive layouts, and print-ready PDF styling.
- **Natural Language "Ask AI" Engine**: Answers queries in plain English with exact statistics and actionable takeaways.

---

## 🚀 7 Required Application Modules

### 1. Module 1: Overview Dashboard
- **Headline KPIs**: Total Revenue (₹), Total Sales Count, Total Profit (₹), Average Sale (₹), Total Products, Revenue Growth (%).
- **Statistical Correlation**: Pearson correlation coefficient ($r$) between Sales and Profit.
- **Interactive Trajectory**: Interactive Chart.js Area & Line chart tracking revenue and profit in Indian Rupees (₹) over time.
- **Recent Activities Stream**: Live transaction table with status tags.

### 2. Module 2: Data Upload & Management
- **File Ingestion**: Upload CSV and Excel (`.xlsx`, `.xls`) with drag-and-drop.
- **Dataset Health Audit**: Total rows, columns, memory usage, duplicate records, and per-column missing values.
- **Automated Data Cleaning**:
  - Missing value imputation: Mean (`df.fillna(df.mean())`), Median, Mode, or Drop rows.
  - Deduplication: One-click `df.drop_duplicates()` removal with before/after count comparison.
- **Dataset Export**: Download processed dataset as clean CSV or Excel workbook.
- **Reset to Raw**: Revert modifications at any time.

### 3. Module 3: Sales Analytics
- **Monthly Sales Breakdown**: Dynamic bar chart showing monthly volume and growth momentum.
- **Cumulative Revenue Trend**: Area chart showing total financial accumulation over time.
- **Daily Cadence Performance**: Granular timeline sales tracking.
- **Peak & Lowest Sales Periods**: Instant detection of maximum and minimum sales periods.
- **Date-Based Filtering**: Filter records by custom start and end date ranges.

### 4. Module 4: Product Analytics
- **Spotlight Cards**: Highlighting Best-Selling and Least-Selling products with % contribution.
- **Product Revenue Comparison**: Horizontal bar chart comparing product revenue.
- **Product Contribution Percentage**: Interactive Donut chart displaying market share.
- **Performance Leaderboard**: Ranked table with revenue, profit, margins, and contribution progress bars.

### 5. Module 5: Profit Analytics
- **Headline Metrics**: Total Net Profit, Average Profit, Overall Net Margin %, Peak Single Profit.
- **Revenue vs. Profit Combo Chart**: Dual-axis bar and line chart comparing top-line revenue to bottom-line profit.
- **Profitability Tier Matrix**: Products automatically classified into High Margin (>20%), Healthy Margin (10-20%), Low Margin (<10%), and Loss tiers.

### 6. Module 6: AI Business Insights & Natural Language Assistant
- **Automated Intelligence Feed**: Automatically explains sales performance, flagship product contribution, and trend trajectory.
- **Statistical Anomaly Detection**: Highlights spikes and dips exceeding 1.8 standard deviations from the seasonal mean.
- **Strategic Recommendations**: Prioritized business actions (inventory replenishment, dynamic pricing bundles, retention strategies).
- **Interactive "Ask AI" Chat Assistant**: Answers queries in plain English:
  - *"Which product generates the highest revenue?"*
  - *"What is the total profit?"*
  - *"Which month has the highest sales?"*
  - *"Why are sales decreasing?"*
  - *"Give me a summary of business performance."*
  - *"What is the average sales?"*
  - *"Show me correlation between sales and profit"*

### 7. Module 7: Reports & Export
- **Executive Analytical Report**: Formatted document containing executive KPIs, top product leaderboards, and AI recommendations.
- **Export to PDF**: One-click printable view formatted for PDF save.
- **Export to Excel**: Multi-sheet formatted Excel workbook (`.xlsx`) using OpenPyXL.
- **Download Processed CSV**: Cleaned and imputed CSV export.

---

## 🛠️ Quick Start Instructions

### Prerequisites
- Python 3.10+ (or Anaconda Python)
- Web browser (Chrome, Edge, Firefox, Safari)

### 1. Running on Windows
Simply double-click `run.bat` or run:
```cmd
cd business_analytics_platform
python app.py
```
*(If using Anaconda: `"%USERPROFILE%\anaconda3\python.exe" app.py`)*

### 2. Running on macOS / Linux
```bash
cd business_analytics_platform
chmod +x run.sh
./run.sh
```

### 3. Open in Browser
Visit: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📂 Project Directory Structure

```
business_analytics_platform/
├── app.py                      # Flask backend & RESTful API routes
├── analytics_engine.py         # Pandas/NumPy analytics, statistical modeling, AI NLP engine
├── requirements.txt            # Python dependencies
├── run.bat                     # Windows 1-click launcher
├── run.sh                      # Unix/macOS launcher
├── README.md                   # Project documentation
├── data/                       # Datasets storage
│   ├── enterprise_sales_2026.csv   # 12-month enterprise dataset
│   ├── sales_and_profit.csv        # Dataset with missing values and duplicates
│   └── sales_data.csv              # Monthly sales baseline dataset
├── static/
│   ├── css/
│   │   └── styles.css          # Modern SaaS CSS, dark mode variables, glassmorphism
│   └── js/
│       ├── app.js              # SPA router, theme manager, dataset selector
│       ├── charts.js           # Reusable Chart.js wrappers & theme sync
│       └── modules/
│           ├── overview.js         # Module 1
│           ├── data_manager.js     # Module 2
│           ├── sales_analytics.js  # Module 3
│           ├── product_analytics.js# Module 4
│           ├── profit_analytics.js # Module 5
│           ├── ai_insights.js      # Module 6
│           └── reports_export.js   # Module 7
└── templates/
    └── index.html              # Responsive single-page dashboard container
```
