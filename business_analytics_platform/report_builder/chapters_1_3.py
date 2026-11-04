from report_builder.config import wrap_page

def get_chapters_1_to_3():
    pages = []

    # PAGE 9: CHAPTER 1 INTRODUCTION
    p9 = """
    <h1 class="chap-title">CHAPTER 1<br>INTRODUCTION</h1>
    <p style="text-align: justify;">
        Modern corporate enterprises, retail outlets, and commercial organizations often have complex daily transactions involving products, inventory, revenue, and profit margins. Managing the financial performance and operational metrics of the business is a critical aspect of ensuring sustained profitability, preventing cash-flow bottlenecks, and optimizing resource allocations. The traditional manual business tracking process can be time-consuming and error-prone, leading to revenue losses, delayed reporting, and strategic inefficiencies.
    </p>
    <p style="text-align: justify;">
        To overcome these challenges, a modern web-based AI-Powered Business Analytics Dashboard tracking system can be developed. The proposed system will allow business managers, executives, and department administrators to track revenue levels, receive automated business growth alerts, analyze product margins, and generate detailed analytical reports on sales performance. The system will be designed to be user-friendly, with a clean and intuitive SaaS dashboard interface that allows easy navigation and efficient analytics management.
    </p>
    <p style="text-align: justify;">
        The proposed system will be developed using Python Flask as the analytical backend and programmed using HTML5, Modern CSS (Tailwind CSS architecture), and interactive JavaScript with Chart.js. The computation and analytics management engine used will be Pandas and NumPy. The system will have features such as overview KPI tracking, automated data upload and missing-value cleaning, temporal sales tracking, product performance breakdowns, profit margin gauges, AI-powered insight generation, and natural language question answering. This project aims to develop an efficient and effective solution for business intelligence management, providing real-time data tracking, profit analysis, and growth forecasting, which can help to reduce financial waste and improve profitability.
    </p>
    """
    pages.append(wrap_page(p9, '<div class="page-num">9</div>'))

    # PAGE 10: CHAPTER 2 SYSTEM ANALYSIS
    p10 = """
    <h1 class="chap-title">CHAPTER 2<br>SYSTEM ANALYSIS</h1>
    <h2 class="sec-title">2.1 EXISTING SYSTEM</h2>
    <p style="text-align: justify;">
        The existing system for managing business transactions and revenue in many retail and corporate institutions involves manual tracking using physical ledgers or standalone disconnected spreadsheets (e.g., raw Microsoft Excel or CSV files without automated validation). The existing setup suffers from absent real-time synchronisation, fragmented data silos, no automated anomaly detection, and lack of AI-assisted decision intelligence.
    </p>
    <h3 class="subsec-title">DISADVANTAGES OF EXISTING SYSTEM</h3>
    <ul>
        <li>The existing system leads to substantial operational friction and inefficient decision-making due to the lack of real-time visibility into sales metrics and profit fluctuations.</li>
        <li>The system is labour-intensive, slow, and highly prone to human computation errors when manually tracking revenue numbers, profit margins, and inventory quantities.</li>
        <li>The system cannot provide dynamic visualizations, multidimensional slicing, or automated outlier explanations on business trends.</li>
        <li>Absence of natural language exploration compels non-technical business managers to rely completely on IT developers for basic ad-hoc reports.</li>
    </ul>

    <h2 class="sec-title">2.2 PROPOSED SYSTEM</h2>
    <p style="text-align: justify;">
        The proposed system is an AI-Based Business Analytics Dashboard developed for business administrators, executive leaders, and financial analysts. It includes comprehensive features such as automated data cleaning, real-time KPI overview monitoring, temporal sales trends, product contribution charts, profitability analytics, automated rule-based AI business insights, natural language AI assistance, and instant multi-format reporting (PDF, Excel, CSV) formatted strictly in Indian Rupees (₹ INR).
    </p>
    <h3 class="subsec-title">ADVANTAGES OF PROPOSED SYSTEM</h3>
    <ul>
        <li>Provides an efficient, automated, and visually interactive way to manage and analyze business performance metrics in a centralized SaaS dashboard.</li>
        <li>Significantly reduces manual computational overhead and improves inventory allocation by delivering instantaneous data summaries and automated missing-value imputation.</li>
        <li>Empowers non-technical executives to query business metrics using plain conversational English through an embedded rule-based Natural Language Processing engine.</li>
        <li>Offers cross-device accessibility with responsive light/dark themes, enabling seamless data analysis across desktop workstations, tablets, and smartphones.</li>
    </ul>
    """
    pages.append(wrap_page(p10, '<div class="page-num">10</div>'))

    # PAGE 11: CHAPTER 3 SYSTEM REQUIREMENTS
    p11 = """
    <h1 class="chap-title">CHAPTER 3<br>SYSTEM REQUIREMENTS</h1>
    <h2 class="sec-title">3.1 HARDWARE REQUIREMENTS</h2>
    <table class="academic-table">
        <tbody>
            <tr><td style="width: 35%; font-weight: bold;">● Processor</td><td style="width: 65%;">i5 Processor or Above (Intel Core / AMD Ryzen / Apple Silicon)</td></tr>
            <tr><td style="font-weight: bold;">● RAM</td><td>8 GB (16 GB Recommended for large datasets)</td></tr>
            <tr><td style="font-weight: bold;">● Hard Disk</td><td>512 GB SSD (Minimum 10 GB free space for workspace &amp; data)</td></tr>
            <tr><td style="font-weight: bold;">● GPU</td><td>Integrated graphics or 2 GB dedicated VRAM</td></tr>
            <tr><td style="font-weight: bold;">● Network</td><td>Standard broadband / local area network for intranet hosting</td></tr>
        </tbody>
    </table>

    <h2 class="sec-title">3.2 SOFTWARE REQUIREMENTS</h2>
    <table class="academic-table">
        <tbody>
            <tr><td style="width: 35%; font-weight: bold;">● Operating System</td><td style="width: 65%;">Windows 10 / Windows 11 / Linux (Ubuntu 22.04+) / macOS</td></tr>
            <tr><td style="font-weight: bold;">● Domain</td><td>AI, DATA ANALYTICS and MODERN WEB APPLICATION</td></tr>
            <tr><td style="font-weight: bold;">● Editor / IDE Used</td><td>Visual Studio Code / PyCharm / Cursor IDE</td></tr>
            <tr><td style="font-weight: bold;">● Frontend Technologies</td><td>HTML5, Modern CSS3 (Tailwind CSS), JavaScript (ES6+), Chart.js</td></tr>
            <tr><td style="font-weight: bold;">● Backend Framework</td><td>Python 3.10+ with Flask RESTful microframework</td></tr>
            <tr><td style="font-weight: bold;">● Analytics &amp; Math</td><td>Pandas 2.x, NumPy 1.26+, OpenPyXL</td></tr>
            <tr><td style="font-weight: bold;">● Browser Runtime</td><td>Google Chrome 115+, Mozilla Firefox, Microsoft Edge</td></tr>
        </tbody>
    </table>

    <h2 class="sec-title">3.3 SOFTWARE REQUIREMENTS SPECIFICATIONS</h2>
    <h3 class="subsec-title">PYTHON &amp; FLASK FRAMEWORK</h3>
    <p style="text-align: justify;">
        Python is a high-level, interpreted programming language celebrated for its readability, vast scientific computing ecosystem, and versatility. In this project, Python 3.13 serves as the primary engine powering the business intelligence platform.
    </p>
    <p style="text-align: justify;">
        Flask is a lightweight WSGI web application framework engineered to provide fast, scalable, and modular RESTful APIs. Some of the key features of the Flask framework utilized in this system include:
    </p>
    <ul>
        <li><strong>Micro-Architecture:</strong> Provides complete flexibility to integrate custom machine learning and statistical data pipelines without unnecessary boilerplate.</li>
        <li><strong>Built-in Development Server &amp; Debugger:</strong> Accelerates development and testing cycles with real-time stack traces.</li>
        <li><strong>RESTful Request Handling:</strong> Seamlessly dispatches JSON payloads between frontend AJAX fetch calls and backend Pandas analytical routines.</li>
    </ul>
    """
    pages.append(wrap_page(p11, '<div class="page-num">11</div>'))

    # PAGE 12: CHAPTER 3 SOFTWARE REQUIREMENTS (Contd. 1)
    p12 = """
    <h3 class="subsec-title">PANDAS DATA ANALYSIS LIBRARY</h3>
    <p style="text-align: justify;">
        Pandas is a fast, powerful, flexible, and open-source data analysis and manipulation tool built on top of the Python programming language. For the AI-Based Business Analytics Dashboard project, Pandas is the core computational backbone responsible for:
    </p>
    <ul>
        <li><strong>High-Performance DataFrames:</strong> Efficient memory management and fast ingestion of tabular records from both CSV and XLSX spreadsheet formats.</li>
        <li><strong>Automated Column Detection:</strong> Scanning file headers and data distributions with regex matching to detect Sales, Profit, Date, Product Name, Category, and Regional groupings automatically.</li>
        <li><strong>Data Sanitization:</strong> Flexible missing-data imputation strategies (Mean, Median, Mode, Row Drop) and automated duplicate-record detection and removal.</li>
        <li><strong>Grouping &amp; Aggregations:</strong> Instant calculation of monthly aggregations, temporal variances, product revenue shares, and profitability percentages across large transactional datasets.</li>
    </ul>

    <h3 class="subsec-title">NUMPY NUMERICAL COMPUTATION</h3>
    <p style="text-align: justify;">
        NumPy is the fundamental package for scientific computing in Python. It provides high-performance multidimensional array objects and mathematical tools used in this project to compute:
    </p>
    <ul>
        <li><strong>Z-Score Statistical Distributions:</strong> Standardizing sales variances to flag positive promotional surges or sudden operational risk dips beyond 1.8 standard deviations.</li>
        <li><strong>Correlation Matrices:</strong> Generating Pearson correlation coefficients between Sales volumes and Net Profit margins to validate unit-economic health.</li>
        <li><strong>High-Speed Array Vectorization:</strong> Eliminating Python loop bottlenecks during financial calculations.</li>
    </ul>

    <h3 class="subsec-title">VISUAL STUDIO CODE</h3>
    <p style="text-align: justify;">
        Visual Studio Code (VS Code) is an open-source code editor developed by Microsoft. Features utilized include:
    </p>
    <ul>
        <li><strong>Integrated Terminal:</strong> Allows running Flask daemons, test runners, and package managers in unified panels.</li>
        <li><strong>Extensibility:</strong> Python Pylance linters, JavaScript debugger, and Tailwind IntelliSense to ensure high-grade code quality.</li>
        <li><strong>Git Version Control:</strong> Native Git integration for branch tracking and release workflows.</li>
    </ul>
    """
    pages.append(wrap_page(p12, '<div class="page-num">12</div>'))

    # PAGE 13: CHAPTER 3 SOFTWARE REQUIREMENTS (Contd. 2)
    p13 = """
    <h3 class="subsec-title">CHART.JS DATA VISUALIZATION</h3>
    <p style="text-align: justify;">
        Chart.js is a premier open-source JavaScript library that renders HTML5 canvas-based interactive charts. Key architectural features include:
    </p>
    <ul>
        <li><strong>Responsive Canvas Rendering:</strong> Smoothly adapts charts across full HD desktop monitors, tablet viewports, and mobile screens.</li>
        <li><strong>Rich Visualization Palette:</strong> Native rendering of Multi-Line Trend Charts, Bar Charts, Donut/Pie distributions, and Gauge indicators.</li>
        <li><strong>Dynamic Interactivity:</strong> Custom HTML hover tooltips formatted in Indian Rupees (₹), smooth bezier curve animations, and dynamic dataset toggling.</li>
        <li><strong>Theme Harmonization:</strong> Full palette synchronization that flips grid lines and label contrasts smoothly between Light and Dark SaaS modes.</li>
    </ul>

    <h3 class="subsec-title">HTML5 (HYPERTEXT MARKUP LANGUAGE 5)</h3>
    <p style="text-align: justify;">
        HTML5 is the standard markup language for creating modern web applications. Key features utilized:
    </p>
    <ul>
        <li><strong>Semantic Elements:</strong> Utilization of &lt;header&gt;, &lt;aside&gt;, &lt;main&gt;, &lt;section&gt;, and &lt;article&gt; tags for accessible DOM structure.</li>
        <li><strong>Drag-and-Drop Ingestion APIs:</strong> Providing intuitive native file drops for immediate CSV/XLSX uploads.</li>
        <li><strong>Modern Form Validation:</strong> Native input pattern validation for date filters and numerical parameter bounds.</li>
    </ul>

    <h3 class="subsec-title">TAILWIND CSS &amp; MODERN CSS3</h3>
    <p style="text-align: justify;">
        CSS3 and the Tailwind CSS utility framework provide the presentation architecture of the dashboard:
    </p>
    <ul>
        <li><strong>Utility-First Design:</strong> Ensures clean spacing, uniform padding, typography hierarchy, and sleek rounded card contours inspired by Stripe and Vercel.</li>
        <li><strong>Dark Mode Architecture:</strong> Class-based theme toggling with deep navy backgrounds (#0b0f19) and high-contrast slate typography.</li>
        <li><strong>CSS Flexbox &amp; Grid:</strong> Resilient multidimensional layouts that prevent UI breakage during heavy data rendering.</li>
    </ul>
    """
    pages.append(wrap_page(p13, '<div class="page-num">13</div>'))

    # PAGE 14: CHAPTER 3 SOFTWARE REQUIREMENTS (Contd. 3)
    p14 = """
    <h3 class="subsec-title">JAVASCRIPT (ES6+) AND REST APIS</h3>
    <p style="text-align: justify;">
        JavaScript provides client-side reactivity and client-server asynchronous communication:
    </p>
    <ul>
        <li><strong>Asynchronous Fetch / AJAX:</strong> Decoupled API calls that fetch JSON payloads from Flask endpoints without full page reloads.</li>
        <li><strong>Hash-Based SPA Routing:</strong> Client-side router handling navigation between Overview, Data Management, Sales, Products, Profit, AI Insights, and Reports.</li>
        <li><strong>DOM Mutation &amp; Reactive UI:</strong> Dynamically updating KPI value cards, loading skeletons, and interactive data tables.</li>
        <li><strong>Currency Standardisation:</strong> Formatting monetary figures via <code>Intl.NumberFormat('en-IN', {style: 'currency', currency: 'INR'})</code>.</li>
    </ul>

    <h3 class="subsec-title">LUCIDE ICONS</h3>
    <p style="text-align: justify;">
        Lucide is an open-source vector icon family that delivers scalable SVG iconography. The dashboard incorporates sleek, recognizable icons across all navigation bars, stat cards, download actions, and status badges.
    </p>

    <h3 class="subsec-title">OPENPYXL &amp; SPREADSHEET ENGINES</h3>
    <p style="text-align: justify;">
        OpenPyXL is a Python library to read and write Excel 2010 xlsx/xlsm files. It enables the platform to:
    </p>
    <ul>
        <li>Parse multi-sheet enterprise Excel workbooks uploaded by users seamlessly.</li>
        <li>Generate formatted multi-sheet Excel analytical reports on demand with metadata summaries.</li>
    </ul>
    """
    pages.append(wrap_page(p14, '<div class="page-num">14</div>'))

    # PAGE 15: CHAPTER 3 FUNCTIONAL REQUIREMENTS
    p15 = """
    <h3 class="subsec-title">3.4 FUNCTIONAL REQUIREMENTS</h3>
    <p style="text-align: justify;">
        The functional requirements define the operational capabilities that the AI-Based Business Analytics Dashboard must provide to its end users:
    </p>
    <ol>
        <li><strong>Executive Overview Dashboard:</strong>
            <ul>
                <li>Display headline KPI cards: Total Revenue, Total Sales Count, Total Profit, Average Sale, Max/Min Sales, and Active Products.</li>
                <li>Display revenue growth percentage and calculated profit margin ratio.</li>
                <li>Render interactive dual-axis Revenue vs. Profit monthly trend preview chart.</li>
                <li>Display recent transactional activity feed.</li>
            </ul>
        </li>
        <li><strong>Dataset Management &amp; Ingestion:</strong>
            <ul>
                <li>Support upload of both CSV and XLSX spreadsheet formats up to 32 MB.</li>
                <li>Provide drag-and-drop file upload with visual feedback.</li>
                <li>Display comprehensive dataset preview with row/column counts and data types.</li>
                <li>Detect duplicate rows and missing values per column with percentage breakdown.</li>
                <li>Execute configurable cleaning routines (Mean, Median, Mode, Drop Rows, Drop Duplicates).</li>
                <li>Provide export of sanitized dataset back to CSV and Excel formats.</li>
            </ul>
        </li>
        <li><strong>Sales Analytics Module:</strong>
            <ul>
                <li>Render temporal sales charts with monthly and daily aggregations.</li>
                <li>Support date-range filtering (From Date &ndash; To Date).</li>
                <li>Highlight peak sales period, lowest sales period, and overall period growth rate.</li>
            </ul>
        </li>
    </ol>
    """
    pages.append(wrap_page(p15, '<div class="page-num">15</div>'))

    # PAGE 16: CHAPTER 3 FUNCTIONAL REQUIREMENTS (Contd.)
    p16 = """
    <ol start="4">
        <li><strong>Product Analytics Module:</strong>
            <ul>
                <li>Compute product-wise revenue, quantity sold, and profitability.</li>
                <li>Identify Top-5 best-selling products and least-selling products.</li>
                <li>Render interactive product revenue comparison bar charts.</li>
                <li>Display product market contribution breakdown in donut/pie format.</li>
            </ul>
        </li>
        <li><strong>Profit Analytics Module:</strong>
            <ul>
                <li>Calculate aggregate profit, average profit per transaction, and overall margin.</li>
                <li>Render dual-series Revenue vs. Profit comparison bar chart.</li>
                <li>Display product-level profitability ranking with margin percentages.</li>
                <li>Visualize margin health on visual gauge meters.</li>
            </ul>
        </li>
        <li><strong>AI Business Insights &amp; Natural Language Assistant:</strong>
            <ul>
                <li>Automatically generate structured business findings across Revenue, Profit, Category, and Risk domains.</li>
                <li>Execute statistical Z-score outlier detection to identify abnormal sales surges or drops.</li>
                <li>Provide conversational Natural Language Query interface (Ask AI) answering business questions in plain English.</li>
                <li>Generate automated strategic recommendations based on unit-economic indicators.</li>
            </ul>
        </li>
        <li><strong>Reports &amp; Multi-Format Export Subsystem:</strong>
            <ul>
                <li>Generate comprehensive consolidated analytical summary report.</li>
                <li>Export high-resolution PDF analytical briefing report.</li>
                <li>Download cleaned datasets in CSV and formatted Excel (.xlsx) formats.</li>
            </ul>
        </li>
    </ol>
    """
    pages.append(wrap_page(p16, '<div class="page-num">16</div>'))

    # PAGE 17: CHAPTER 3 NON-FUNCTIONAL REQUIREMENTS
    p17 = """
    <h3 class="subsec-title">3.5 NON-FUNCTIONAL REQUIREMENTS</h3>
    <p style="text-align: justify;">
        Non-functional requirements describe the quality attributes, performance constraints, and architectural standards of the system:
    </p>
    <ul>
        <li><strong>Performance &amp; Latency:</strong> The dashboard APIs must compute aggregations and respond within 200 milliseconds for standard enterprise datasets (up to 50,000 records). Initial SPA page load must complete in under 1.5 seconds over standard local networks.</li>
        <li><strong>Scalability:</strong> The analytical pipeline must support datasets up to 32 MB in memory without memory leaks. The modular architecture must allow easy addition of new statistical models.</li>
        <li><strong>Usability &amp; Accessibility:</strong> The user interface must adhere to SaaS design standards (Power BI, Stripe, Vercel). Charts must provide clear hover tooltips with Indian Rupee formatting. Smooth transitions and clear loading skeletons must accompany all asynchronous data fetches.</li>
        <li><strong>Reliability &amp; Robustness:</strong> The system must handle corrupted spreadsheets, missing columns, and incompatible data types gracefully with informative user toast notifications without crashing the backend service.</li>
        <li><strong>Cross-Platform Compatibility:</strong> Full responsiveness across desktop viewports (1920x1080, 1366x768), tablet resolutions (768x1024), and mobile viewports (375x667, 390x844). Native compatibility across all modern Chromium, WebKit, and Gecko browser engines.</li>
        <li><strong>Security &amp; Data Integrity:</strong> Uploaded files must be sanitized with <code>secure_filename</code> to prevent directory traversal exploits. All operations must run locally or in controlled enterprise boundaries to preserve business data confidentiality.</li>
    </ul>
    """
    pages.append(wrap_page(p17, '<div class="page-num">17</div>'))

    return pages
