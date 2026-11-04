from report_builder.config import wrap_page, get_b64

def get_chapters_7_to_9():
    pages = []

    # PAGE 52: CHAPTER 7 SYSTEM TESTING - 7.1 UNIT TESTING
    p52 = """
    <h1 class="chap-title">CHAPTER 7<br>SYSTEM TESTING</h1>
    <h2 class="sec-title">7.1 UNIT TESTING</h2>
    <p style="text-align: justify;">
        Unit testing involves testing individual components, computational algorithms, and isolated API endpoints to verify that each function operates correctly under valid, boundary, and erroneous conditions. In the context of the AI-Based Business Analytics Dashboard, the following unit testing scenarios were implemented and executed:
    </p>
    <ol>
        <li><strong>Dataset Management &amp; Ingestion:</strong>
            <ul>
                <li>Validate CSV file ingestion and dynamic schema detection across varying column naming formats.</li>
                <li>Verify file extension filtering, allowing only valid spreadsheet formats (.csv, .xlsx, .xls) and rejecting unauthorized uploads.</li>
                <li>Test missing-value detection and statistical imputation routines (Mean, Median, Mode, Drop).</li>
            </ul>
        </li>
        <li><strong>Executive Overview Analytics:</strong>
            <ul>
                <li>Verify computation of cumulative turnover, transaction count, net profit, and average order value.</li>
                <li>Validate Pearson correlation coefficients between Sales and Profit numerical vectors.</li>
            </ul>
        </li>
        <li><strong>Sales Analytics Module:</strong>
            <ul>
                <li>Test temporal aggregation logic across daily and monthly periods.</li>
                <li>Verify date-range filtering accuracy when specifying custom start and end dates.</li>
                <li>Validate peak sales and lowest sales period detection algorithms.</li>
            </ul>
        </li>
        <li><strong>Product &amp; Profit Analytics:</strong>
            <ul>
                <li>Verify product-level ranking by revenue and unit sales.</li>
                <li>Test profit margin ratio calculations and margin categorization tiers.</li>
            </ul>
        </li>
    </ol>
    """
    pages.append(wrap_page(p52, '<div class="page-num">52</div>'))

    # PAGE 53: 7.2 INTEGRATION TESTING
    p53 = """
    <h2 class="sec-title">7.2 INTEGRATION TESTING</h2>
    <p style="text-align: justify;">
        Integration testing focuses on evaluating the interconnected operations between independent modules, ensuring cohesive data flow from client-side AJAX requests to backend Pandas analytical routines and filesystem operations.
    </p>
    <ol>
        <li><strong>File Upload and Analytics Synchronisation:</strong>
            Verifies that uploading a new spreadsheet dynamically reconfigures the active analytical DataFrame, triggers immediate column re-detection, and refreshes the KPI cards across the frontend SPA without requiring manual server restarts.
        </li>
        <li><strong>Data Cleaning and Metric Propagation:</strong>
            Ensures that applying missing-value imputation or duplicate-record elimination updates the analytical pipeline immediately, so subsequent Sales and Profit requests query the sanitized dataset.
        </li>
        <li><strong>AI Insights and Natural Language Query Integration:</strong>
            Tests the end-to-end flow from user conversational query input to regex intent parsing, dynamic Pandas query extraction, and return of accurate responses formatted in Indian Rupees (₹).
        </li>
        <li><strong>Report Generation &amp; Export Integration:</strong>
            Verifies that the consolidated analytical report aggregates accurate metrics across all six upstream modules, and ensures downloadable CSV and Excel streams match the active in-memory dataset.
        </li>
    </ol>
    <p style="text-align: justify;">
        The system automated test suite (<code>test_app.py</code>) executed 11 rigorous automated test cases covering dataset upload, overview analytics, sales filtering, product ranking, profit analytics, AI insights generation, natural language Q&amp;A, and multi-format exports. All 11 test cases achieved a 100% pass rate.
    </p>
    """
    pages.append(wrap_page(p53, '<div class="page-num">53</div>'))

    # PAGE 54: CHAPTER 7 TEST RESULTS SUMMARY & TABLE
    p54 = """
    <h3 class="subsec-title">7.3 TEST CASES AND RESULTS VERIFICATION</h3>
    <p style="text-align: justify;">
        The table below details the formal test verification matrix executed on the AI-Based Business Analytics Dashboard:
    </p>
    <table class="academic-table">
        <thead>
            <tr>
                <th style="width: 10%;">TEST ID</th>
                <th style="width: 25%;">TEST SCENARIO</th>
                <th style="width: 35%;">EXPECTED OUTCOME</th>
                <th style="width: 18%;">ACTUAL RESULT</th>
                <th style="width: 12%;">STATUS</th>
            </tr>
        </thead>
        <tbody>
            <tr><td style="text-align: center;">TC-01</td><td>Root SPA Route Access</td><td>HTTP 200 OK, index.html rendered</td><td>HTTP 200, HTML loaded</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-02</td><td>Dataset Listing API</td><td>Returns active file &amp; inventory list</td><td>JSON status: success</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-03</td><td>Dataset Overview &amp; Stats</td><td>Row/Col counts, missing values dict</td><td>All schemas mapped</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-04</td><td>Data Cleaning (Mean/Dedup)</td><td>Nulls imputed, duplicate rows dropped</td><td>Cleaning audit logged</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-05</td><td>Overview Analytics KPIs</td><td>Total sales, profit, growth computed</td><td>Formatted in ₹ INR</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-06</td><td>Sales Analytics &amp; Date Filter</td><td>Monthly &amp; daily trends with bounds</td><td>Filtered JSON returned</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-07</td><td>Product Analytics Ranking</td><td>Top/Bottom products &amp; shares</td><td>Pareto groups correct</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-08</td><td>Profit Analytics Margins</td><td>Net profit margin &amp; dual series</td><td>Margin tier matched</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-09</td><td>AI Automated Insights</td><td>Z-score outliers &amp; findings generated</td><td>Findings cards built</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-10</td><td>Ask AI NLP Question</td><td>Natural query returns accurate ₹ data</td><td>Intent resolved</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
            <tr><td style="text-align: center;">TC-11</td><td>Analytical Report &amp; Export</td><td>Consolidated report &amp; CSV stream</td><td>HTTP 200 attachment</td><td style="text-align: center; color: green; font-weight: bold;">PASS</td></tr>
        </tbody>
    </table>
    <p style="text-align: justify; margin-top: 15px;">
        All 11 automated test cases were executed via Python test harness (<code>test_app.py</code>), verifying complete functional compliance and computational reliability.
    </p>
    """
    pages.append(wrap_page(p54, '<div class="page-num">54</div>'))

    # CHAPTER 8: SCREENSHOTS (Pages 55 to 64)
    screenshots_meta = [
        ("OVERVIEW DASHBOARD", "screen_overview.png", "Fig 8.1 EXECUTIVE OVERVIEW DASHBOARD", False),
        ("DATA MANAGEMENT & UPLOAD", "screen_datamanager.png", "Fig 8.2 DATA MANAGEMENT & FILE INGESTION", False),
        ("DATASET PREVIEW & CLEANING", "screen_preview.png", "Fig 8.3 DATASET INSPECTION & CLEANING PIPELINE", False),
        ("SALES PERFORMANCE ANALYTICS", "screen_sales.png", "Fig 8.4 TEMPORAL SALES & GROWTH ANALYTICS", False),
        ("PRODUCT & CATEGORY ANALYTICS", "screen_products.png", "Fig 8.5 PRODUCT PERFORMANCE & MARKET CONTRIBUTION", False),
        ("PROFIT MARGIN ANALYTICS", "screen_profit.png", "Fig 8.6 PROFITABILITY & MARGIN OPTIMIZATION", False),
        ("AI BUSINESS INSIGHTS", "screen_ai_insights.png", "Fig 8.7 RULE-BASED AI AUTOMATED INSIGHTS", False),
        ("NATURAL LANGUAGE ASK AI", "screen_ai_ask.png", "Fig 8.8 NATURAL LANGUAGE BUSINESS Q&A CHAT", False),
        ("REPORTS & EXPORT SUBSYSTEM", "screen_reports.png", "Fig 8.9 ANALYTICAL REPORTING & PDF/EXCEL EXPORT", False),
        ("MOBILE RESPONSIVE DASHBOARD", "screen_mobile.png", "Fig 8.10 MOBILE RESPONSIVE DASHBOARD VIEW", True)
    ]

    for idx, (title, fname, fig_cap, is_android) in enumerate(screenshots_meta):
        p_num = 55 + idx
        img_b64 = get_b64(fname)
        chap_hdr = '<h1 class="chap-title" style="margin-bottom: 10px;">CHAPTER 8<br>APPENDICES</h1><h2 class="sec-title" style="margin-top: 5px; margin-bottom: 10px;">8.1 SCREENSHOTS</h2>' if idx == 0 else ''
        img_cls = 'screenshot-img-android' if is_android else 'screenshot-img'
        
        p_content = f"""
        {chap_hdr}
        <div style="font-size: 11pt; font-weight: bold; text-align: center; margin-bottom: 6px; text-transform: uppercase;">{title}</div>
        <div class="screenshot-frame">
            <img class="{img_cls}" src="{img_b64}" alt="{title}">
        </div>
        <div class="figure-caption" style="margin-top: 6px; margin-bottom: 4px;">{fig_cap}</div>
        """
        pages.append(wrap_page(p_content, f'<div class="page-num">{p_num}</div>'))

    # PAGE 65: 8.2 DATA DICTIONARY (Part 1 - Tables 8.1, 8.2, 8.3)
    p65 = """
    <h2 class="sec-title">8.2 DATA DICTIONARY</h2>
    <p style="text-align: justify; margin-bottom: 10px;">
        The data dictionary provides formal technical specifications for all database entities, session variables, and transactional tables utilized across the AI-Based Business Analytics Dashboard.
    </p>

    <div class="table-caption">TABLE 8.1 USER &amp; SESSION TABLE</div>
    <table class="academic-table" style="margin-bottom: 15px;">
        <thead>
            <tr><th>Field Name</th><th>Data Type</th><th>Constraints</th><th>Description</th></tr>
        </thead>
        <tbody>
            <tr><td>user_id</td><td>VARCHAR(36)</td><td>Primary Key, Not Null</td><td>Unique UUID identifier for client session</td></tr>
            <tr><td>username</td><td>VARCHAR(50)</td><td>Not Null</td><td>Logged user or active enterprise profile</td></tr>
            <tr><td>active_dataset</td><td>VARCHAR(255)</td><td>Not Null</td><td>Current active CSV/XLSX file pointer</td></tr>
            <tr><td>theme_preference</td><td>VARCHAR(10)</td><td>Default 'dark'</td><td>Active UI theme mode ('light' / 'dark')</td></tr>
            <tr><td>created_at</td><td>TIMESTAMP</td><td>Not Null</td><td>Session instantiation timestamp</td></tr>
        </tbody>
    </table>

    <div class="table-caption">TABLE 8.2 DATASET INVENTORY TABLE</div>
    <table class="academic-table" style="margin-bottom: 15px;">
        <thead>
            <tr><th>Field Name</th><th>Data Type</th><th>Constraints</th><th>Description</th></tr>
        </thead>
        <tbody>
            <tr><td>dataset_id</td><td>INT AUTO_INCREMENT</td><td>Primary Key</td><td>Unique identifier for stored file</td></tr>
            <tr><td>filename</td><td>VARCHAR(255)</td><td>Not Null, Unique</td><td>Sanitized file storage name</td></tr>
            <tr><td>file_size_kb</td><td>DECIMAL(10,2)</td><td>Not Null</td><td>Storage size in Kilobytes</td></tr>
            <tr><td>total_rows</td><td>INT</td><td>Not Null</td><td>Total recorded observations</td></tr>
            <tr><td>total_cols</td><td>INT</td><td>Not Null</td><td>Total registered dimensional attributes</td></tr>
            <tr><td>upload_date</td><td>TIMESTAMP</td><td>Default Current</td><td>Upload completion timestamp</td></tr>
        </tbody>
    </table>

    <div class="table-caption">TABLE 8.3 SALES TRANSACTION TABLE</div>
    <table class="academic-table">
        <thead>
            <tr><th>Field Name</th><th>Data Type</th><th>Constraints</th><th>Description</th></tr>
        </thead>
        <tbody>
            <tr><td>transaction_id</td><td>BIGINT AUTO_INCREMENT</td><td>Primary Key</td><td>Sequential transaction identifier</td></tr>
            <tr><td>transaction_date</td><td>DATE</td><td>Not Null</td><td>Date of commercial transaction</td></tr>
            <tr><td>product_name</td><td>VARCHAR(150)</td><td>Not Null</td><td>Name or SKU of purchased item</td></tr>
            <tr><td>category</td><td>VARCHAR(100)</td><td>Default 'General'</td><td>Department or merchandise category</td></tr>
            <tr><td>sales_amount</td><td>DECIMAL(14,2)</td><td>Not Null</td><td>Gross transaction turnover in ₹ INR</td></tr>
            <tr><td>profit_amount</td><td>DECIMAL(14,2)</td><td>Not Null</td><td>Net profit margin earned in ₹ INR</td></tr>
        </tbody>
    </table>
    """
    pages.append(wrap_page(p65, '<div class="page-num">65</div>'))

    # PAGE 66: 8.2 DATA DICTIONARY (Part 2 - Tables 8.4, 8.5)
    p66 = """
    <div class="table-caption">TABLE 8.4 PRODUCT PROFITABILITY TABLE</div>
    <table class="academic-table" style="margin-bottom: 25px;">
        <thead>
            <tr><th>Field Name</th><th>Data Type</th><th>Constraints</th><th>Description</th></tr>
        </thead>
        <tbody>
            <tr><td>product_id</td><td>INT AUTO_INCREMENT</td><td>Primary Key</td><td>Unique SKU catalogue identifier</td></tr>
            <tr><td>product_name</td><td>VARCHAR(150)</td><td>Not Null, Unique</td><td>Standardized commercial merchandise title</td></tr>
            <tr><td>category</td><td>VARCHAR(100)</td><td>Not Null</td><td>Parent business merchandise hierarchy</td></tr>
            <tr><td>total_units_sold</td><td>INT</td><td>Default 0</td><td>Cumulative quantity distributed</td></tr>
            <tr><td>gross_revenue</td><td>DECIMAL(14,2)</td><td>Not Null</td><td>Cumulative revenue generated in ₹ INR</td></tr>
            <tr><td>cumulative_profit</td><td>DECIMAL(14,2)</td><td>Not Null</td><td>Cumulative net profit earned in ₹ INR</td></tr>
            <tr><td>margin_percentage</td><td>DECIMAL(5,2)</td><td>Calculated</td><td>Profit to Revenue yield percentage</td></tr>
            <tr><td>pareto_tier</td><td>VARCHAR(10)</td><td>'A' / 'B' / 'C'</td><td>80/20 ABC inventory performance tier</td></tr>
        </tbody>
    </table>

    <div class="table-caption">TABLE 8.5 AI INSIGHTS AUDIT TABLE</div>
    <table class="academic-table">
        <thead>
            <tr><th>Field Name</th><th>Data Type</th><th>Constraints</th><th>Description</th></tr>
        </thead>
        <tbody>
            <tr><td>insight_id</td><td>BIGINT AUTO_INCREMENT</td><td>Primary Key</td><td>Unique insight diagnostic record identifier</td></tr>
            <tr><td>dataset_name</td><td>VARCHAR(255)</td><td>Not Null</td><td>Source dataset evaluated</td></tr>
            <tr><td>insight_type</td><td>VARCHAR(50)</td><td>Not Null</td><td>Category ('Surge', 'Risk', 'Growth', 'Pareto')</td></tr>
            <tr><td>statistical_metric</td><td>VARCHAR(100)</td><td>Not Null</td><td>Z-score value, correlation coefficient, or delta</td></tr>
            <tr><td>finding_text</td><td>TEXT</td><td>Not Null</td><td>Natural language descriptive finding</td></tr>
            <tr><td>recommendation</td><td>TEXT</td><td>Not Null</td><td>Prescriptive strategic business advice</td></tr>
            <tr><td>generated_at</td><td>TIMESTAMP</td><td>Default Current</td><td>Diagnostic execution timestamp</td></tr>
        </tbody>
    </table>
    """
    pages.append(wrap_page(p66, '<div class="page-num">66</div>'))

    # PAGE 67: CHAPTER 9 CONCLUSION AND FUTURE ENHANCEMENT
    p67 = """
    <h1 class="chap-title">CHAPTER 9<br>CONCLUSION AND FUTURE ENHANCEMENT</h1>
    <h2 class="sec-title">9.1 CONCLUSION</h2>
    <p style="text-align: justify;">
        The AI-Based Business Analytics Dashboard (NexusBI) successfully delivers a modern, high-performance, and accessible business intelligence platform tailored for contemporary commercial enterprises. By integrating Python's robust data science ecosystem (Flask, Pandas, NumPy) with modern reactive frontend technologies (HTML5, Tailwind CSS, Chart.js), the platform democratizes advanced corporate analytics without imposing the prohibitive licensing costs of proprietary platforms like Microsoft Power BI or Tableau.
    </p>
    <p style="text-align: justify;">
        Through its comprehensive seven-module architecture, the system streamlines dataset ingestion and automated preprocessing, provides real-time multi-metric KPI tracking, performs deep temporal sales and product contribution breakdowns, analyzes gross profitability in Indian Rupees (₹), and introduces rule-based AI insight synthesis alongside conversational natural language question answering. The platform underwent extensive unit and integration testing, proving its computational accuracy, data integrity, and cross-device responsiveness.
    </p>

    <h2 class="sec-title">9.2 FUTURE ENHANCEMENT</h2>
    <ul>
        <li><strong>Machine Learning Predictive Forecasting:</strong> Integrating advanced time-series predictive models (such as ARIMA, Prophet, or LSTM recurrent neural networks) to provide automated 30-day and 90-day forward-looking sales forecasts with confidence intervals.</li>
        <li><strong>LLM Semantic Integration:</strong> Incorporating localized Large Language Models (LLMs) via Ollama or enterprise APIs to expand the Natural Language Query assistant with generative multi-hop reasoning across unstructured corporate documents.</li>
        <li><strong>Automated Anomaly Alerting via Webhooks:</strong> Implementing automated alert dispatches via email, WhatsApp Business API, and Slack webhooks when sales fall below statistical thresholds or critical margin erosion is detected.</li>
        <li><strong>Multi-Tenant Role-Based Access Control:</strong> Introducing enterprise user authentication, organization workspaces, and fine-grained role-based permissions (Administrator, Analyst, Viewer) with encrypted database credentials.</li>
    </ul>
    """
    pages.append(wrap_page(p67, '<div class="page-num">67</div>'))

    # PAGE 68: REFERENCES
    p68 = """
    <h1 class="chap-title">REFERENCES</h1>
    <div style="line-height: 2.0; font-size: 11pt; text-align: justify; margin-top: 30px;">
        <p>[1] W. McKinney, &ldquo;Data Structures for Statistical Computing in Python,&rdquo; in <em>Proceedings of the 9th Python in Science Conference</em>, Austin, TX, 2010, pp. 56&ndash;61, doi: 10.25080/Majora-92bf1924-009.</p>
        
        <p>[2] S. Bird, E. Klein, and E. Loper, <em>Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit</em>, 1st ed. Sebastopol, CA: O'Reilly Media, 2009.</p>
        
        <p>[3] M. Grinberg, <em>Flask Web Development: Developing Web Applications with Python</em>, 2nd ed. Sebastopol, CA: O'Reilly Media, 2018.</p>
        
        <p>[4] C. R. Harris et al., &ldquo;Array programming with NumPy,&rdquo; <em>Nature</em>, vol. 585, no. 7825, pp. 357&ndash;362, Sep. 2020, doi: 10.1038/s41586-020-2649-2.</p>
        
        <p>[5] T. Tandel, S. Wagal, N. Singh, R. Chaudhari, and V. Badgujar, &ldquo;Case Study on an Analytics Dashboard with Sales Prediction for Commercial Enterprises,&rdquo; in <em>2020 6th International Conference on Advanced Computing and Communication Systems (ICACCS)</em>, Coimbatore, India, 2020, pp. 931&ndash;934, doi: 10.1109/ICACCS48705.2020.9074234.</p>
        
        <p>[6] R. Few, <em>Information Dashboard Design: Displaying Data for At-a-Glance Monitoring</em>, 2nd ed. Burlingame, CA: Analytics Press, 2013.</p>
        
        <p>[7] V. Mayer-Sch&ouml;nberger and K. Cukier, <em>Big Data: A Revolution That Will Transform How We Live, Work, and Think</em>. Boston, MA: Houghton Mifflin Harcourt, 2013.</p>
        
        <p>[8] Academy of Maritime Education and Training (AMET University), <em>Capstone Project Documentation Guidelines and Specifications</em>, Kanathur, Chennai, India, 2026.</p>
    </div>
    """
    pages.append(wrap_page(p68, '<div class="page-num">68</div>'))

    return pages
