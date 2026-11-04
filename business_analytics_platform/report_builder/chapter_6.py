import html
from report_builder.config import wrap_page

def get_chapter_6(app_lines, eng_lines):
    pages = []

    # Helper to slice lines and format as code block
    def format_code(lines_list, start_idx, end_idx, title=""):
        sub = lines_list[start_idx:end_idx]
        code_text = "".join(sub)
        esc_code = html.escape(code_text)
        title_html = f'<div style="font-size: 10pt; font-weight: bold; margin-bottom: 4px; color: #1e3a8a;">{title}</div>' if title else ""
        return f"""{title_html}
        <div class="code-container" style="max-height: 195mm; overflow: hidden; font-size: 8pt; line-height: 1.3;">{esc_code}</div>
        """

    # PAGE 30: CHAPTER 6 SYSTEM IMPLEMENTATION - 6.1 CODING & app.py Part 1
    p30_content = f"""
    <h1 class="chap-title">CHAPTER 6<br>SYSTEM IMPLEMENTATION</h1>
    <h2 class="sec-title">6.1 IMPLEMENTATION AND CODING</h2>
    <p style="text-align: justify; margin-bottom: 6px;">
        The system implementation encompasses the Flask application routing controllers (<code>app.py</code>) and the analytical processing engine (<code>analytics_engine.py</code>). All source code adheres to modern Python 3 standards, PEP 8 guidelines, and strict UTF-8 Indian Rupee (&#8377;) encoding.
    </p>
    {format_code(app_lines, 0, 48, "PYTHON FLASK SERVER ENTRY POINT (app.py - Lines 1 to 48)")}
    """
    pages.append(wrap_page(p30_content, '<div class="page-num">30</div>'))

    # PAGE 31: app.py Part 2 (Dataset Management Routes)
    p31_content = f"""
    {format_code(app_lines, 48, 102, "DATASET SELECTION & UPLOAD REST APIS (app.py - Lines 49 to 102)")}
    """
    pages.append(wrap_page(p31_content, '<div class="page-num">31</div>'))

    # PAGE 32: app.py Part 3 (Cleaning & Export APIs)
    p32_content = f"""
    {format_code(app_lines, 102, 158, "DATASET CLEANING & EXPORT DISPATCHERS (app.py - Lines 103 to 158)")}
    """
    pages.append(wrap_page(p32_content, '<div class="page-num">32</div>'))

    # PAGE 33: app.py Part 4 (Analytics Endpoints)
    p33_content = f"""
    {format_code(app_lines, 158, 208, "ANALYTICS & AI RESTFUL ENDPOINTS (app.py - Lines 159 to 208)")}
    """
    pages.append(wrap_page(p33_content, '<div class="page-num">33</div>'))

    # PAGE 34: app.py Part 5 (Reporting & Server Initialization)
    p34_content = f"""
    {format_code(app_lines, 208, len(app_lines), "ANALYTICAL REPORT & SERVER INITIALIZER (app.py - Lines 209 to End)")}
    """
    pages.append(wrap_page(p34_content, '<div class="page-num">34</div>'))

    # PBI 35 to 51: analytics_engine.py (17 pages for 1006 lines = ~60 lines per page)
    total_eng = len(eng_lines)
    step = 58
    curr_idx = 0

    page_titles = [
        "ANALYTICS ENGINE CLASS INITIALIZER (analytics_engine.py)",
        "AUTOMATIC COLUMN & SCHEMA DETECTION (analytics_engine.py)",
        "DATASET OVERVIEW & SUMMARY STATISTICS (analytics_engine.py)",
        "DATA CLEANING & IMPUTATION ROUTINES (analytics_engine.py)",
        "OVERVIEW ANALYTICS & CORRELATION ENGINE (analytics_engine.py)",
        "MONTHLY & DAILY SALES COMPUTATION (analytics_engine.py)",
        "TEMPORAL GROWTH RATE & ANOMALY MODELS (analytics_engine.py)",
        "PRODUCT PERFORMANCE & CONTRIBUTION (analytics_engine.py)",
        "CATEGORY AGGREGATION & PARETO METRICS (analytics_engine.py)",
        "PROFIT ANALYTICS & MARGIN GAUGES (analytics_engine.py)",
        "PRODUCT MARGIN RANKING & COST ANALYSIS (analytics_engine.py)",
        "RULE-BASED AI INSIGHTS GENERATOR (analytics_engine.py)",
        "STATISTICAL Z-SCORE OUTLIER DETECTOR (analytics_engine.py)",
        "NATURAL LANGUAGE QUERY INTENT PARSER (analytics_engine.py)",
        "ASK AI PATTERN MATCHER & RESPONDER (analytics_engine.py)",
        "CONSOLIDATED ANALYTICAL REPORT BUILDER (analytics_engine.py)",
        "SPREADSHEET EXPORT ENGINE & DATA PIPELINES (analytics_engine.py)"
    ]

    for p_num in range(35, 52):
        t_idx = p_num - 35
        p_title = page_titles[t_idx] if t_idx < len(page_titles) else "ANALYTICS ENGINE MODULE (analytics_engine.py)"
        end_idx = min(curr_idx + step, total_eng)
        content_code = format_code(eng_lines, curr_idx, end_idx, f"{p_title} - Lines {curr_idx+1} to {end_idx}")
        curr_idx = end_idx
        pages.append(wrap_page(content_code, f'<div class="page-num">{p_num}</div>'))

    return pages
