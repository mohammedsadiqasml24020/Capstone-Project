from report_builder.config import wrap_page

def get_chapter_4():
    pages = []

    # PAGE 18: CHAPTER 4 SYSTEM DESIGN - 4.1 ARCHITECTURE DIAGRAM
    p18 = """
    <h1 class="chap-title">CHAPTER 4<br>SYSTEM DESIGN</h1>
    <h2 class="sec-title">4.1 ARCHITECTURE DIAGRAM</h2>
    <p style="text-align: justify;">
        The system architecture of the AI-Based Business Analytics Dashboard follows a decoupled, 3-tier Modern Web Application architecture comprising the Client Presentation Layer, the Flask Application &amp; API Controller Layer, and the Data Processing &amp; Analytical Engine Layer.
    </p>

    <!-- Architecture Diagram SVG -->
    <div style="text-align: center; margin: 15px auto; padding: 12px; background: #fafafa; border: 1px solid #d0d0d0; border-radius: 6px;">
        <svg width="600" height="420" viewBox="0 0 600 420" xmlns="http://www.w3.org/2000/svg">
            <rect width="600" height="420" fill="#f8fafc" rx="8"/>
            
            <!-- User / Client Tier -->
            <rect x="20" y="30" width="160" height="360" rx="8" fill="#ffffff" stroke="#3b82f6" stroke-width="2"/>
            <text x="100" y="55" font-family="'Times New Roman', serif" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">PRESENTATION TIER</text>
            <text x="100" y="70" font-family="'Times New Roman', serif" font-size="10" fill="#64748b" text-anchor="middle">(Client Browser / SPA)</text>
            
            <rect x="35" y="90" width="130" height="45" rx="5" fill="#eff6ff" stroke="#93c5fd"/>
            <text x="100" y="112" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Executive Dashboard</text>
            <text x="100" y="125" font-family="'Times New Roman', serif" font-size="9" fill="#475569" text-anchor="middle">KPI Cards &amp; Dual Charts</text>
            
            <rect x="35" y="145" width="130" height="45" rx="5" fill="#eff6ff" stroke="#93c5fd"/>
            <text x="100" y="167" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Analytics Modules</text>
            <text x="100" y="180" font-family="'Times New Roman', serif" font-size="9" fill="#475569" text-anchor="middle">Sales, Product, Profit</text>

            <rect x="35" y="200" width="130" height="45" rx="5" fill="#eff6ff" stroke="#93c5fd"/>
            <text x="100" y="222" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Data Manager &amp; Clean</text>
            <text x="100" y="235" font-family="'Times New Roman', serif" font-size="9" fill="#475569" text-anchor="middle">Drag-Drop &amp; Imputation</text>

            <rect x="35" y="255" width="130" height="45" rx="5" fill="#eff6ff" stroke="#93c5fd"/>
            <text x="100" y="277" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">AI Insights &amp; NLP Chat</text>
            <text x="100" y="290" font-family="'Times New Roman', serif" font-size="9" fill="#475569" text-anchor="middle">Natural Language Q&amp;A</text>

            <rect x="35" y="310" width="130" height="45" rx="5" fill="#eff6ff" stroke="#93c5fd"/>
            <text x="100" y="332" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Chart.js Engine</text>
            <text x="100" y="345" font-family="'Times New Roman', serif" font-size="9" fill="#475569" text-anchor="middle">Rupee (₹) Tooltips</text>

            <!-- Arrows Presentation to Backend -->
            <path d="M 180 160 L 220 160" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)"/>
            <path d="M 220 230 L 180 230" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)"/>
            <text x="200" y="150" font-family="'Times New Roman', serif" font-size="9" fill="#0369a1" text-anchor="middle">HTTP REST</text>
            <text x="200" y="245" font-family="'Times New Roman', serif" font-size="9" fill="#0369a1" text-anchor="middle">JSON Data</text>

            <!-- Backend Application Tier -->
            <rect x="220" y="30" width="160" height="360" rx="8" fill="#ffffff" stroke="#10b981" stroke-width="2"/>
            <text x="300" y="55" font-family="'Times New Roman', serif" font-size="12" font-weight="bold" fill="#065f46" text-anchor="middle">APPLICATION TIER</text>
            <text x="300" y="70" font-family="'Times New Roman', serif" font-size="10" fill="#64748b" text-anchor="middle">(Python / Flask REST Server)</text>

            <rect x="235" y="90" width="130" height="45" rx="5" fill="#ecfdf5" stroke="#a7f3d0"/>
            <text x="300" y="112" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">REST API Routing</text>
            <text x="300" y="125" font-family="'Times New Roman', serif" font-size="9" fill="#047857" text-anchor="middle">app.py Endpoints</text>

            <rect x="235" y="145" width="130" height="45" rx="5" fill="#ecfdf5" stroke="#a7f3d0"/>
            <text x="300" y="167" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Payload Sanitizer</text>
            <text x="300" y="180" font-family="'Times New Roman', serif" font-size="9" fill="#047857" text-anchor="middle">NumpyJSONEncoder</text>

            <rect x="235" y="200" width="130" height="45" rx="5" fill="#ecfdf5" stroke="#a7f3d0"/>
            <text x="300" y="222" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Session &amp; Upload Handler</text>
            <text x="300" y="235" font-family="'Times New Roman', serif" font-size="9" fill="#047857" text-anchor="middle">secure_filename / 32MB</text>

            <rect x="235" y="255" width="130" height="45" rx="5" fill="#ecfdf5" stroke="#a7f3d0"/>
            <text x="300" y="277" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Report Generator</text>
            <text x="300" y="290" font-family="'Times New Roman', serif" font-size="9" fill="#047857" text-anchor="middle">PDF &amp; XLSX Exporter</text>

            <!-- Arrows Application to Analytics Tier -->
            <path d="M 380 160 L 420 160" stroke="#059669" stroke-width="2"/>
            <path d="M 420 230 L 380 230" stroke="#059669" stroke-width="2"/>
            <text x="400" y="150" font-family="'Times New Roman', serif" font-size="9" fill="#047857" text-anchor="middle">Invokes</text>
            <text x="400" y="245" font-family="'Times New Roman', serif" font-size="9" fill="#047857" text-anchor="middle">Returns</text>

            <!-- Analytics & Engine Tier -->
            <rect x="420" y="30" width="160" height="360" rx="8" fill="#ffffff" stroke="#8b5cf6" stroke-width="2"/>
            <text x="500" y="55" font-family="'Times New Roman', serif" font-size="12" font-weight="bold" fill="#5b21b6" text-anchor="middle">ANALYTICS TIER</text>
            <text x="500" y="70" font-family="'Times New Roman', serif" font-size="10" fill="#64748b" text-anchor="middle">(Analytics Engine / ML)</text>

            <rect x="435" y="90" width="130" height="45" rx="5" fill="#f5f3ff" stroke="#ddd6fe"/>
            <text x="500" y="112" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Pandas &amp; NumPy Core</text>
            <text x="500" y="125" font-family="'Times New Roman', serif" font-size="9" fill="#6d28d9" text-anchor="middle">DataFrames / Stats</text>

            <rect x="435" y="145" width="130" height="45" rx="5" fill="#f5f3ff" stroke="#ddd6fe"/>
            <text x="500" y="167" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Auto-Detect Schema</text>
            <text x="500" y="180" font-family="'Times New Roman', serif" font-size="9" fill="#6d28d9" text-anchor="middle">Sales, Profit, Date SKUs</text>

            <rect x="435" y="200" width="130" height="45" rx="5" fill="#f5f3ff" stroke="#ddd6fe"/>
            <text x="500" y="222" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Rule-Based AI Engine</text>
            <text x="500" y="235" font-family="'Times New Roman', serif" font-size="9" fill="#6d28d9" text-anchor="middle">Outliers, Growth, Risks</text>

            <rect x="435" y="255" width="130" height="45" rx="5" fill="#f5f3ff" stroke="#ddd6fe"/>
            <text x="500" y="277" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Natural Language Q&amp;A</text>
            <text x="500" y="290" font-family="'Times New Roman', serif" font-size="9" fill="#6d28d9" text-anchor="middle">Intent Parsing Engine</text>

            <rect x="435" y="310" width="130" height="45" rx="5" fill="#f5f3ff" stroke="#ddd6fe"/>
            <text x="500" y="332" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Datasets Storage</text>
            <text x="500" y="345" font-family="'Times New Roman', serif" font-size="9" fill="#6d28d9" text-anchor="middle">CSV / XLSX Datasets</text>
        </svg>
    </div>
    <div class="figure-caption">Fig 4.1 ARCHITECTURE DIAGRAM</div>
    """
    pages.append(wrap_page(p18, '<div class="page-num">18</div>'))

    # PAGE 19: 4.2 UML DIAGRAM - 4.2.1 USE CASE DIAGRAM
    p19 = """
    <h2 class="sec-title">4.2 UML DIAGRAM</h2>
    <h3 class="subsec-title">4.2.1 USE CASE DIAGRAM</h3>
    <p style="text-align: justify;">
        The Use Case Diagram models the functional interactions between the primary enterprise actors (Business Administrator / Data Analyst / Executive Viewer) and the core modules of the AI-Based Business Analytics Dashboard.
    </p>

    <!-- Use Case SVG -->
    <div style="text-align: center; margin: 15px auto; padding: 10px; background: #fafafa; border: 1px solid #d0d0d0; border-radius: 6px;">
        <svg width="580" height="440" viewBox="0 0 580 440" xmlns="http://www.w3.org/2000/svg">
            <rect width="580" height="440" fill="#ffffff" rx="8"/>
            <rect x="160" y="20" width="260" height="400" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
            <text x="290" y="42" font-family="'Times New Roman', serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">AI-Based Business Analytics Dashboard</text>

            <!-- Actor Left: Business Admin -->
            <circle cx="60" cy="140" r="15" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
            <line x1="60" y1="155" x2="60" y2="200" stroke="#dc2626" stroke-width="2"/>
            <line x1="60" y1="170" x2="35" y2="185" stroke="#dc2626" stroke-width="2"/>
            <line x1="60" y1="170" x2="85" y2="185" stroke="#dc2626" stroke-width="2"/>
            <line x1="60" y1="200" x2="40" y2="235" stroke="#dc2626" stroke-width="2"/>
            <line x1="60" y1="200" x2="80" y2="235" stroke="#dc2626" stroke-width="2"/>
            <text x="60" y="255" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Business Admin /</text>
            <text x="60" y="268" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Data Analyst</text>

            <!-- Actor Right: Executive Viewer -->
            <circle cx="520" cy="180" r="15" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>
            <line x1="520" y1="195" x2="520" y2="240" stroke="#4f46e5" stroke-width="2"/>
            <line x1="520" y1="210" x2="495" y2="225" stroke="#4f46e5" stroke-width="2"/>
            <line x1="520" y1="210" x2="545" y2="225" stroke="#4f46e5" stroke-width="2"/>
            <line x1="520" y1="240" x2="500" y2="275" stroke="#4f46e5" stroke-width="2"/>
            <line x1="520" y1="240" x2="540" y2="275" stroke="#4f46e5" stroke-width="2"/>
            <text x="520" y="295" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Executive Viewer /</text>
            <text x="520" y="308" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Stakeholder</text>

            <!-- Use Cases -->
            <ellipse cx="290" cy="70" rx="90" ry="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="290" y="74" font-family="'Times New Roman', serif" font-size="9.5" text-anchor="middle">Upload &amp; Clean Datasets</text>

            <ellipse cx="290" cy="115" rx="90" ry="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="290" y="119" font-family="'Times New Roman', serif" font-size="9.5" text-anchor="middle">Monitor Overview KPIs</text>

            <ellipse cx="290" cy="160" rx="90" ry="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="290" y="164" font-family="'Times New Roman', serif" font-size="9.5" text-anchor="middle">Analyze Sales Performance</text>

            <ellipse cx="290" cy="205" rx="90" ry="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="290" y="209" font-family="'Times New Roman', serif" font-size="9.5" text-anchor="middle">Track Product Revenue &amp; Shares</text>

            <ellipse cx="290" cy="250" rx="90" ry="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="290" y="254" font-family="'Times New Roman', serif" font-size="9.5" text-anchor="middle">Assess Profitability &amp; Margins</text>

            <ellipse cx="290" cy="295" rx="90" ry="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="290" y="299" font-family="'Times New Roman', serif" font-size="9.5" text-anchor="middle">Generate Rule-Based AI Insights</text>

            <ellipse cx="290" cy="340" rx="90" ry="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="290" y="344" font-family="'Times New Roman', serif" font-size="9.5" text-anchor="middle">Query Business via Natural Language</text>

            <ellipse cx="290" cy="385" rx="90" ry="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="290" y="389" font-family="'Times New Roman', serif" font-size="9.5" text-anchor="middle">Export PDF / Excel / CSV Reports</text>

            <!-- Connection lines Admin -->
            <line x1="85" y1="170" x2="200" y2="70" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="85" y1="170" x2="200" y2="115" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="85" y1="170" x2="200" y2="160" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="85" y1="170" x2="200" y2="205" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="85" y1="170" x2="200" y2="250" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="85" y1="170" x2="200" y2="295" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="85" y1="170" x2="200" y2="340" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="85" y1="170" x2="200" y2="385" stroke="#94a3b8" stroke-width="1.2"/>

            <!-- Connection lines Viewer -->
            <line x1="495" y1="210" x2="380" y2="115" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="495" y1="210" x2="380" y2="160" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="495" y1="210" x2="380" y2="205" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="495" y1="210" x2="380" y2="250" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="495" y1="210" x2="380" y2="295" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="495" y1="210" x2="380" y2="340" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="495" y1="210" x2="380" y2="385" stroke="#94a3b8" stroke-width="1.2"/>
        </svg>
    </div>
    <div class="figure-caption">Fig 4.2 USE CASE DIAGRAM</div>
    """
    pages.append(wrap_page(p19, '<div class="page-num">19</div>'))

    # PAGE 20: 4.2.2 CLASS DIAGRAM
    p20 = """
    <h3 class="subsec-title">4.2.2 CLASS DIAGRAM</h3>
    <p style="text-align: justify;">
        The Class Diagram illustrates the object-oriented structure of the system, highlighting the attributes, operations, and relationships across the BusinessAnalyticsEngine, Flask Controller, and Presentation Modules.
    </p>

    <!-- Class Diagram SVG -->
    <div style="text-align: center; margin: 15px auto; padding: 10px; background: #fafafa; border: 1px solid #d0d0d0; border-radius: 6px;">
        <svg width="580" height="440" viewBox="0 0 580 440" xmlns="http://www.w3.org/2000/svg">
            <rect width="580" height="440" fill="#ffffff" rx="8"/>

            <!-- Class 1: BusinessAnalyticsEngine -->
            <rect x="20" y="20" width="260" height="390" rx="4" fill="#ffffff" stroke="#1e293b" stroke-width="1.5"/>
            <rect x="20" y="20" width="260" height="28" fill="#1e293b"/>
            <text x="150" y="38" font-family="'Times New Roman', serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">BusinessAnalyticsEngine</text>
            <line x1="20" y1="130" x2="280" y2="130" stroke="#1e293b" stroke-width="1"/>
            
            <!-- Attributes -->
            <text x="26" y="60" font-family="'Courier New', monospace" font-size="8.5" fill="#334155">- data_dir: str</text>
            <text x="26" y="74" font-family="'Courier New', monospace" font-size="8.5" fill="#334155">- active_dataset_name: str</text>
            <text x="26" y="88" font-family="'Courier New', monospace" font-size="8.5" fill="#334155">- raw_df: DataFrame</text>
            <text x="26" y="102" font-family="'Courier New', monospace" font-size="8.5" fill="#334155">- df: DataFrame</text>
            <text x="26" y="116" font-family="'Courier New', monospace" font-size="8.5" fill="#334155">- column_mapping: dict</text>

            <!-- Methods -->
            <text x="26" y="146" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ load_dataset(filename): dict</text>
            <text x="26" y="160" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ clean_dataset(strategy, dedup): dict</text>
            <text x="26" y="174" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ get_overview_analytics(): dict</text>
            <text x="26" y="188" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ get_sales_analytics(f, t): dict</text>
            <text x="26" y="202" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ get_product_analytics(): dict</text>
            <text x="26" y="216" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ get_profit_analytics(): dict</text>
            <text x="26" y="230" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ generate_ai_insights(): dict</text>
            <text x="26" y="244" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ ask_ai(question): dict</text>
            <text x="26" y="258" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ export_csv_bytes(): bytes</text>
            <text x="26" y="272" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ export_excel_path(path): str</text>
            <text x="26" y="286" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ generate_analytical_report(): dict</text>

            <!-- Class 2: FlaskController -->
            <rect x="310" y="20" width="250" height="190" rx="4" fill="#ffffff" stroke="#1e293b" stroke-width="1.5"/>
            <rect x="310" y="20" width="250" height="28" fill="#1e293b"/>
            <text x="435" y="38" font-family="'Times New Roman', serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">FlaskController (app.py)</text>
            <line x1="310" y1="80" x2="560" y2="80" stroke="#1e293b" stroke-width="1"/>
            
            <text x="316" y="58" font-family="'Courier New', monospace" font-size="8.5" fill="#334155">- engine: BusinessAnalyticsEngine</text>
            <text x="316" y="72" font-family="'Courier New', monospace" font-size="8.5" fill="#334155">- upload_folder: str</text>

            <text x="316" y="96" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ index(): render_template</text>
            <text x="316" y="110" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ get_datasets(): Response</text>
            <text x="316" y="124" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ upload_dataset(): Response</text>
            <text x="316" y="138" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ clean_dataset(): Response</text>
            <text x="316" y="152" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ analytics_overview(): Response</text>
            <text x="316" y="166" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ ai_insights(): Response</text>
            <text x="316" y="180" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ ai_ask(): Response</text>
            <text x="316" y="194" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ export_csv(): Response</text>

            <!-- Class 3: ClientSPAManager -->
            <rect x="310" y="240" width="250" height="170" rx="4" fill="#ffffff" stroke="#1e293b" stroke-width="1.5"/>
            <rect x="310" y="240" width="250" height="28" fill="#1e293b"/>
            <text x="435" y="258" font-family="'Times New Roman', serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">ClientSPAManager (app.js)</text>
            <line x1="310" y1="300" x2="560" y2="300" stroke="#1e293b" stroke-width="1"/>

            <text x="316" y="278" font-family="'Courier New', monospace" font-size="8.5" fill="#334155">- currentRoute: str</text>
            <text x="316" y="292" font-family="'Courier New', monospace" font-size="8.5" fill="#334155">- activeDataset: str</text>

            <text x="316" y="316" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ init(): void</text>
            <text x="316" y="330" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ navigateTo(route): void</text>
            <text x="316" y="344" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ initTheme(): void</text>
            <text x="316" y="358" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ refreshDatasetSelector(): void</text>
            <text x="316" y="372" font-family="'Courier New', monospace" font-size="8.5" fill="#0f172a">+ showToast(msg, type): void</text>

            <!-- Relationship Lines -->
            <line x1="310" y1="100" x2="280" y2="100" stroke="#000" stroke-width="1.5"/>
            <polygon points="280,100 290,95 290,105" fill="#000"/>
            <text x="295" y="90" font-family="'Times New Roman', serif" font-size="8.5">1</text>
            <text x="302" y="90" font-family="'Times New Roman', serif" font-size="8.5">1</text>

            <line x1="435" y1="210" x2="435" y2="240" stroke="#000" stroke-width="1.5" stroke-dasharray="3,3"/>
            <polygon points="435,210 430,220 440,220" fill="none" stroke="#000"/>
        </svg>
    </div>
    <div class="figure-caption">Fig 4.3 CLASS DIAGRAM</div>
    """
    pages.append(wrap_page(p20, '<div class="page-num">20</div>'))

    # PAGE 21: 4.2.3 SEQUENCE DIAGRAM
    p21 = """
    <h3 class="subsec-title">4.2.3 SEQUENCE DIAGRAM</h3>
    <p style="text-align: justify;">
        The Sequence Diagram illustrates the step-by-step chronological interactions across system components during dataset upload, automated schema detection, cleaning, and natural language AI query processing.
    </p>

    <!-- Sequence Diagram SVG -->
    <div style="text-align: center; margin: 15px auto; padding: 10px; background: #fafafa; border: 1px solid #d0d0d0; border-radius: 6px;">
        <svg width="580" height="440" viewBox="0 0 580 440" xmlns="http://www.w3.org/2000/svg">
            <rect width="580" height="440" fill="#ffffff" rx="8"/>

            <!-- Lifelines -->
            <rect x="20" y="20" width="80" height="30" rx="4" fill="#1e293b"/>
            <text x="60" y="39" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">User</text>
            <line x1="60" y1="50" x2="60" y2="410" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

            <rect x="140" y="20" width="90" height="30" rx="4" fill="#3b82f6"/>
            <text x="185" y="39" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">Frontend SPA</text>
            <line x1="185" y1="50" x2="185" y2="410" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

            <rect x="280" y="20" width="100" height="30" rx="4" fill="#10b981"/>
            <text x="330" y="39" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">Flask REST API</text>
            <line x1="330" y1="50" x2="330" y2="410" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

            <rect x="430" y="20" width="120" height="30" rx="4" fill="#8b5cf6"/>
            <text x="490" y="39" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">Analytics Engine</text>
            <line x1="490" y1="50" x2="490" y2="410" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>

            <!-- Messages -->
            <!-- Step 1 Upload -->
            <line x1="60" y1="80" x2="185" y2="80" stroke="#000" stroke-width="1.2"/>
            <polygon points="185,80 177,76 177,84" fill="#000"/>
            <text x="120" y="74" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">1: Drop CSV File</text>

            <line x1="185" y1="105" x2="330" y2="105" stroke="#000" stroke-width="1.2"/>
            <polygon points="330,105 322,101 322,109" fill="#000"/>
            <text x="255" y="99" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">2: POST /api/dataset/upload</text>

            <line x1="330" y1="130" x2="490" y2="130" stroke="#000" stroke-width="1.2"/>
            <polygon points="490,130 482,126 482,134" fill="#000"/>
            <text x="410" y="124" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">3: load_dataset(filename)</text>

            <!-- Self execution: Detect Schema -->
            <path d="M 490 145 L 520 145 L 520 165 L 490 165" fill="none" stroke="#6d28d9" stroke-width="1.2"/>
            <text x="525" y="158" font-family="'Times New Roman', serif" font-size="8" fill="#6d28d9">Auto-detect columns</text>

            <line x1="490" y1="180" x2="330" y2="180" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
            <polygon points="330,180 338,176 338,184" fill="#000"/>
            <text x="410" y="174" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">4: overview data &amp; summary</text>

            <line x1="330" y1="205" x2="185" y2="205" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
            <polygon points="185,205 193,201 193,209" fill="#000"/>
            <text x="255" y="199" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">5: JSON {status, preview}</text>

            <line x1="185" y1="225" x2="60" y2="225" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
            <polygon points="60,225 68,221 68,229" fill="#000"/>
            <text x="120" y="219" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">6: Render Preview &amp; Toast</text>

            <!-- Step 2: Query Ask AI -->
            <line x1="60" y1="270" x2="185" y2="270" stroke="#000" stroke-width="1.2"/>
            <polygon points="185,270 177,266 177,274" fill="#000"/>
            <text x="120" y="264" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">7: Submit "Highest Sales Month?"</text>

            <line x1="185" y1="295" x2="330" y2="295" stroke="#000" stroke-width="1.2"/>
            <polygon points="330,295 322,291 322,299" fill="#000"/>
            <text x="255" y="289" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">8: POST /api/ai/ask {question}</text>

            <line x1="330" y1="320" x2="490" y2="320" stroke="#000" stroke-width="1.2"/>
            <polygon points="490,320 482,316 482,324" fill="#000"/>
            <text x="410" y="314" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">9: ask_ai(question)</text>

            <!-- Self execution: NLP intent matching -->
            <path d="M 490 335 L 520 335 L 520 355 L 490 355" fill="none" stroke="#6d28d9" stroke-width="1.2"/>
            <text x="525" y="348" font-family="'Times New Roman', serif" font-size="8" fill="#6d28d9">Regex NLP parsing</text>

            <line x1="490" y1="370" x2="330" y2="370" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
            <polygon points="330,370 338,366 338,374" fill="#000"/>
            <text x="410" y="364" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">10: formatted INR response</text>

            <line x1="330" y1="390" x2="185" y2="390" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
            <polygon points="185,390 193,386 193,394" fill="#000"/>
            <text x="255" y="384" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">11: JSON response</text>

            <line x1="185" y1="405" x2="60" y2="405" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
            <polygon points="60,405 68,401 68,409" fill="#000"/>
            <text x="120" y="399" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">12: Display AI Answer Card</text>
        </svg>
    </div>
    <div class="figure-caption">Fig 4.4 SEQUENCE DIAGRAM</div>
    """
    pages.append(wrap_page(p21, '<div class="page-num">21</div>'))

    return pages
