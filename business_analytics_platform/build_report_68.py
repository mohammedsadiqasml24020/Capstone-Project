#!/usr/bin/env python3
"""
Build 68-page AMET Capstone Project Report
AI-Based Business Analytics Dashboard
Student: MOHAMMED SADIQ.A | Reg No: ASML24020
"""
import os, sys, base64

if sys.platform.startswith('win'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs')
os.makedirs(DOCS, exist_ok=True)

# Load screenshots as base64 data URIs
def load_img(name):
    p = os.path.join(DOCS, name)
    if os.path.exists(p):
        with open(p, 'rb') as f:
            return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()
    return ''

IMG_OVERVIEW = load_img('screen_overview.png')
IMG_DATA = load_img('screen_datamanager.png')
IMG_SALES = load_img('screen_sales.png')
IMG_PRODUCTS = load_img('screen_products.png')
IMG_PROFIT = load_img('screen_profit.png')
IMG_AI = load_img('screen_ai_insights.png')
IMG_REPORTS = load_img('screen_reports.png')
IMG_MOBILE = load_img('screen_mobile.png')

# Read source code files
SRC = os.path.dirname(os.path.abspath(__file__))
def read_src(fname):
    p = os.path.join(SRC, fname)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            return f.read()
    return '# File not found'

APP_PY = read_src('app.py')
ENGINE_PY = read_src('analytics_engine.py')
TEST_PY = read_src('test_app.py')

def esc(t):
    return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

print("[1/4] Building CSS...")

CSS = """
@page { size: A4; margin: 25mm 25mm 25mm 30mm; }
@page:first { margin: 20mm; }
body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt; line-height: 1.5; color: #000;
    background: #fff; margin: 0; padding: 0; text-align: justify;
}
.page { page-break-after: always; min-height: 950px; box-sizing: border-box; }
.page:last-child { page-break-after: auto; }
.no-break { page-break-inside: avoid; }
.page-num { text-align: center; font-size: 11pt; margin-top: 20px; }
.roman-num { text-align: center; font-size: 11pt; margin-top: 20px; font-style: italic; }

h1.chapter-title {
    text-align: center; font-size: 16pt; font-weight: bold;
    text-transform: uppercase; margin: 40px 0 30px 0; letter-spacing: 0.5px;
}
h2.section-title {
    font-size: 14pt; font-weight: bold; margin: 25px 0 12px 0;
}
h3.subsection-title {
    font-size: 12pt; font-weight: bold; margin: 18px 0 8px 0;
}
p { margin: 0 0 12px 0; text-indent: 0; }
ul, ol { margin: 0 0 12px 0; padding-left: 30px; }
li { margin-bottom: 5px; }

table.at {
    width: 100%; border-collapse: collapse; margin: 15px 0 20px 0; font-size: 11pt;
}
table.at th, table.at td {
    border: 1px solid #000; padding: 7px 10px; text-align: left;
}
table.at th { background: #f0f0f0; font-weight: bold; text-align: center; }

.fig-cap { text-align: center; font-weight: bold; margin: 10px 0 20px 0; font-size: 11pt; }
.tbl-cap { text-align: center; font-weight: bold; margin: 12px 0 6px 0; font-size: 11pt; }

pre.code {
    background: #f8f9fa; border: 1px solid #ccc; padding: 10px;
    font-family: 'Courier New', monospace; font-size: 8.5pt;
    line-height: 1.3; white-space: pre-wrap; word-break: break-all;
    margin: 10px 0 15px 0; border-radius: 3px;
}

.cover-page {
    text-align: center; display: flex; flex-direction: column;
    justify-content: space-between; height: 940px;
}
.sig-container { display: flex; justify-content: space-between; margin-top: 80px; }
.sig-box { width: 45%; line-height: 1.4; font-size: 11pt; }
.examiner-sig { display: flex; justify-content: space-between; margin-top: 70px; font-size: 11pt; font-weight: bold; }

.toc-row { display: flex; justify-content: space-between; margin-bottom: 7px; font-size: 11.5pt; }
.toc-left { display: flex; flex: 1; }
.toc-num { width: 90px; font-weight: bold; }
.toc-title { flex: 1; padding-right: 8px; }
.toc-dots { flex-grow: 1; border-bottom: 1px dotted #555; margin: 0 6px; height: 14px; }
.toc-page { font-weight: bold; }

.diagram-box {
    text-align: center; margin: 18px 0; padding: 12px;
    border: 1px solid #ccc; background: #fafafa; border-radius: 5px;
}
.screenshot-img {
    max-width: 100%; border: 1px solid #999; border-radius: 4px;
    margin: 10px auto; display: block;
}
"""

print("[2/4] Building HTML pages...")

# ============== PAGE BUILDERS ==============

def page_cover():
    return """
<div class="page cover-page">
  <div>
    <div style="display:flex;align-items:center;justify-content:center;gap:20px;margin-bottom:20px;">
      <svg width="85" height="85" viewBox="0 0 200 200">
        <circle cx="100" cy="100" r="92" fill="#800000" stroke="#ffd700" stroke-width="4"/>
        <circle cx="100" cy="100" r="76" fill="#fff" stroke="#800000" stroke-width="2"/>
        <circle cx="100" cy="100" r="62" fill="#800000"/>
        <circle cx="100" cy="100" r="45" fill="none" stroke="#ffd700" stroke-width="5" stroke-dasharray="10,6"/>
        <path d="M100 65 L100 135 M85 100 L115 100 M75 125 C85 140 115 140 125 125" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
        <circle cx="100" cy="65" r="7" fill="#fff"/>
        <text x="100" y="24" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle" font-family="Times New Roman">ACADEMY OF MARITIME EDUCATION AND TRAINING</text>
        <text x="100" y="185" fill="#ffd700" font-size="12" font-weight="bold" text-anchor="middle" font-family="Times New Roman">DEEMED TO BE UNIVERSITY</text>
      </svg>
      <div style="text-align:left;">
        <div style="font-size:32pt;font-weight:900;color:#1a2a5e;letter-spacing:1.5px;line-height:1;">AMET</div>
        <div style="font-size:15pt;font-weight:700;color:#1e40af;letter-spacing:5px;line-height:1.2;">UNIVERSITY</div>
        <div style="font-size:7.5pt;color:#475569;font-style:italic;">(Deemed to be University Under Section 3 of UGC Act 1956)</div>
      </div>
    </div>

    <div style="font-size:18pt;font-weight:bold;letter-spacing:1px;margin:25px 0 15px;text-transform:uppercase;">
      AI-BASED BUSINESS ANALYTICS DASHBOARD
    </div>
    <div style="font-size:12pt;font-style:italic;margin-bottom:15px;">Submitted by</div>
    <div style="font-size:15pt;font-weight:bold;margin-bottom:6px;letter-spacing:0.5px;">MOHAMMED SADIQ.A</div>
    <div style="font-size:13pt;font-weight:bold;margin-bottom:20px;">Reg. No (ASML24020)</div>

    <div style="font-size:14pt;font-weight:bold;margin:20px 0 15px;">
      A PROJECT REPORT
    </div>
    <p style="font-size:12pt;text-align:center;max-width:500px;margin:0 auto 20px;">
      Submitted to the Faculty of Advanced Computing Sciences in partial fulfilment
      of the requirements for the award of the degree of
    </p>
    <div style="font-size:14pt;font-weight:bold;margin:15px 0;line-height:1.4;">
      BACHELOR OF SCIENCE<br/>
      IN<br/>
      ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING
    </div>
  </div>
  <div>
    <div style="font-size:13pt;font-weight:bold;margin:10px 0 20px;line-height:1.3;">
      DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND DATA SCIENCE<br/>
      FACULTY OF ADVANCED COMPUTING SCIENCES
    </div>
    <div style="font-size:12pt;font-weight:bold;line-height:1.4;margin-bottom:20px;">
      AMET University<br/>
      (Deemed to be University)<br/>
      Kanathur &ndash; 603 112, Tamil Nadu, India
    </div>
    <div style="font-size:13pt;font-weight:bold;letter-spacing:1px;">NOVEMBER 2026</div>
  </div>
</div>
"""

def page_certificate():
    return """
<div class="page">
  <h1 class="chapter-title" style="margin-bottom:20px;">BONAFIDE CERTIFICATE</h1>
  <p style="text-align:justify;line-height:2;margin-top:30px;">
    Certified that the project report titled <strong>&ldquo;AI-BASED BUSINESS ANALYTICS DASHBOARD&rdquo;</strong>
    is the bonafide work of <strong>MOHAMMED SADIQ.A</strong>, Registration Number <strong>ASML24020</strong>,
    who carried out the project under my supervision. This report is submitted to
    <strong>AMET University</strong> (Deemed to be University), Kanathur, in partial fulfilment of the
    requirements for the award of the degree of <strong>Bachelor of Science in Artificial Intelligence
    and Machine Learning (B.Sc. AIML)</strong> during the academic year <strong>2024&ndash;2026</strong>.
  </p>
  <div class="sig-container">
    <div class="sig-box">
      <br/><br/><br/>
      <strong>Mr. Tamilarasan D</strong><br/>
      Project Supervisor<br/>
      Department of AI &amp; Data Science<br/>
      AMET University
    </div>
    <div class="sig-box" style="text-align:right;">
      <br/><br/><br/>
      <strong>Dr. C.N. Ravi</strong><br/>
      Head of Department<br/>
      Department of AI &amp; Data Science<br/>
      AMET University
    </div>
  </div>
  <div style="margin-top:60px;font-size:11pt;">
    <strong>Viva-voce Examination held on:</strong> ____________________
  </div>
  <div class="examiner-sig">
    <div>Internal Examiner<br/><br/>Signature: ______________</div>
    <div>External Examiner<br/><br/>Signature: ______________</div>
  </div>
</div>
"""

def page_abstract():
    return """
<div class="page">
  <h1 class="chapter-title">ABSTRACT</h1>
  <p>In the modern era of data-driven decision-making, enterprises across industries generate vast volumes of transactional and operational data. However, extracting meaningful and actionable insights from raw data remains a significant challenge, particularly for Small and Medium-sized Enterprises (SMEs) that lack access to costly commercial analytics solutions such as Microsoft Power BI, Tableau, or SAP Analytics Cloud.</p>
  <p>This project presents the design, development, and implementation of an <strong>AI-Based Business Analytics Dashboard (NexusBI)</strong> &mdash; a comprehensive, web-based analytics platform built using Python, Flask, Pandas, NumPy, and Chart.js. The system enables business stakeholders to upload enterprise datasets in CSV or Excel format, perform automated data cleaning and preprocessing, and explore rich interactive visualisations covering sales performance, product analytics, profitability metrics, and temporal trend analysis.</p>
  <p>The distinguishing feature of this platform is its <strong>Rule-Based Artificial Intelligence Engine</strong> that automatically generates business insights by analysing statistical patterns, detecting anomalies, identifying seasonal trends, and computing key performance indicators (KPIs). Furthermore, the system incorporates a <strong>Natural Language Query Interface</strong> that allows non-technical users to ask questions in plain English (e.g., &ldquo;Which product generates the highest revenue?&rdquo;, &ldquo;What is the total profit?&rdquo;) and receive accurate, contextual responses derived directly from the underlying data.</p>
  <p>The application follows a modular Single-Page Application (SPA) architecture comprising seven independent modules: (1) Executive Overview Dashboard, (2) Data Ingestion and Management, (3) Sales Analytics, (4) Product Analytics, (5) Profit Analytics, (6) AI Business Insights, and (7) Reports and Export. All monetary values are formatted in the Indian Rupee (&lsquo;&#8377;&rsquo;) standard using the <em>en-IN</em> locale.</p>
  <p>The system was rigorously tested using a comprehensive unit-testing framework (Python <code>unittest</code>) covering 11 automated test cases across all API endpoints and analytical functions, achieving a 100% pass rate. The platform features a professional, responsive user interface with light and dark theme support, designed to function seamlessly across desktop, tablet, and mobile devices.</p>
  <p>This project demonstrates the practical application of Artificial Intelligence, Data Analytics, and Modern Web Development technologies to solve real-world business intelligence challenges, making enterprise-grade analytics accessible to organisations of all sizes.</p>
  <p><strong>Keywords:</strong> Business Analytics, Artificial Intelligence, Data Visualisation, Flask, Python, Dashboard, Natural Language Processing, KPI, Indian Rupee, SPA Architecture.</p>
  <div class="roman-num">i</div>
</div>
"""

print("  - Cover, Certificate, Abstract built")

def page_acknowledgement():
    return """
<div class="page">
  <h1 class="chapter-title">ACKNOWLEDGEMENT</h1>
  <p>I would like to express my sincere gratitude to all those who contributed to the successful completion of this project.</p>
  <p>First and foremost, I thank the <strong>Almighty</strong> for granting me the strength, wisdom, and perseverance to undertake and complete this endeavour.</p>
  <p>I am profoundly grateful to our Chancellor, <strong>Dr. S. Ramachandran</strong>, and our Vice-Chancellor for providing the institutional support and world-class academic infrastructure at AMET University that enabled this research.</p>
  <p>I extend my heartfelt thanks to <strong>Dr. C.N. Ravi</strong>, Head of the Department of Artificial Intelligence and Data Science, for his encouragement, administrative support, and for fostering an environment of academic excellence within the department.</p>
  <p>I express my deepest appreciation to my project supervisor, <strong>Mr. Tamilarasan D</strong>, for his invaluable guidance, constructive feedback, and continuous encouragement throughout the project. His expertise in software development and data analytics significantly shaped the direction and quality of this work.</p>
  <p>I sincerely thank all the <strong>faculty members</strong> of the Department of Artificial Intelligence and Data Science for imparting the theoretical knowledge and practical skills that formed the foundation of this project.</p>
  <p>I am thankful to the <strong>laboratory staff</strong> for ensuring the availability of computing resources and for providing timely technical assistance during the development and testing phases.</p>
  <p>I also wish to acknowledge the contributions of my <strong>classmates and friends</strong> who provided moral support, engaged in constructive discussions, and offered valuable suggestions that enhanced the quality of this project.</p>
  <p>Finally, I owe an immeasurable debt of gratitude to my <strong>parents and family</strong> for their unconditional love, unwavering support, constant encouragement, and the sacrifices they have made throughout my academic journey. This accomplishment would not have been possible without them.</p>
  <p style="text-align:right;margin-top:40px;"><strong>MOHAMMED SADIQ.A</strong></p>
  <div class="roman-num">ii</div>
</div>
"""

def page_toc():
    return """
<div class="page">
  <h1 class="chapter-title">TABLE OF CONTENTS</h1>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title"><strong>CHAPTER</strong></div></div><div class="toc-dots"></div><div class="toc-page"><strong>PAGE NO.</strong></div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">ABSTRACT</div></div><div class="toc-dots"></div><div class="toc-page">i</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">ACKNOWLEDGEMENT</div></div><div class="toc-dots"></div><div class="toc-page">ii</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">TABLE OF CONTENTS</div></div><div class="toc-dots"></div><div class="toc-page">iii</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">LIST OF FIGURES</div></div><div class="toc-dots"></div><div class="toc-page">v</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">LIST OF TABLES</div></div><div class="toc-dots"></div><div class="toc-page">vi</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">LIST OF ABBREVIATIONS</div></div><div class="toc-dots"></div><div class="toc-page">vii</div></div>

  <div style="margin-top:15px;"></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num">1</div><div class="toc-title"><strong>INTRODUCTION</strong></div></div><div class="toc-dots"></div><div class="toc-page">1</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">1.1 Background of the Study</div></div><div class="toc-dots"></div><div class="toc-page">1</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">1.2 Problem Statement</div></div><div class="toc-dots"></div><div class="toc-page">2</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">1.3 Objectives of the Project</div></div><div class="toc-dots"></div><div class="toc-page">3</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">1.4 Scope and Limitations</div></div><div class="toc-dots"></div><div class="toc-page">4</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">1.5 Organisation of the Report</div></div><div class="toc-dots"></div><div class="toc-page">5</div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num">2</div><div class="toc-title"><strong>SYSTEM ANALYSIS</strong></div></div><div class="toc-dots"></div><div class="toc-page">7</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">2.1 Existing System</div></div><div class="toc-dots"></div><div class="toc-page">7</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">2.2 Proposed System</div></div><div class="toc-dots"></div><div class="toc-page">8</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">2.3 Feasibility Study</div></div><div class="toc-dots"></div><div class="toc-page">10</div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num">3</div><div class="toc-title"><strong>SYSTEM REQUIREMENTS SPECIFICATION</strong></div></div><div class="toc-dots"></div><div class="toc-page">13</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">3.1 Hardware Requirements</div></div><div class="toc-dots"></div><div class="toc-page">13</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">3.2 Software Requirements</div></div><div class="toc-dots"></div><div class="toc-page">14</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">3.3 Functional Requirements</div></div><div class="toc-dots"></div><div class="toc-page">15</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">3.4 Non-Functional Requirements</div></div><div class="toc-dots"></div><div class="toc-page">16</div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num">4</div><div class="toc-title"><strong>SYSTEM DESIGN</strong></div></div><div class="toc-dots"></div><div class="toc-page">18</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">4.1 System Architecture</div></div><div class="toc-dots"></div><div class="toc-page">18</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">4.2 Use Case Diagram</div></div><div class="toc-dots"></div><div class="toc-page">20</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">4.3 Class Diagram</div></div><div class="toc-dots"></div><div class="toc-page">22</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">4.4 Sequence Diagram</div></div><div class="toc-dots"></div><div class="toc-page">24</div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num">5</div><div class="toc-title"><strong>MODULE DESCRIPTION</strong></div></div><div class="toc-dots"></div><div class="toc-page">26</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">5.1 Overview Dashboard Module</div></div><div class="toc-dots"></div><div class="toc-page">26</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">5.2 Data Upload &amp; Management Module</div></div><div class="toc-dots"></div><div class="toc-page">27</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">5.3 Sales Analytics Module</div></div><div class="toc-dots"></div><div class="toc-page">28</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">5.4 Product Analytics Module</div></div><div class="toc-dots"></div><div class="toc-page">29</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">5.5 Profit Analytics Module</div></div><div class="toc-dots"></div><div class="toc-page">30</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">5.6 AI Business Insights Module</div></div><div class="toc-dots"></div><div class="toc-page">31</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">5.7 Reports &amp; Export Module</div></div><div class="toc-dots"></div><div class="toc-page">32</div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num">6</div><div class="toc-title"><strong>SYSTEM IMPLEMENTATION AND CODING</strong></div></div><div class="toc-dots"></div><div class="toc-page">34</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">6.1 Application Entry Point (app.py)</div></div><div class="toc-dots"></div><div class="toc-page">34</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">6.2 Analytics Engine (analytics_engine.py)</div></div><div class="toc-dots"></div><div class="toc-page">38</div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num">7</div><div class="toc-title"><strong>SYSTEM TESTING</strong></div></div><div class="toc-dots"></div><div class="toc-page">48</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">7.1 Testing Strategy</div></div><div class="toc-dots"></div><div class="toc-page">48</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">7.2 Test Cases and Results</div></div><div class="toc-dots"></div><div class="toc-page">49</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">7.3 Test Code Listing</div></div><div class="toc-dots"></div><div class="toc-page">50</div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num">8</div><div class="toc-title"><strong>SCREENSHOTS AND APPENDICES</strong></div></div><div class="toc-dots"></div><div class="toc-page">54</div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num">9</div><div class="toc-title"><strong>CONCLUSION AND FUTURE ENHANCEMENT</strong></div></div><div class="toc-dots"></div><div class="toc-page">64</div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title"><strong>REFERENCES</strong></div></div><div class="toc-dots"></div><div class="toc-page">67</div></div>
  <div class="roman-num">iii</div>
</div>

<div class="page">
  <h1 class="chapter-title" style="font-size:14pt;">TABLE OF CONTENTS (Continued)</h1>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title"><strong>CHAPTER</strong></div></div><div class="toc-dots"></div><div class="toc-page"><strong>PAGE NO.</strong></div></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.1 Overview Dashboard Screenshot</div></div><div class="toc-dots"></div><div class="toc-page">54</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.2 Data Management Screenshot</div></div><div class="toc-dots"></div><div class="toc-page">55</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.3 Sales Analytics Screenshot</div></div><div class="toc-dots"></div><div class="toc-page">56</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.4 Product Analytics Screenshot</div></div><div class="toc-dots"></div><div class="toc-page">57</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.5 Profit Analytics Screenshot</div></div><div class="toc-dots"></div><div class="toc-page">58</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.6 AI Business Insights Screenshot</div></div><div class="toc-dots"></div><div class="toc-page">59</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.7 Reports &amp; Export Screenshot</div></div><div class="toc-dots"></div><div class="toc-page">60</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.8 Mobile Responsive View</div></div><div class="toc-dots"></div><div class="toc-page">61</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.9 Data Dictionary</div></div><div class="toc-dots"></div><div class="toc-page">62</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">8.10 API Endpoints Reference</div></div><div class="toc-dots"></div><div class="toc-page">63</div></div>

  <div style="margin-top:15px;"></div>

  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">9.1 Conclusion</div></div><div class="toc-dots"></div><div class="toc-page">64</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">9.2 Limitations</div></div><div class="toc-dots"></div><div class="toc-page">65</div></div>
  <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left:15px;">9.3 Future Enhancements</div></div><div class="toc-dots"></div><div class="toc-page">66</div></div>
  <div class="roman-num">iv</div>
</div>
"""

print("  - Acknowledgement, TOC built")

def page_list_of_figures():
    return """
<div class="page">
  <h1 class="chapter-title">LIST OF FIGURES</h1>
  <table class="at">
    <tr><th>Figure No.</th><th>Title</th><th>Page No.</th></tr>
    <tr><td style="text-align:center;">4.1</td><td>System Architecture Diagram</td><td style="text-align:center;">19</td></tr>
    <tr><td style="text-align:center;">4.2</td><td>Use Case Diagram</td><td style="text-align:center;">21</td></tr>
    <tr><td style="text-align:center;">4.3</td><td>Class Diagram</td><td style="text-align:center;">23</td></tr>
    <tr><td style="text-align:center;">4.4</td><td>Sequence Diagram</td><td style="text-align:center;">25</td></tr>
    <tr><td style="text-align:center;">8.1</td><td>Overview Dashboard &ndash; Desktop View</td><td style="text-align:center;">54</td></tr>
    <tr><td style="text-align:center;">8.2</td><td>Data Upload &amp; Management Module</td><td style="text-align:center;">55</td></tr>
    <tr><td style="text-align:center;">8.3</td><td>Sales Analytics Module</td><td style="text-align:center;">56</td></tr>
    <tr><td style="text-align:center;">8.4</td><td>Product Analytics Module</td><td style="text-align:center;">57</td></tr>
    <tr><td style="text-align:center;">8.5</td><td>Profit Analytics Module</td><td style="text-align:center;">58</td></tr>
    <tr><td style="text-align:center;">8.6</td><td>AI Business Insights Module</td><td style="text-align:center;">59</td></tr>
    <tr><td style="text-align:center;">8.7</td><td>Reports &amp; Export Module</td><td style="text-align:center;">60</td></tr>
    <tr><td style="text-align:center;">8.8</td><td>Mobile Responsive View</td><td style="text-align:center;">61</td></tr>
  </table>
  <div class="roman-num">v</div>
</div>
"""

def page_list_of_tables():
    return """
<div class="page">
  <h1 class="chapter-title">LIST OF TABLES</h1>
  <table class="at">
    <tr><th>Table No.</th><th>Title</th><th>Page No.</th></tr>
    <tr><td style="text-align:center;">2.1</td><td>Comparison of Existing and Proposed Systems</td><td style="text-align:center;">9</td></tr>
    <tr><td style="text-align:center;">3.1</td><td>Hardware Requirements Specification</td><td style="text-align:center;">13</td></tr>
    <tr><td style="text-align:center;">3.2</td><td>Software Requirements Specification</td><td style="text-align:center;">14</td></tr>
    <tr><td style="text-align:center;">3.3</td><td>Technology Stack and Libraries</td><td style="text-align:center;">15</td></tr>
    <tr><td style="text-align:center;">5.1</td><td>Module Summary with Features</td><td style="text-align:center;">33</td></tr>
    <tr><td style="text-align:center;">7.1</td><td>Unit Test Cases and Results</td><td style="text-align:center;">49</td></tr>
    <tr><td style="text-align:center;">7.2</td><td>Integration Test Results Summary</td><td style="text-align:center;">50</td></tr>
    <tr><td style="text-align:center;">8.1</td><td>Enterprise Sales Dataset Schema</td><td style="text-align:center;">62</td></tr>
    <tr><td style="text-align:center;">8.2</td><td>API Endpoints Reference Table</td><td style="text-align:center;">63</td></tr>
  </table>
  <div class="roman-num">vi</div>
</div>
"""

def page_abbreviations():
    return """
<div class="page">
  <h1 class="chapter-title">LIST OF ABBREVIATIONS</h1>
  <table class="at">
    <tr><th>Abbreviation</th><th>Expansion</th></tr>
    <tr><td>AI</td><td>Artificial Intelligence</td></tr>
    <tr><td>AIML</td><td>Artificial Intelligence and Machine Learning</td></tr>
    <tr><td>API</td><td>Application Programming Interface</td></tr>
    <tr><td>B.Sc.</td><td>Bachelor of Science</td></tr>
    <tr><td>CDN</td><td>Content Delivery Network</td></tr>
    <tr><td>CPU</td><td>Central Processing Unit</td></tr>
    <tr><td>CRUD</td><td>Create, Read, Update, Delete</td></tr>
    <tr><td>CSS</td><td>Cascading Style Sheets</td></tr>
    <tr><td>CSV</td><td>Comma-Separated Values</td></tr>
    <tr><td>DOM</td><td>Document Object Model</td></tr>
    <tr><td>GB</td><td>Gigabyte</td></tr>
    <tr><td>HTML</td><td>Hypertext Markup Language</td></tr>
    <tr><td>HTTP</td><td>Hypertext Transfer Protocol</td></tr>
    <tr><td>IDE</td><td>Integrated Development Environment</td></tr>
    <tr><td>INR</td><td>Indian Rupee</td></tr>
    <tr><td>JSON</td><td>JavaScript Object Notation</td></tr>
    <tr><td>KPI</td><td>Key Performance Indicator</td></tr>
    <tr><td>ML</td><td>Machine Learning</td></tr>
    <tr><td>NLP</td><td>Natural Language Processing</td></tr>
    <tr><td>OS</td><td>Operating System</td></tr>
    <tr><td>PDF</td><td>Portable Document Format</td></tr>
    <tr><td>RAM</td><td>Random Access Memory</td></tr>
    <tr><td>REST</td><td>Representational State Transfer</td></tr>
    <tr><td>SME</td><td>Small and Medium-sized Enterprise</td></tr>
    <tr><td>SPA</td><td>Single-Page Application</td></tr>
    <tr><td>SRS</td><td>Software Requirements Specification</td></tr>
    <tr><td>SVG</td><td>Scalable Vector Graphics</td></tr>
    <tr><td>UI</td><td>User Interface</td></tr>
    <tr><td>URL</td><td>Uniform Resource Locator</td></tr>
    <tr><td>UX</td><td>User Experience</td></tr>
    <tr><td>WSGI</td><td>Web Server Gateway Interface</td></tr>
    <tr><td>XLSX</td><td>Microsoft Excel Open XML Spreadsheet</td></tr>
  </table>
  <div class="roman-num">vii</div>
</div>
"""

print("  - List of Figures, Tables, Abbreviations built")

def chapter1():
    return """
<div class="page">
  <h1 class="chapter-title">CHAPTER 1<br/>INTRODUCTION</h1>

  <h2 class="section-title">1.1 Background of the Study</h2>
  <p>The contemporary business landscape is characterised by an unprecedented volume, velocity, and variety of data generated across every operational facet of an enterprise. From point-of-sale transactions and supply-chain logistics to customer relationship management and digital marketing campaigns, organisations accumulate massive datasets that hold the potential to drive strategic decision-making and competitive advantage. The field of Business Analytics has emerged as a critical discipline that leverages statistical analysis, data mining, predictive modelling, and visualisation techniques to transform raw data into actionable intelligence.</p>
  <p>According to a report by Grand View Research (2023), the global business intelligence and analytics market was valued at approximately USD 27.11 billion in 2022 and is projected to grow at a Compound Annual Growth Rate (CAGR) of 13.5% from 2023 to 2030. This exponential growth underscores the increasing recognition among enterprises that data-driven strategies yield measurably superior outcomes in revenue optimisation, cost reduction, and operational efficiency.</p>
  <p>However, the adoption of sophisticated analytics tools remains disproportionately concentrated among large corporations that can afford enterprise-grade solutions such as Microsoft Power BI (Pro licences starting at approximately &#8377;820 per user per month), Tableau (Team edition at approximately &#8377;5,800 per user per month), and SAP Analytics Cloud. Small and Medium-sized Enterprises (SMEs), which constitute over 90% of businesses in India and contribute approximately 30% to the nation's GDP, frequently lack both the financial resources and the technical expertise to deploy, configure, and maintain such platforms.</p>
  <p>This disparity creates a significant gap in the analytics ecosystem: the organisations that stand to benefit most from data-driven insights are precisely those that are least equipped to access them. The AI-Based Business Analytics Dashboard project addresses this gap by providing an open-source, web-based analytics platform that combines the power of Python's data-science ecosystem with modern web technologies to deliver enterprise-grade analytical capabilities without the prohibitive costs associated with commercial solutions.</p>

  <h2 class="section-title">1.2 Problem Statement</h2>
  <p>Despite the acknowledged importance of business analytics, SMEs in India face several critical barriers to adoption:</p>
  <ol>
    <li><strong>Prohibitive Cost:</strong> Commercial analytics platforms require significant upfront investment and recurring subscription fees that are not economically viable for small businesses operating on tight margins.</li>
    <li><strong>Technical Complexity:</strong> Existing tools often require specialised training, database connectivity configurations, and IT infrastructure that exceeds the capabilities of non-technical business owners.</li>
    <li><strong>Limited Customisation:</strong> Off-the-shelf solutions provide generic dashboards that may not align with the specific KPIs, metrics, and reporting formats relevant to a particular industry or business model.</li>
    <li><strong>Data Privacy Concerns:</strong> Cloud-based commercial platforms require uploading sensitive business data to third-party servers, raising concerns about data sovereignty, regulatory compliance, and confidentiality.</li>
    <li><strong>Absence of AI-Driven Insights:</strong> While dashboards display charts and numbers, they rarely provide interpretive, actionable recommendations that translate data patterns into concrete business strategies.</li>
  </ol>
  <p>The problem, therefore, is to design and develop a cost-effective, user-friendly, and intelligent analytics platform that empowers non-technical stakeholders to derive meaningful insights from their business data without requiring advanced technical skills, expensive licences, or external IT support.</p>
  <div class="page-num">2</div>
</div>

<div class="page">
  <h2 class="section-title">1.3 Objectives of the Project</h2>
  <p>The primary objectives of this project are as follows:</p>
  <ol>
    <li>To design and develop a modern, responsive, web-based Business Analytics Dashboard that provides professional-grade visualisations and interactive data exploration capabilities.</li>
    <li>To implement a robust data ingestion engine that supports multiple file formats (CSV and XLSX), provides automated data quality assessment, and offers configurable data cleaning and preprocessing pipelines.</li>
    <li>To create comprehensive analytical modules covering Sales Analytics, Product Analytics, and Profit Analytics with interactive charts, statistical summaries, and date-based filtering capabilities.</li>
    <li>To develop a Rule-Based AI Engine that automatically generates business insights by analysing statistical patterns, detecting anomalies, identifying trends, and producing actionable recommendations.</li>
    <li>To implement a Natural Language Query Interface that enables users to ask business questions in plain English and receive accurate, data-driven answers without requiring knowledge of query languages or programming.</li>
    <li>To provide a multi-format reporting and export subsystem that generates analytical reports and supports export to PDF, CSV, and Excel formats for offline distribution and archival.</li>
    <li>To ensure the platform adheres to the Indian Rupee (&#8377;) standard with <em>en-IN</em> locale formatting for all monetary values, making it suitable for Indian business contexts.</li>
    <li>To implement responsive design with light and dark theme support, ensuring accessibility across desktop, tablet, and mobile devices.</li>
  </ol>

  <h2 class="section-title">1.4 Scope and Limitations</h2>
  <h3 class="subsection-title">1.4.1 Scope</h3>
  <p>The scope of this project encompasses the following:</p>
  <ul>
    <li>Development of a complete, functional web application with a Flask-based backend and a Single-Page Application (SPA) frontend.</li>
    <li>Implementation of seven independent analytical modules as specified in the requirements.</li>
    <li>Support for datasets up to 32 MB in size, accommodating the typical data volumes of SMEs.</li>
    <li>Deployment-ready architecture suitable for local deployment, intranet hosting, or cloud deployment on platforms such as Railway, Render, or AWS.</li>
  </ul>
  <h3 class="subsection-title">1.4.2 Limitations</h3>
  <ul>
    <li>The AI engine is rule-based and does not employ deep learning or large language models; its analytical capabilities are bounded by the predefined rule set.</li>
    <li>The system operates on single-user mode without authentication or role-based access control.</li>
    <li>Real-time streaming data ingestion is not supported; datasets must be uploaded as static files.</li>
    <li>The natural language query interface supports a defined set of question patterns and may not handle highly ambiguous or complex queries.</li>
  </ul>
  <div class="page-num">4</div>
</div>

<div class="page">
  <h2 class="section-title">1.5 Organisation of the Report</h2>
  <p>This report is organised into nine chapters, each addressing a specific aspect of the project lifecycle:</p>
  <ul>
    <li><strong>Chapter 1 &ndash; Introduction:</strong> Provides the background, problem statement, objectives, scope, and limitations of the project.</li>
    <li><strong>Chapter 2 &ndash; System Analysis:</strong> Analyses the existing systems, presents the proposed system, and includes a comprehensive feasibility study covering technical, operational, and economic dimensions.</li>
    <li><strong>Chapter 3 &ndash; System Requirements Specification:</strong> Documents the hardware requirements, software requirements, functional requirements, and non-functional requirements of the system.</li>
    <li><strong>Chapter 4 &ndash; System Design:</strong> Presents the system architecture, Use Case Diagram, Class Diagram, and Sequence Diagram using standardised UML notations.</li>
    <li><strong>Chapter 5 &ndash; Module Description:</strong> Provides detailed descriptions of all seven modules, including their features, data flows, and user interactions.</li>
    <li><strong>Chapter 6 &ndash; System Implementation and Coding:</strong> Presents the core implementation with annotated source code listings for the Flask application and the Analytics Engine.</li>
    <li><strong>Chapter 7 &ndash; System Testing:</strong> Describes the testing strategy, presents the test cases and results, and includes the complete test code listing.</li>
    <li><strong>Chapter 8 &ndash; Screenshots and Appendices:</strong> Contains application screenshots, data dictionaries, and the API endpoints reference.</li>
    <li><strong>Chapter 9 &ndash; Conclusion and Future Enhancement:</strong> Summarises the project outcomes, discusses limitations, and proposes directions for future development.</li>
  </ul>
  <div class="page-num">6</div>
</div>
"""

print("  - Chapter 1 built")
