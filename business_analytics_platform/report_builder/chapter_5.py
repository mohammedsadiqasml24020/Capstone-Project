from report_builder.config import wrap_page

def get_chapter_5():
    pages = []

    # PAGE 22: CHAPTER 5 MODULE DESCRIPTION - 5.1 MAIN MODULES & 5.1.1
    p22 = """
    <h1 class="chap-title">CHAPTER 5<br>MODULE DESCRIPTION</h1>
    <h2 class="sec-title">5.1 MAIN MODULES</h2>
    <p style="text-align: justify;">
        The AI-Based Business Analytics Dashboard is architected as an interconnected suite of seven functional modules, each addressing a specialized operational domain:
    </p>
    <ul>
        <li>Executive Overview Dashboard</li>
        <li>Data Upload &amp; Management</li>
        <li>Sales Performance Analytics</li>
        <li>Product &amp; Category Analytics</li>
        <li>Profit Margin Analytics</li>
        <li>AI Business Insights &amp; Natural Language Q&amp;A</li>
        <li>Analytical Reports &amp; Multi-Format Export</li>
    </ul>

    <h2 class="sec-title">5.1.1 EXECUTIVE OVERVIEW DASHBOARD</h2>
    <p style="text-align: justify;">
        The Overview Dashboard module in the AI-Based Business Analytics Dashboard acts as the primary executive command center, aggregating high-level business metrics into an immediately digestible format. Upon application launch or navigation, this module dispatches an asynchronous GET request to the Flask server (<code>/api/analytics/overview</code>) to retrieve headline performance parameters.
    </p>
    <p style="text-align: justify;">
        The module computes and presents six primary Key Performance Indicator (KPI) cards: Total Revenue, Total Transaction Volume, Total Net Profit, Average Order Value, Maximum Single Sale, and Active Product Assortment. Each KPI card features a distinct accent gradient, an intuitive Lucide vector icon, and formatted currency labels adhering strictly to the Indian Rupee (₹ INR) convention.
    </p>
    <p style="text-align: justify;">
        Furthermore, the Overview Dashboard computes Period-over-Period Revenue Growth percentage by evaluating sales velocity across temporal midpoints, providing immediate awareness of whether top-line revenue is accelerating or contracting. A profit margin efficiency badge computes overall net margin against gross revenue.
    </p>
    """
    pages.append(wrap_page(p22, '<div class="page-num">22</div>'))

    # PAGE 23: 5.1.2 DATA UPLOAD & MANAGEMENT MODULE (Part 1)
    p23 = """
    <h2 class="sec-title">5.1.2 DATA UPLOAD &amp; MANAGEMENT MODULE</h2>
    <p style="text-align: justify;">
        The Data Upload &amp; Management module is responsible for the ingestion, validation, inspection, and sanitization of raw enterprise datasets. Recognizing that real-world business data frequently originates from diverse Point-of-Sale (POS) systems, legacy Enterprise Resource Planning (ERP) software, or manual spreadsheets, this module provides an intuitive drag-and-drop file upload zone supporting both Comma-Separated Values (.csv) and Microsoft Excel (.xlsx/.xls) workbooks up to 32 MB in size.
    </p>
    <p style="text-align: justify;">
        When a user uploads a new dataset, client-side validation first confirms file extension validity before transmitting the multi-part form payload to the Flask endpoint (<code>/api/dataset/upload</code>). The backend executes <code>secure_filename</code> sanitization, stores the file in the centralized repository, and instantly instantiates the analytical ingestion pipeline.
    </p>
    <p style="text-align: justify;">
        A critical innovation of this module is its <strong>Automated Schema Detection Engine</strong>. Rather than forcing rigid column header naming requirements upon the user, the engine scans the DataFrame utilizing semantic keyword heuristics and regular expressions. It dynamically maps columns representing:
    </p>
    <ul>
        <li><strong>Sales / Revenue:</strong> Scans for terms such as <em>sales</em>, <em>revenue</em>, <em>turnover</em>, <em>amount</em>, or selects the first primary numerical series.</li>
        <li><strong>Profit:</strong> Detects <em>profit</em>, <em>net_profit</em>, <em>margin</em>, or <em>earnings</em>.</li>
        <li><strong>Temporal Periods:</strong> Detects <em>date</em>, <em>month</em>, <em>timestamp</em>, <em>period</em>, or <em>time</em>.</li>
        <li><strong>Product SKU:</strong> Identifies <em>product</em>, <em>item</em>, <em>sku</em>, or <em>product_name</em>.</li>
        <li><strong>Category / Department:</strong> Maps <em>category</em>, <em>dept</em>, or <em>type</em>.</li>
    </ul>
    """
    pages.append(wrap_page(p23, '<div class="page-num">23</div>'))

    # PAGE 24: 5.1.2 DATA UPLOAD & MANAGEMENT (Part 2 - Data Cleaning Pipeline)
    p24 = """
    <h3 class="subsec-title">DATA INSPECTION &amp; AUTOMATED CLEANING PIPELINE</h3>
    <p style="text-align: justify;">
        Once ingested, the Data Management module displays a comprehensive structural overview of the dataset. This encompasses total row count, column count, memory footprint, column data types (int64, float64, object, datetime64), and an interactive 25-row data preview table.
    </p>
    <p style="text-align: justify;">
        The module executes immediate data quality profiling:
    </p>
    <ul>
        <li><strong>Missing Value Diagnostics:</strong> Evaluates every column for <code>NaN</code>, <code>null</code>, or blank cells, calculating both the raw missing record count and the exact missing percentage.</li>
        <li><strong>Duplicate Record Detection:</strong> Performs full-row hashing across all dimensional vectors to calculate the number of identical duplicate records present in the dataset.</li>
    </ul>
    <p style="text-align: justify;">
        To eliminate the manual labor of cleaning defective spreadsheets, the module features an <strong>Automated Data Cleaning Panel</strong>. Users can configure and trigger cleaning actions via a single click:
    </p>
    <ul>
        <li><strong>Missing Value Strategy:</strong> Users can choose between Mean Imputation (replaces numerical blanks with column average), Median Imputation (robust against outliers), Mode Imputation (for categorical fields), or Complete Row Dropping.</li>
        <li><strong>Duplicate Elimination:</strong> An automated toggle that drops duplicate records while preserving the initial primary instance.</li>
    </ul>
    <p style="text-align: justify;">
        Every cleaning invocation records an audit entry with timestamps, initial row count, cleaned row count, and total cells repaired. Furthermore, users can download the cleaned dataset immediately back to CSV or Excel, or reset the dataset to its original raw state at any time.
    </p>
    """
    pages.append(wrap_page(p24, '<div class="page-num">24</div>'))

    # PAGE 25: 5.1.3 SALES ANALYTICS MODULE
    p25 = """
    <h2 class="sec-title">5.1.3 SALES ANALYTICS MODULE</h2>
    <p style="text-align: justify;">
        The Sales Analytics module provides deep temporal exploration of business sales volumes, revenue velocity, and seasonal growth trends. By disaggregating high-level turnover figures into granular chronological intervals, managers can identify demand surges, holiday seasonality, and periods of revenue contraction.
    </p>
    <p style="text-align: justify;">
        The module features dynamic date-range filtering, enabling users to isolate specific fiscal quarters, months, or custom date spans (e.g., 2026-01-01 to 2026-06-30). Upon selecting a date filter, an asynchronous request (<code>/api/analytics/sales?from=...&amp;to=...</code>) recalculates all temporal metrics in real time.
    </p>
    <p style="text-align: justify;">
        Key analytical capabilities of this module include:
    </p>
    <ul>
        <li><strong>Monthly &amp; Daily Trend Visualizations:</strong> Renders smooth bezier-curved line charts illustrating turnover trajectories across months and individual transaction days.</li>
        <li><strong>Period-over-Period Growth Tracking:</strong> Calculates discrete percentage growth rates between consecutive intervals using the standard velocity formula:
            <div style="text-align: center; margin: 10px 0; font-weight: bold; font-family: 'Times New Roman', serif;">
                &Delta; Growth Rate (%) = [(Sales<sub>t</sub> &minus; Sales<sub>t&minus;1</sub>) / Sales<sub>t&minus;1</sub>] &times; 100
            </div>
        </li>
        <li><strong>Peak &amp; Trough Analysis:</strong> Automatically detects the calendar period with the highest turnover (Peak Sales) and the lowest turnover (Trough Sales), displaying exact figures and dates in highlighted stat cards.</li>
        <li><strong>Comparative Period Analysis:</strong> Allows side-by-side comparison of historical sales versus recent sales to validate whether marketing campaigns achieved targeted revenue benchmarks.</li>
    </ul>
    """
    pages.append(wrap_page(p25, '<div class="page-num">25</div>'))

    # PAGE 26: 5.1.4 PRODUCT ANALYTICS MODULE
    p26 = """
    <h2 class="sec-title">5.1.4 PRODUCT ANALYTICS MODULE</h2>
    <p style="text-align: justify;">
        The Product Analytics module provides comprehensive multi-product performance evaluation, merchandise mix optimization, and revenue contribution analysis. In enterprise retail and distribution, understanding which Stock Keeping Units (SKUs) drive revenue versus which products tie up operational working capital is crucial for maintaining healthy inventory turnover.
    </p>
    <p style="text-align: justify;">
        The module queries <code>/api/analytics/products</code>, triggering Pandas aggregation pipelines that group transactional records by product name and merchandise category:
    </p>
    <ul>
        <li><strong>Top-Performing &amp; Least-Selling Products:</strong> Automatically identifies the Top-5 best-selling products by revenue and units sold, as well as the Bottom-5 least-performing products, giving procurement teams immediate visibility into clearance priorities.</li>
        <li><strong>Product Revenue Comparison Chart:</strong> Renders horizontal and vertical bar charts comparing total sales generated across all active catalog products.</li>
        <li><strong>Market Contribution Distribution:</strong> Generates an interactive donut and pie chart illustrating each product's percentage contribution to overall company revenue:
            <div style="text-align: center; margin: 10px 0; font-weight: bold; font-family: 'Times New Roman', serif;">
                Contribution (%) = (Product Sales / Total Revenue) &times; 100
            </div>
        </li>
        <li><strong>Category-Level Performance:</strong> Aggregates product lines into broader business departments (e.g., Electronics, Apparel, Groceries), providing executive visibility into cross-departmental sales share.</li>
    </ul>
    <p style="text-align: justify;">
        Interactive tooltips allow managers to hover over any slice or bar to review exact revenue in Indian Rupees (₹) and exact unit sales volumes.
    </p>
    """
    pages.append(wrap_page(p26, '<div class="page-num">26</div>'))

    # PAGE 27: 5.1.5 PROFIT ANALYTICS MODULE
    p27 = """
    <h2 class="sec-title">5.1.5 PROFIT ANALYTICS MODULE</h2>
    <p style="text-align: justify;">
        While top-line sales figures reflect market demand, bottom-line net profit determines business viability. The Profit Analytics module provides rigorous fiscal scrutiny of gross margins, cost structures, and item-by-item profitability metrics.
    </p>
    <p style="text-align: justify;">
        The module interacts with the backend endpoint (<code>/api/analytics/profit</code>) to compute and visualize critical financial indicators:
    </p>
    <ul>
        <li><strong>Aggregate Profit &amp; Average Profit:</strong> Computes the cumulative net profit generated across all transactions, alongside average profit yield per individual transaction.</li>
        <li><strong>Profit Margin Gauge:</strong> Measures overall business margin health calculated as:
            <div style="text-align: center; margin: 10px 0; font-weight: bold; font-family: 'Times New Roman', serif;">
                Profit Margin (%) = (Total Net Profit / Total Revenue) &times; 100
            </div>
            The margin is visually mapped to color-coded performance tiers: Low Margin (&lt; 15%), Healthy Margin (15% &ndash; 30%), and High-Yield Margin (&gt; 30%).
        </li>
        <li><strong>Revenue vs. Profit Dual-Series Chart:</strong> Renders grouped bar charts displaying gross revenue alongside net profit for every month or product, clearly exposing margin compression or widening profitability spreads.</li>
        <li><strong>Product-Level Profitability Ranking:</strong> Generates a sorted ranking of all products based on individual profit contribution and margin percentage, enabling management to identify &ldquo;loss leaders&rdquo; versus high-margin flagship offerings.</li>
    </ul>
    """
    pages.append(wrap_page(p27, '<div class="page-num">27</div>'))

    # PAGE 28: 5.1.6 AI BUSINESS INSIGHTS & Q&A MODULE
    p28 = """
    <h2 class="sec-title">5.1.6 AI BUSINESS INSIGHTS &amp; NATURAL LANGUAGE ASSISTANT</h2>
    <p style="text-align: justify;">
        The AI Business Insights module is the intelligent core of the platform, transforming descriptive dashboard charts into automated prescriptive business intelligence. Traditional dashboards merely display numbers; this module interprets patterns, flags anomalies, and synthesizes strategic recommendations.
    </p>
    <h3 class="subsec-title">AUTOMATED STATISTICAL INSIGHT ENGINE</h3>
    <p style="text-align: justify;">
        The backend engine (<code>generate_ai_insights()</code>) executes automated analytical algorithms across the active dataset:
    </p>
    <ul>
        <li><strong>Statistical Outlier &amp; Anomaly Detection:</strong> Analyzes temporal variance using Z-score models (<em>Z</em> = (<em>x</em> &minus; &mu;) / &sigma;). Periods with sales exceeding 1.8 standard deviations are flagged as positive promotional surges, while drops below -1.8 standard deviations generate risk warnings.</li>
        <li><strong>Correlation Diagnostics:</strong> Computes Pearson correlation coefficients between sales volume and profitability to verify whether volume discounts are eroding margins.</li>
        <li><strong>Automated Business Findings:</strong> Generates formatted diagnostic cards highlighting Best Performing Month, Most Profitable SKU, Risk Alerts, and Actionable Recommendations (e.g., promotional strategies, restocking priorities).</li>
    </ul>

    <h3 class="subsec-title">NATURAL LANGUAGE QUERY ASSISTANT (ASK AI)</h3>
    <p style="text-align: justify;">
        To eliminate the need for non-technical users to write database queries or navigate complex menus, the module incorporates a conversational Natural Language Assistant. Users enter plain-English inquiries into a chat interface (e.g., <em>&ldquo;Which product generates the highest revenue?&rdquo;</em>, <em>&ldquo;What is the total profit?&rdquo;</em>, <em>&ldquo;Which month had the best sales?&rdquo;</em>).
    </p>
    <p style="text-align: justify;">
        The NLP parsing engine utilizes intent token matching and regex pattern extraction to parse the user's inquiry, query the Pandas analytical pipeline, and return a comprehensive answer formatted with exact Rupee figures and contextual operational explanations.
    </p>
    """
    pages.append(wrap_page(p28, '<div class="page-num">28</div>'))

    # PAGE 29: 5.1.7 REPORTS & MULTI-FORMAT EXPORT MODULE
    p29 = """
    <h2 class="sec-title">5.1.7 REPORTS &amp; MULTI-FORMAT EXPORT MODULE</h2>
    <p style="text-align: justify;">
        The Reports &amp; Export module facilitates corporate reporting, compliance auditing, and offline dissemination of business intelligence findings. While real-time dashboards serve operational needs, periodic board meetings, stakeholder reviews, and external audits require formal documented reports.
    </p>
    <p style="text-align: justify;">
        The module provides three distinct export channels:
    </p>
    <ol>
        <li><strong>Executive Analytical Report Generation:</strong> Compiles a consolidated multi-section analytical summary (<code>/api/reports/analytical</code>) incorporating Dataset Profile, Executive KPIs, Top Products by Sales, Top Products by Profit, Temporal Trajectories, and AI Recommendations into an interactive on-screen report layout.</li>
        <li><strong>High-Resolution PDF Export:</strong> Features a dedicated PDF Export generator utilizing Chrome headless printing architecture to produce formatted, paginated corporate reports with headers, footers, and academic thesis typography.</li>
        <li><strong>Spreadsheet Exports (Excel &amp; CSV):</strong>
            <ul>
                <li><strong>Processed CSV Export:</strong> Streams cleaned, deduplicated, and imputed dataset records directly via the <code>/api/dataset/export/csv</code> endpoint as an attachment.</li>
                <li><strong>Excel Analytical Workbook (.xlsx):</strong> Generates a multi-sheet Microsoft Excel workbook via OpenPyXL containing the raw cleaned dataset alongside pivot summaries of monthly performance and product rankings.</li>
            </ul>
        </li>
    </ol>
    <p style="text-align: justify;">
        All exported currency values maintain strict Indian Rupee (₹) formatting with comma grouping, ensuring immediate utility for Indian accounting standards.
    </p>
    """
    pages.append(wrap_page(p29, '<div class="page-num">29</div>'))

    return pages
