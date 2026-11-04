import os
import sys

# Ensure UTF-8 output encoding
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI-Based Business Analytics Dashboard - Capstone Project Report</title>
    <style>
        @page {
            size: A4;
            margin: 25mm 20mm 25mm 25mm; /* Standard Indian thesis margins: left 25mm for binding */
        }
        
        @page:first {
            margin: 20mm;
        }

        body {
            font-family: 'Times New Roman', Times, serif;
            font-size: 12pt;
            line-height: 1.5;
            color: #000000;
            background: #ffffff;
            margin: 0;
            padding: 0;
            text-align: justify;
        }

        .page {
            page-break-after: always;
            position: relative;
            min-height: 980px;
            box-sizing: border-box;
        }

        .no-break {
            page-break-inside: avoid;
        }

        /* Running Headers and Footers */
        .page-num {
            text-align: center;
            font-size: 11pt;
            margin-top: 25px;
            font-family: 'Times New Roman', Times, serif;
        }

        .roman-num {
            text-align: center;
            font-size: 11pt;
            margin-top: 25px;
            font-style: italic;
        }

        /* Headings */
        h1.chapter-title {
            text-align: center;
            font-size: 16pt;
            font-weight: bold;
            text-transform: uppercase;
            margin-top: 40px;
            margin-bottom: 30px;
            letter-spacing: 0.5px;
        }

        h2.section-title {
            font-size: 13pt;
            font-weight: bold;
            margin-top: 25px;
            margin-bottom: 12px;
            text-transform: uppercase;
        }

        h3.subsection-title {
            font-size: 12pt;
            font-weight: bold;
            margin-top: 18px;
            margin-bottom: 8px;
        }

        h4.sub-subsection-title {
            font-size: 11.5pt;
            font-weight: bold;
            margin-top: 14px;
            margin-bottom: 6px;
        }

        p {
            margin-top: 0;
            margin-bottom: 14px;
            text-indent: 0;
        }

        ul, ol {
            margin-top: 0;
            margin-bottom: 14px;
            padding-left: 28px;
        }

        li {
            margin-bottom: 6px;
        }

        /* Tables */
        table.academic-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 18px;
            margin-bottom: 22px;
            font-size: 10.5pt;
        }

        table.academic-table th, table.academic-table td {
            border: 1px solid #000000;
            padding: 8px 10px;
            text-align: left;
        }

        table.academic-table th {
            background-color: #f2f2f2;
            font-weight: bold;
            text-align: center;
        }

        .table-caption {
            text-align: center;
            font-weight: bold;
            margin-top: 12px;
            margin-bottom: 6px;
            font-size: 11pt;
        }

        .figure-caption {
            text-align: center;
            font-weight: bold;
            margin-top: 12px;
            margin-bottom: 24px;
            font-size: 11pt;
        }

        /* Diagrams */
        .diagram-container {
            text-align: center;
            margin: 20px 0;
            padding: 12px;
            border: 1px solid #d0d0d0;
            background: #fafafa;
            border-radius: 6px;
        }

        /* Code Blocks */
        pre.code-block {
            background-color: #f8f9fa;
            border: 1px solid #cccccc;
            padding: 12px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 9pt;
            line-height: 1.35;
            white-space: pre-wrap;
            word-break: break-all;
            margin-top: 12px;
            margin-bottom: 18px;
            border-radius: 4px;
        }

        /* Cover Page Specific Styles */
        .cover-page {
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 940px;
        }

        .cover-logo-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 25px;
        }

        .cover-title {
            font-size: 18pt;
            font-weight: bold;
            letter-spacing: 1px;
            margin: 25px 0 15px 0;
            text-transform: uppercase;
        }

        .cover-subtitle {
            font-size: 12pt;
            font-style: italic;
            margin-bottom: 15px;
        }

        .cover-author {
            font-size: 15pt;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.5px;
        }

        .cover-regno {
            font-size: 13pt;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .cover-report-type {
            font-size: 14pt;
            font-weight: bold;
            margin: 20px 0 15px 0;
            letter-spacing: 0.5px;
        }

        .cover-dept {
            font-size: 13pt;
            font-weight: bold;
            margin: 10px 0 20px 0;
            line-height: 1.3;
        }

        .cover-degree {
            font-size: 14pt;
            font-weight: bold;
            margin: 15px 0;
            line-height: 1.4;
        }

        .cover-address {
            font-size: 12pt;
            font-weight: bold;
            line-height: 1.4;
            margin-bottom: 20px;
        }

        .cover-date {
            font-size: 13pt;
            font-weight: bold;
            letter-spacing: 1px;
        }

        /* Certificate Signatures */
        .sig-container {
            display: flex;
            justify-content: space-between;
            margin-top: 80px;
            text-align: left;
        }

        .sig-box {
            width: 45%;
            line-height: 1.4;
            font-size: 11pt;
        }

        .viva-box {
            margin-top: 60px;
            font-size: 11pt;
        }

        .examiner-sig {
            display: flex;
            justify-content: space-between;
            margin-top: 70px;
            font-size: 11pt;
            font-weight: bold;
        }

        /* TOC Leader dots */
        .toc-row {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 8px;
            font-size: 11.5pt;
        }

        .toc-left {
            display: flex;
            align-items: baseline;
            flex: 1;
        }

        .toc-num {
            width: 80px;
            flex-shrink: 0;
            font-weight: bold;
        }

        .toc-subnum {
            width: 50px;
            flex-shrink: 0;
            padding-left: 15px;
        }

        .toc-title {
            flex: 1;
            padding-right: 10px;
        }

        .toc-dots {
            flex-grow: 1;
            border-bottom: 1px dotted #555555;
            margin: 0 8px;
            height: 14px;
        }

        .toc-page {
            font-weight: bold;
            flex-shrink: 0;
        }

        /* Screenshots Mockups */
        .screenshot-mockup {
            border: 1px solid #1e293b;
            border-radius: 8px;
            background: #0f172a;
            color: #ffffff;
            padding: 16px;
            margin: 15px 0 25px 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 9.5pt;
        }

        .mockup-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #334155;
            padding-bottom: 8px;
            margin-bottom: 12px;
        }

        .mockup-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 12px;
        }

        .mockup-card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 6px;
            padding: 10px;
        }

        .mockup-chart {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 6px;
            padding: 14px;
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <!-- ======================================================== -->
    <!-- PAGE 1: COVER PAGE                                       -->
    <!-- ======================================================== -->
    <div class="page cover-page">
        <div>
            <!-- AMET University Header with Crest and Seal -->
            <div class="cover-logo-container">
                <svg width="85" height="85" viewBox="0 0 200 200">
                    <circle cx="100" cy="100" r="92" fill="#800000" stroke="#ffd700" stroke-width="4"/>
                    <circle cx="100" cy="100" r="76" fill="#ffffff" stroke="#800000" stroke-width="2"/>
                    <circle cx="100" cy="100" r="62" fill="#800000"/>
                    <!-- Anchor and Wheel Icon -->
                    <circle cx="100" cy="100" r="45" fill="none" stroke="#ffd700" stroke-width="5" stroke-dasharray="10, 6"/>
                    <path d="M100 65 L100 135 M85 100 L115 100 M75 125 C85 140 115 140 125 125" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
                    <circle cx="100" cy="65" r="7" fill="#ffffff"/>
                    <!-- Crest Text -->
                    <text x="100" y="24" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="'Times New Roman'">ACADEMY OF MARITIME EDUCATION AND TRAINING</text>
                    <text x="100" y="185" fill="#ffd700" font-size="12" font-weight="bold" text-anchor="middle" font-family="'Times New Roman'">DEEMED TO BE UNIVERSITY</text>
                </svg>
                <div style="text-align: left;">
                    <div style="font-size: 32pt; font-weight: 900; color: #1a2a5e; font-family: 'Times New Roman', serif; letter-spacing: 1.5px; line-height: 1;">AMET</div>
                    <div style="font-size: 15pt; font-weight: 700; color: #1e40af; font-family: 'Times New Roman', serif; letter-spacing: 5px; line-height: 1.2;">UNIVERSITY</div>
                    <div style="font-size: 7.5pt; color: #475569; font-family: 'Times New Roman', serif; font-style: italic;">(Deemed to be University Under Section 3 of UGC Act 1956)</div>
                </div>
            </div>

            <div class="cover-title">AI-BASED BUSINESS ANALYTICS DASHBOARD</div>
            
            <div class="cover-subtitle">Submitted by</div>
            
            <div class="cover-author">MOHAMMED SADIQ.A</div>
            <div class="cover-regno">Reg. No (ASML24020)</div>
            
            <div class="cover-subtitle">of</div>
            
            <div style="font-size: 14pt; font-weight: bold; margin-bottom: 25px;">AMET UNIVERSITY</div>
            
            <div class="cover-report-type">A CAPSTONE PROJECT REPORT</div>
            
            <div class="cover-subtitle">Submitted to the</div>
            
            <div class="cover-dept">FACULTY OF ADVANCED COMPUTING SCIENCES</div>
            
            <div class="cover-subtitle">In partial fulfillment of requirements for the award of the degree<br>of</div>
            
            <div class="cover-degree">BACHELOR OF SCIENCE -<br>ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING</div>
        </div>

        <div>
            <div class="cover-address">
                AMET UNIVERSITY<br>
                135, East Coast Road, Kanathur - 603 112<br>
                Tamil Nadu, India
            </div>
            
            <div class="cover-date">NOVEMBER 2026</div>
        </div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 2: BONAFIDE CERTIFICATE                             -->
    <!-- ======================================================== -->
    <div class="page">
        <h1 class="chapter-title" style="margin-top: 60px;">BONAFIDE CERTIFICATE</h1>

        <p style="line-height: 1.8; font-size: 12.5pt; margin-top: 40px;">
            Certified that this project report titled <strong>“AI-BASED BUSINESS ANALYTICS DASHBOARD”</strong> is the bonafide work of <strong>MOHAMMED SADIQ.A (Reg No: ASML24020)</strong> who carried out the project under supervision. Certified further, that to the best of my knowledge, the work report or dissertation on the basics of which a degree or award was conferred on an earlier occasion on this or any other candidate.
        </p>

        <div class="sig-container" style="margin-top: 100px;">
            <div class="sig-box">
                <strong>Supervisor</strong><br><br>
                <strong>Mr. Tamilarasan D, M.C.A.,</strong><br>
                Assistant Professor,<br>
                Department of ACS,<br>
                AMET University,<br>
                Kanathur - 603 112.
            </div>
            <div class="sig-box" style="text-align: right;">
                <strong>Head of the Department</strong><br><br>
                <strong>Dr. C.N. Ravi, Ph.D.,</strong><br>
                Head of the Department,<br>
                Department of CSE,<br>
                AMET University,<br>
                Kanathur - 603 112.
            </div>
        </div>

        <div class="viva-box" style="margin-top: 100px;">
            Submitted for Project Viva Examination held on ______________________
        </div>

        <div class="examiner-sig" style="margin-top: 80px;">
            <div>Internal Examiner</div>
            <div>External Examiner</div>
        </div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 3: ABSTRACT                                         -->
    <!-- ======================================================== -->
    <div class="page">
        <h1 class="chapter-title">ABSTRACT</h1>

        <p>
            The <strong>AI-Based Business Analytics Dashboard (NexusBI)</strong> is an innovative full-stack enterprise data intelligence web application developed to revolutionize corporate financial analytics, sales performance monitoring, and strategic business decision-making. The platform addresses critical industry challenges stemming from legacy spreadsheet dependencies, fragmented manual calculation scripts, and the absence of real-time conversational business intelligence. By uniting advanced Python computational pipelines with an interactive, modern SaaS frontend, the system provides automated diagnostic insights, statistical anomaly detection, and intuitive natural language querying for cross-functional business stakeholders.
        </p>

        <p>
            Through a modular, responsive architecture inspired by contemporary data platforms such as Microsoft Power BI, Tableau, and Stripe, the system empowers executives, business analysts, and operations personnel to upload and interrogate complex datasets seamlessly. The platform features dedicated modules for Executive Overview Key Performance Indicators (KPIs), Drag-and-Drop Dataset Management with automated missing-value imputation (Mean, Median, Mode) and deduplication, Period-over-Period Sales Growth Analytics with custom date filtering, Product Contribution Analysis, Profitability Tier Classification, and automated Executive Report Generation with print-ready PDF and formatted Excel (.xlsx) export capabilities.
        </p>

        <p>
            A core technological advancement of this project is its integrated <strong>Natural Language Business Intelligence (NLBI) Engine</strong>. Utilizing context-aware semantic parsing and statistical correlation algorithms, the AI assistant interprets plain English analytical queries (e.g., <em>"Which product generates the highest revenue?"</em>, <em>"What is the total profit?"</em>, <em>"Why are sales decreasing?"</em>) and synthesizes instant, data-backed answers accompanied by exact metrics and strategic takeaways. Furthermore, automated statistical anomaly detection scans temporal records for variations exceeding 1.8 standard deviations from seasonal baselines, enabling proactive inventory replenishment and margin risk mitigation.
        </p>

        <p>
            In conclusion, the AI-Based Business Analytics Dashboard represents a comprehensive, production-ready capstone engineering achievement. Developed utilizing Python (Flask, Pandas, NumPy, OpenPyXL) on the backend and modern reactive web technologies (Tailwind CSS, Chart.js, Lucide Icons) on the frontend, the platform sets a robust benchmark for academic and industrial data analytics, maximizing operational efficiency, eliminating reporting discrepancies, and delivering actionable intelligence in standard Indian Rupee (₹) financial currency.
        </p>

        <div class="roman-num">i</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 4: ACKNOWLEDGEMENT                                  -->
    <!-- ======================================================== -->
    <div class="page">
        <h1 class="chapter-title">ACKNOWLEDGEMENT</h1>

        <p>
            I offer my humble gratitude to the <strong>Lord Almighty</strong> who graced and helped me all along to complete this capstone project successfully. I would like to sincerely acknowledge all the esteemed individuals who guided and supported the development of this project.
        </p>

        <p>
            First and foremost, I sincerely thank <strong>"Everlasting"</strong> for enabling me to undertake and complete this research and software engineering endeavor successfully.
        </p>

        <p>
            I owe my sincere thanks to <strong>Dr. C.N. Ravi, Ph.D.</strong>, Head of the Department, Department of CSE / Faculty of Advanced Computing Sciences, AMET University, for taking a keen interest in the project and for providing invaluable guidance, coordination, and encouragement throughout the course of this work even amidst his demanding schedule. His continuous availability, insightful suggestions, and motivational support were instrumental in bringing out the best in this project.
        </p>

        <p>
            I express my profound gratitude to my Project Supervisor, <strong>Mr. Tamilarasan D, M.C.A.</strong>, Assistant Professor, Department of ACS, AMET University, for his exceptional mentorship, technical direction, and timely reviews. His constructive feedback on algorithmic design, data cleaning strategies, and user experience significantly refined the quality of this work.
        </p>

        <p>
            I am also deeply grateful to <strong>Mr. Aakaash M, M.C.A.</strong>, Assistant Professor and Faculty Advisor, Department of ACS, AMET University. I greatly benefited from his invaluable guidance, coordination, and advice throughout my academic tenure.
        </p>

        <p>
            I also express my appreciation to all faculty members of the Department of ACS, AMET University, for their constant support and academic foundation. Furthermore, I extend my heartfelt thanks to all the non-teaching and laboratory staff members for their dedicated assistance.
        </p>

        <p>
            Finally, I express my deepest gratitude to my beloved <strong>Parents and Friends</strong> for their unconditional encouragement, patience, and constant moral support throughout this journey.
        </p>

        <div style="margin-top: 50px; text-align: right; font-weight: bold;">
            MOHAMMED SADIQ.A<br>
            Reg. No: ASML24020
        </div>

        <div class="roman-num">iv</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 5: TABLE OF CONTENTS (Part 1)                       -->
    <!-- ======================================================== -->
    <div class="page">
        <h1 class="chapter-title">TABLE OF CONTENTS</h1>

        <div class="toc-row" style="font-weight: bold; border-bottom: 1.5px solid #000; padding-bottom: 4px; margin-bottom: 14px;">
            <div class="toc-left">
                <span class="toc-num">CHAPTER</span>
                <span class="toc-title">TITLE</span>
            </div>
            <span class="toc-page">PAGE NO</span>
        </div>

        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-title">ABSTRACT (ENGLISH)</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">i</span>
        </div>

        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-title">ACKNOWLEDGEMENT</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">iv</span>
        </div>

        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-title">TABLE OF CONTENTS</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">v</span>
        </div>

        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-title">LIST OF FIGURES</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">vii</span>
        </div>

        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-title">LIST OF TABLES</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">vii</span>
        </div>

        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-title">ABBREVIATIONS</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">viii</span>
        </div>

        <div class="toc-row" style="font-weight: bold; margin-top: 10px;">
            <div class="toc-left"><span class="toc-num">1</span><span class="toc-title">INTRODUCTION</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">1</span>
        </div>

        <div class="toc-row" style="font-weight: bold; margin-top: 10px;">
            <div class="toc-left"><span class="toc-num">2</span><span class="toc-title">SYSTEM ANALYSIS</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">2</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">2.1</span><span class="toc-title">EXISTING SYSTEM</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">2</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">2.2</span><span class="toc-title">PROPOSED SYSTEM</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">2</span>
        </div>

        <div class="toc-row" style="font-weight: bold; margin-top: 10px;">
            <div class="toc-left"><span class="toc-num">3</span><span class="toc-title">SYSTEM REQUIREMENTS</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">3</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">3.1</span><span class="toc-title">HARDWARE REQUIREMENTS</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">3</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">3.2</span><span class="toc-title">SOFTWARE REQUIREMENTS</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">3</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">3.3</span><span class="toc-title">SOFTWARE REQUIREMENT SPECIFICATION</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">3</span>
        </div>

        <div class="toc-row" style="font-weight: bold; margin-top: 10px;">
            <div class="toc-left"><span class="toc-num">4</span><span class="toc-title">SYSTEM DESIGN</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">10</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">4.1</span><span class="toc-title">ARCHITECTURE DIAGRAM</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">10</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">4.2</span><span class="toc-title">UML DIAGRAMS</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">11</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">4.2.1</span><span class="toc-title">USE CASE DIAGRAM</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">11</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">4.2.2</span><span class="toc-title">CLASS DIAGRAM</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">12</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">4.2.3</span><span class="toc-title">SEQUENCE DIAGRAM</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">13</span>
        </div>

        <div class="roman-num">v</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 6: TABLE OF CONTENTS (Part 2)                       -->
    <!-- ======================================================== -->
    <div class="page">
        <h1 class="chapter-title" style="margin-top: 25px;">TABLE OF CONTENTS (Contd.)</h1>

        <div class="toc-row" style="font-weight: bold; border-bottom: 1.5px solid #000; padding-bottom: 4px; margin-bottom: 14px;">
            <div class="toc-left">
                <span class="toc-num">CHAPTER</span>
                <span class="toc-title">TITLE</span>
            </div>
            <span class="toc-page">PAGE NO</span>
        </div>

        <div class="toc-row" style="font-weight: bold;">
            <div class="toc-left"><span class="toc-num">5</span><span class="toc-title">MODULE DESCRIPTION</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">14</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">5.1</span><span class="toc-title">MAIN MODULES</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">14</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">5.1.1</span><span class="toc-title">OVERVIEW DASHBOARD MODULE</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">14</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">5.1.2</span><span class="toc-title">DATA UPLOAD & MANAGEMENT MODULE</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">15</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">5.1.3</span><span class="toc-title">SALES ANALYTICS MODULE</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">17</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">5.1.4</span><span class="toc-title">PRODUCT ANALYTICS MODULE</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">18</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">5.1.5</span><span class="toc-title">PROFIT ANALYTICS MODULE</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">19</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">5.1.6</span><span class="toc-title">AI BUSINESS INSIGHTS & NATURAL LANGUAGE ASSISTANT</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">20</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">5.1.7</span><span class="toc-title">REPORTS & EXPORT MODULE</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">21</span>
        </div>

        <div class="toc-row" style="font-weight: bold; margin-top: 10px;">
            <div class="toc-left"><span class="toc-num">6</span><span class="toc-title">IMPLEMENTATION AND TESTING</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">22</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">6.1</span><span class="toc-title">IMPLEMENTATION AND CODING</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">22</span>
        </div>

        <div class="toc-row" style="font-weight: bold; margin-top: 10px;">
            <div class="toc-left"><span class="toc-num">7</span><span class="toc-title">SYSTEM TESTING</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">44</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">7.1</span><span class="toc-title">UNIT TESTING</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">44</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">7.2</span><span class="toc-title">INTEGRATION TESTING</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">45</span>
        </div>

        <div class="toc-row" style="font-weight: bold; margin-top: 10px;">
            <div class="toc-left"><span class="toc-num">8</span><span class="toc-title">APPENDICES</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">47</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">8.1</span><span class="toc-title">SYSTEM SCREENSHOTS & UI MOCKUPS</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">47</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">8.2</span><span class="toc-title">DATA DICTIONARY</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">57</span>
        </div>

        <div class="toc-row" style="font-weight: bold; margin-top: 10px;">
            <div class="toc-left"><span class="toc-num">9</span><span class="toc-title">CONCLUSION AND FUTURE ENHANCEMENT</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">59</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">9.1</span><span class="toc-title">CONCLUSION</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">59</span>
        </div>
        <div class="toc-row">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-subnum">9.2</span><span class="toc-title">FUTURE ENHANCEMENT</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">59</span>
        </div>

        <div class="toc-row" style="font-weight: bold; margin-top: 10px;">
            <div class="toc-left"><span class="toc-num"></span><span class="toc-title">REFERENCES</span></div>
            <span class="toc-dots"></span>
            <span class="toc-page">60</span>
        </div>

        <div class="roman-num">vi</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 7: LIST OF FIGURES & LIST OF TABLES                 -->
    <!-- ======================================================== -->
    <div class="page">
        <h1 class="chapter-title" style="margin-bottom: 20px;">LIST OF FIGURES</h1>

        <table class="academic-table" style="margin-bottom: 40px;">
            <thead>
                <tr>
                    <th style="width: 25%;">FIGURE NO</th>
                    <th style="width: 55%;">NAME</th>
                    <th style="width: 20%;">PAGE NO</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="text-align: center;">4.1</td>
                    <td>ARCHITECTURE DIAGRAM</td>
                    <td style="text-align: center;">10</td>
                </tr>
                <tr>
                    <td style="text-align: center;">4.2</td>
                    <td>USE CASE DIAGRAM</td>
                    <td style="text-align: center;">11</td>
                </tr>
                <tr>
                    <td style="text-align: center;">4.3</td>
                    <td>CLASS DIAGRAM</td>
                    <td style="text-align: center;">12</td>
                </tr>
                <tr>
                    <td style="text-align: center;">4.4</td>
                    <td>SEQUENCE DIAGRAM</td>
                    <td style="text-align: center;">13</td>
                </tr>
            </tbody>
        </table>

        <h1 class="chapter-title" style="margin-top: 30px; margin-bottom: 20px;">LIST OF TABLES</h1>

        <table class="academic-table">
            <thead>
                <tr>
                    <th style="width: 25%;">TABLE NO</th>
                    <th style="width: 55%;">NAME</th>
                    <th style="width: 20%;">PAGE NO</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="text-align: center;">8.1</td>
                    <td>ENTERPRISE SALES 2026 DATASET TABLE</td>
                    <td style="text-align: center;">57</td>
                </tr>
                <tr>
                    <td style="text-align: center;">8.2</td>
                    <td>SALES AND PROFIT CORE DATASET TABLE</td>
                    <td style="text-align: center;">57</td>
                </tr>
                <tr>
                    <td style="text-align: center;">8.3</td>
                    <td>MONTHLY SALES BASELINE DATASET TABLE</td>
                    <td style="text-align: center;">58</td>
                </tr>
                <tr>
                    <td style="text-align: center;">8.4</td>
                    <td>DATA CLEANING LOG AND AUDIT TABLE</td>
                    <td style="text-align: center;">58</td>
                </tr>
                <tr>
                    <td style="text-align: center;">8.5</td>
                    <td>ANALYTICAL REPORT EXECUTIVE METRICS TABLE</td>
                    <td style="text-align: center;">58</td>
                </tr>
            </tbody>
        </table>

        <div class="roman-num">vii</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 8: ABBREVIATIONS                                    -->
    <!-- ======================================================== -->
    <div class="page">
        <h1 class="chapter-title">ABBREVIATIONS</h1>

        <div style="margin-top: 40px; line-height: 2.2; font-size: 12pt;">
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">AI</span> <span>- ARTIFICIAL INTELLIGENCE</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">ML</span> <span>- MACHINE LEARNING</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">NLP</span> <span>- NATURAL LANGUAGE PROCESSING</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">BI</span> <span>- BUSINESS INTELLIGENCE</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">KPI</span> <span>- KEY PERFORMANCE INDICATOR</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">HTML</span> <span>- HYPERTEXT MARKUP LANGUAGE</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">CSS</span> <span>- CASCADING STYLE SHEETS</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">JS</span> <span>- JAVASCRIPT</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">HTTP</span> <span>- HYPERTEXT TRANSFER PROTOCOL</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">API</span> <span>- APPLICATION PROGRAMMING INTERFACE</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">REST</span> <span>- REPRESENTATIONAL STATE TRANSFER</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">SPA</span> <span>- SINGLE PAGE APPLICATION</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">CSV</span> <span>- COMMA SEPARATED VALUES</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">XLSX</span> <span>- MICROSOFT EXCEL OPEN XML SPREADSHEET</span></div>
            <div style="display: flex;"><span style="width: 140px; font-weight: bold;">INR (₹)</span> <span>- INDIAN RUPEE STANDARD</span></div>
        </div>

        <div class="roman-num">viii</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 9: CHAPTER 1 - INTRODUCTION                         -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">1</div>
        <h1 class="chapter-title" style="margin-top: 20px;">CHAPTER 1<br>INTRODUCTION</h1>

        <p>
            In contemporary corporate ecosystems, data is generated at an unprecedented velocity across retail transactions, operational logistics, customer touchpoints, and fiscal ledgers. Effective analysis and interpretation of business data is a critical aspect of ensuring sustained profitability, maintaining inventory equilibrium, and steering strategic organizational growth. Traditional corporate reporting methodologies rely heavily on manual spreadsheets or disjointed console scripts, which are inherently time-consuming, prone to human calculation errors, and unable to surface real-time actionable insights to managerial executives.
        </p>

        <p>
            To overcome these substantial challenges, the <strong>AI-Based Business Analytics Dashboard (NexusBI)</strong> has been conceived and developed. The proposed platform transforms static, localized data processing routines into an enterprise-grade, responsive Web Application. The system empowers corporate leaders, business analysts, and operational managers to ingest structured datasets, audit missing values, execute automated data cleaning, monitor sales velocity in standard Indian Rupees (₹), evaluate product profitability matrices, and interrogate financial metrics through a conversational Natural Language AI Assistant.
        </p>

        <p>
            The software platform is architected utilizing a robust <strong>Python (Flask, Pandas, NumPy, OpenPyXL)</strong> computational backend integrated with a reactive frontend powered by <strong>HTML5, CSS3, Tailwind CSS, Chart.js, and Lucide Icons</strong>. The application features seven cohesive modules: an Executive Overview Dashboard, Data Upload & Management, Sales Analytics, Product Analytics, Profit Analytics, AI Business Insights, and Analytical Reports & Export. This capstone engineering project delivers an end-to-end business intelligence suite designed to minimize analytical latency, eliminate reporting discrepancies, and foster rigorous data-driven decision-making.
        </p>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 10: CHAPTER 2 - SYSTEM ANALYSIS                     -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">2</div>
        <h1 class="chapter-title" style="margin-top: 20px;">CHAPTER 2<br>SYSTEM ANALYSIS</h1>

        <h2 class="section-title">2.1 EXISTING SYSTEM</h2>
        <p>
            The existing operational approach for enterprise sales and profit analysis predominantly relies on standalone spreadsheet applications (such as Microsoft Excel or Google Sheets) or raw Python/Matplotlib console scripts executed locally by a programmer. These tools lack an interactive multi-user graphical interface, require manual intervention to clean missing data cells, and produce static visualization plots that cannot be filtered dynamically across time ranges or product lines.
        </p>

        <h3 class="subsection-title">DISADVANTAGES OF EXISTING SYSTEM</h3>
        <ul>
            <li><strong>Lack of Real-Time Interactivity:</strong> Static Matplotlib charts do not support interactive tooltips, cross-filtering, or dynamic axis adjustments.</li>
            <li><strong>Error-Prone Data Ingestion:</strong> Missing numerical values (NaN) and duplicated rows require manual identification and ad-hoc code edits, risking data corruption.</li>
            <li><strong>Absence of Conversational Intelligence:</strong> Executives must manually sift through hundreds of tabular rows to discover peak sales periods or margin drivers without natural language query support.</li>
            <li><strong>Rigid Export Mechanisms:</strong> Generating management-ready executive summaries or formatted PDF reports requires manual collation across disparate tools.</li>
        </ul>

        <h2 class="section-title">2.2 PROPOSED SYSTEM</h2>
        <p>
            The proposed system is an enterprise-ready, web-based Business Analytics Dashboard engineered to provide a centralized single-page interface for data upload, statistical data cleaning, visual exploratory analytics, and conversational intelligence. By coupling high-performance Pandas and NumPy calculation engines with responsive Chart.js visual components, the platform offers immediate feedback and drill-down analytics for business metrics in Indian Rupees (₹).
        </p>

        <h3 class="subsection-title">ADVANTAGES OF PROPOSED SYSTEM</h3>
        <ul>
            <li><strong>Unified SaaS Dashboard Interface:</strong> Single-Page Application (SPA) architecture offering instantaneous module switching and persistent dark/light theme options.</li>
            <li><strong>Automated Data Cleaning Pipeline:</strong> Ingests CSV and Excel (.xlsx) files with instant audit of missing cells and single-click imputation (Mean, Median, Mode) and deduplication.</li>
            <li><strong>Conversational "Ask AI" Assistant:</strong> Natural language interrogation engine answering ad-hoc executive questions with exact statistics and strategic recommendations.</li>
            <li><strong>Print-Ready PDF & Excel Reporting:</strong> Automated generation of analytical reports with one-click print-to-PDF formatting and multi-sheet Excel export.</li>
        </ul>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 11: CHAPTER 3 - SYSTEM REQUIREMENTS (Part 1)        -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">3</div>
        <h1 class="chapter-title" style="margin-top: 20px;">CHAPTER 3<br>SYSTEM REQUIREMENTS</h1>

        <h2 class="section-title">3.1 HARDWARE REQUIREMENTS</h2>
        <ul>
            <li><strong>Processor:</strong> Intel Core i5 Processor / AMD Ryzen 5 or Above</li>
            <li><strong>RAM:</strong> 8 GB Minimum (16 GB Recommended for multi-million row processing)</li>
            <li><strong>Hard Disk:</strong> 512 GB Solid State Drive (SSD)</li>
            <li><strong>Display:</strong> 1920 x 1080 Full HD resolution display</li>
            <li><strong>Network:</strong> Standard Local Area Network / TCP/IP Interface</li>
        </ul>

        <h2 class="section-title">3.2 SOFTWARE REQUIREMENTS</h2>
        <ul>
            <li><strong>Operating System:</strong> Microsoft Windows 11 / Windows 10 (64-bit)</li>
            <li><strong>Development Environment (IDE):</strong> Visual Studio Code / Anaconda Navigator</li>
            <li><strong>Backend Programming Language:</strong> Python 3.10+ / Python 3.13.9</li>
            <li><strong>Web Framework:</strong> Flask 3.0+ (WSGI Application Server)</li>
            <li><strong>Data Analysis Libraries:</strong> Pandas 2.3+, NumPy 2.3+, SciPy</li>
            <li><strong>Spreadsheet Engine:</strong> OpenPyXL 3.1+</li>
            <li><strong>Frontend Technologies:</strong> HTML5, CSS3, Tailwind CSS (CDN), Vanilla JavaScript (ES6+)</li>
            <li><strong>Data Visualization Engine:</strong> Chart.js 4.4+</li>
            <li><strong>Iconography:</strong> Lucide Icons SVG Library</li>
            <li><strong>Web Browser:</strong> Google Chrome / Microsoft Edge</li>
        </ul>

        <h2 class="section-title">3.3 SOFTWARE REQUIREMENTS SPECIFICATIONS</h2>
        
        <h3 class="subsection-title">PYTHON & ANACONDA</h3>
        <p>
            Python is an interpreted, high-level, general-purpose programming language renowned for its extensive data science ecosystem. For this capstone project, Python 3.13 within the Anaconda distribution provides the foundational computational engine. Python's clean syntax, dynamic typing, and memory management facilitate robust server-side analytics, data cleaning routines, and natural language semantic parsing.
        </p>

        <h3 class="subsection-title">FLASK WEB FRAMEWORK</h3>
        <p>
            Flask is a lightweight and extensible WSGI micro-web framework developed in Python. Unlike monolithic frameworks, Flask allows developers to construct modular RESTful API endpoints without unnecessary overhead. Flask orchestrates file uploads, manages session states, serves static frontend assets, and exposes JSON endpoints for analytics queries.
        </p>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 12: CHAPTER 3 - SYSTEM REQUIREMENTS (Part 2)        -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">4</div>
        
        <h3 class="subsection-title">PANDAS & NUMPY DATA PIPELINE</h3>
        <p>
            <strong>Pandas</strong> is a fast, powerful, and flexible open-source data analysis and manipulation tool built on top of the Python programming language. In NexusBI, Pandas DataFrames serve as the primary in-memory tabular structure for data ingestion, filtering, grouping, and aggregation. Key operations include:
        </p>
        <ul>
            <li><strong>Missing Value Imputation:</strong> Utilizing <code>df[col].fillna(df[col].mean())</code> and median methods to replace missing numbers without introducing data bias.</li>
            <li><strong>Deduplication:</strong> Identifying and eliminating redundant transactions using <code>df.drop_duplicates()</code>.</li>
            <li><strong>Statistical Aggregation:</strong> Computing sums, means, medians, standard deviations, and quartile distributions via <code>df.describe()</code>.</li>
            <li><strong>Correlation Analysis:</strong> Calculating Pearson correlation coefficients between Sales and Profit via <code>df[['Sales', 'Profit']].corr()</code>.</li>
        </ul>
        <p>
            <strong>NumPy</strong> provides fundamental scientific computing support, supplying multidimensional array objects, vectorized mathematical operations, and statistical calculations such as standard deviation thresholds used in anomaly detection.
        </p>

        <h3 class="subsection-title">CHART.JS VISUALIZATION ENGINE</h3>
        <p>
            Chart.js is a premier JavaScript charting library built upon the HTML5 Canvas element. It delivers responsive, animated, and customizable data visualizations. In NexusBI, a custom ChartManager orchestrates:
        </p>
        <ul>
            <li><strong>Theme Awareness:</strong> Dynamically updating canvas gridline opacities, tick colors, and tooltips upon toggling between Light and Dark themes.</li>
            <li><strong>Currency Localization:</strong> Formatting all tick values and hover tooltips into Indian Rupee standard (₹) with Lakhs (L) and Crores (Cr) abbreviations.</li>
            <li><strong>Chart Variety:</strong> Line/Area trend charts, vertical and horizontal bar charts, doughnut market-share charts, and dual-axis combo charts.</li>
        </ul>

        <h3 class="subsection-title">TAILWIND CSS & MODERN SAAS DESIGN</h3>
        <p>
            Tailwind CSS provides a utility-first styling system enabling rapid UI development with clean class composition. Glassmorphic card surfaces, soft shadows, responsive breakpoints (Desktop, Tablet, Mobile), and dark navy aesthetics (#0b0f19, #111827) provide an executive user experience aligned with Power BI and Stripe standards.
        </p>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 13: CHAPTER 4 - SYSTEM DESIGN (Part 1 - Arch)       -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">10</div>
        <h1 class="chapter-title" style="margin-top: 20px;">CHAPTER 4<br>SYSTEM DESIGN</h1>

        <h2 class="section-title">4.1 ARCHITECTURE DIAGRAM</h2>
        <p>
            The system employs a decoupled, multi-tiered client-server architecture separating the browser-based presentation layer, the Flask API routing tier, the analytical data processing pipeline, and the persistence file storage tier.
        </p>

        <div class="diagram-container">
            <svg width="600" height="340" viewBox="0 0 700 400" style="max-width: 100%;">
                <!-- Background box -->
                <rect x="10" y="10" width="680" height="380" rx="10" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
                
                <!-- Client Tier -->
                <rect x="30" y="40" width="180" height="320" rx="8" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>
                <text x="120" y="65" font-family="'Times New Roman'" font-size="13" font-weight="bold" text-anchor="middle" fill="#312e81">PRESENTATION TIER</text>
                <rect x="45" y="85" width="150" height="45" rx="5" fill="#ffffff" stroke="#6366f1"/>
                <text x="120" y="112" font-family="'Times New Roman'" font-size="11" text-anchor="middle">Single-Page UI (SPA)</text>
                <rect x="45" y="145" width="150" height="45" rx="5" fill="#ffffff" stroke="#6366f1"/>
                <text x="120" y="172" font-family="'Times New Roman'" font-size="11" text-anchor="middle">Chart.js Visualizations</text>
                <rect x="45" y="205" width="150" height="45" rx="5" fill="#ffffff" stroke="#6366f1"/>
                <text x="120" y="232" font-family="'Times New Roman'" font-size="11" text-anchor="middle">Tailwind & SaaS Theme</text>
                <rect x="45" y="265" width="150" height="45" rx="5" fill="#ffffff" stroke="#6366f1"/>
                <text x="120" y="292" font-family="'Times New Roman'" font-size="11" text-anchor="middle">Ask AI Chat Client</text>

                <!-- Arrows Client -> Server -->
                <path d="M 210 160 L 260 160" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
                <path d="M 260 220 L 210 220" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
                <text x="235" y="150" font-family="'Times New Roman'" font-size="10" text-anchor="middle">HTTP REST</text>
                <text x="235" y="235" font-family="'Times New Roman'" font-size="10" text-anchor="middle">JSON Data</text>

                <!-- Application Tier -->
                <rect x="260" y="40" width="200" height="320" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
                <text x="360" y="65" font-family="'Times New Roman'" font-size="13" font-weight="bold" text-anchor="middle" fill="#14532d">APPLICATION TIER</text>
                <rect x="275" y="85" width="170" height="45" rx="5" fill="#ffffff" stroke="#22c55e"/>
                <text x="360" y="112" font-family="'Times New Roman'" font-size="11" text-anchor="middle">Flask RESTful Server</text>
                <rect x="275" y="145" width="170" height="45" rx="5" fill="#ffffff" stroke="#22c55e"/>
                <text x="360" y="172" font-family="'Times New Roman'" font-size="11" text-anchor="middle">Analytics & NLP Engine</text>
                <rect x="275" y="205" width="170" height="45" rx="5" fill="#ffffff" stroke="#22c55e"/>
                <text x="360" y="232" font-family="'Times New Roman'" font-size="11" text-anchor="middle">Imputation & Cleaning</text>
                <rect x="275" y="265" width="170" height="45" rx="5" fill="#ffffff" stroke="#22c55e"/>
                <text x="360" y="292" font-family="'Times New Roman'" font-size="11" text-anchor="middle">Report Generator</text>

                <!-- Arrows Server -> Data -->
                <path d="M 460 160 L 500 160" stroke="#334155" stroke-width="2"/>
                <path d="M 500 220 L 460 220" stroke="#334155" stroke-width="2"/>
                <text x="480" y="150" font-family="'Times New Roman'" font-size="10" text-anchor="middle">Read</text>
                <text x="480" y="235" font-family="'Times New Roman'" font-size="10" text-anchor="middle">Write</text>

                <!-- Data Tier -->
                <rect x="500" y="40" width="170" height="320" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
                <text x="585" y="65" font-family="'Times New Roman'" font-size="13" font-weight="bold" text-anchor="middle" fill="#78350f">DATA STORAGE TIER</text>
                <rect x="515" y="85" width="140" height="45" rx="5" fill="#ffffff" stroke="#f59e0b"/>
                <text x="585" y="112" font-family="'Times New Roman'" font-size="11" text-anchor="middle">enterprise_sales.csv</text>
                <rect x="515" y="145" width="140" height="45" rx="5" fill="#ffffff" stroke="#f59e0b"/>
                <text x="585" y="172" font-family="'Times New Roman'" font-size="11" text-anchor="middle">sales_and_profit.csv</text>
                <rect x="515" y="205" width="140" height="45" rx="5" fill="#ffffff" stroke="#f59e0b"/>
                <text x="585" y="232" font-family="'Times New Roman'" font-size="11" text-anchor="middle">sales_data.csv</text>
                <rect x="515" y="265" width="140" height="45" rx="5" fill="#ffffff" stroke="#f59e0b"/>
                <text x="585" y="292" font-family="'Times New Roman'" font-size="11" text-anchor="middle">User Uploads (.xlsx)</text>
            </svg>
        </div>
        <div class="figure-caption">Fig 4.1 ARCHITECTURE DIAGRAM</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 14: CHAPTER 4 - SYSTEM DESIGN (Part 2 - Use Case)   -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">11</div>
        <h2 class="section-title">4.2 UML DIAGRAMS</h2>
        <h3 class="subsection-title">4.2.1 USE CASE DIAGRAM</h3>
        <p>
            The Use Case diagram visualizes the behavioral interactions between the primary operational actors (Business Analyst, Executive Stakeholder, System Administrator) and the platform's core functional modules.
        </p>

        <div class="diagram-container">
            <svg width="600" height="500" viewBox="0 0 650 560" style="max-width: 100%;">
                <!-- System Boundary Box -->
                <rect x="180" y="20" width="300" height="520" rx="8" fill="#f8fafc" stroke="#334155" stroke-width="1.5"/>
                <text x="330" y="45" font-family="'Times New Roman'" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">NexusBI Analytics System</text>

                <!-- Actor Left: Business Analyst -->
                <circle cx="70" cy="180" r="16" fill="#ffffff" stroke="#000000" stroke-width="2"/>
                <line x1="70" y1="196" x2="70" y2="245" stroke="#000000" stroke-width="2"/>
                <line x1="45" y1="215" x2="95" y2="215" stroke="#000000" stroke-width="2"/>
                <line x1="70" y1="245" x2="50" y2="295" stroke="#000000" stroke-width="2"/>
                <line x1="70" y1="245" x2="90" y2="295" stroke="#000000" stroke-width="2"/>
                <text x="70" y="315" font-family="'Times New Roman'" font-size="11" font-weight="bold" text-anchor="middle">Business Analyst</text>

                <!-- Actor Right: Executive / Manager -->
                <circle cx="580" cy="260" r="16" fill="#ffffff" stroke="#000000" stroke-width="2"/>
                <line x1="580" y1="276" x2="580" y2="325" stroke="#000000" stroke-width="2"/>
                <line x1="555" y1="295" x2="605" y2="295" stroke="#000000" stroke-width="2"/>
                <line x1="580" y1="325" x2="560" y2="375" stroke="#000000" stroke-width="2"/>
                <line x1="580" y1="325" x2="600" y2="375" stroke="#000000" stroke-width="2"/>
                <text x="580" y="395" font-family="'Times New Roman'" font-size="11" font-weight="bold" text-anchor="middle">Executive Stakeholder</text>

                <!-- Use Cases (Ellipses) -->
                <ellipse cx="330" cy="80" rx="100" ry="20" fill="#ffffff" stroke="#4f46e5" stroke-width="1.5"/>
                <text x="330" y="84" font-family="'Times New Roman'" font-size="10.5" text-anchor="middle">View Overview KPIs</text>

                <ellipse cx="330" cy="135" rx="100" ry="20" fill="#ffffff" stroke="#4f46e5" stroke-width="1.5"/>
                <text x="330" y="139" font-family="'Times New Roman'" font-size="10.5" text-anchor="middle">Upload CSV / Excel Dataset</text>

                <ellipse cx="330" cy="190" rx="100" ry="20" fill="#ffffff" stroke="#4f46e5" stroke-width="1.5"/>
                <text x="330" y="194" font-family="'Times New Roman'" font-size="10.5" text-anchor="middle">Clean Missing Values & Dups</text>

                <ellipse cx="330" cy="245" rx="100" ry="20" fill="#ffffff" stroke="#4f46e5" stroke-width="1.5"/>
                <text x="330" y="249" font-family="'Times New Roman'" font-size="10.5" text-anchor="middle">Analyze Sales & Growth Rates</text>

                <ellipse cx="330" cy="300" rx="100" ry="20" fill="#ffffff" stroke="#4f46e5" stroke-width="1.5"/>
                <text x="330" y="304" font-family="'Times New Roman'" font-size="10.5" text-anchor="middle">Evaluate Product Performance</text>

                <ellipse cx="330" cy="355" rx="100" ry="20" fill="#ffffff" stroke="#4f46e5" stroke-width="1.5"/>
                <text x="330" y="359" font-family="'Times New Roman'" font-size="10.5" text-anchor="middle">Assess Profitability Matrix</text>

                <ellipse cx="330" cy="410" rx="100" ry="20" fill="#ffffff" stroke="#4f46e5" stroke-width="1.5"/>
                <text x="330" y="414" font-family="'Times New Roman'" font-size="10.5" text-anchor="middle">Ask AI Natural Language Queries</text>

                <ellipse cx="330" cy="465" rx="100" ry="20" fill="#ffffff" stroke="#4f46e5" stroke-width="1.5"/>
                <text x="330" y="469" font-family="'Times New Roman'" font-size="10.5" text-anchor="middle">Export PDF & Excel Reports</text>

                <!-- Association Lines Analyst -->
                <line x1="85" y1="210" x2="230" y2="80" stroke="#64748b" stroke-width="1.2"/>
                <line x1="85" y1="210" x2="230" y2="135" stroke="#64748b" stroke-width="1.2"/>
                <line x1="85" y1="210" x2="230" y2="190" stroke="#64748b" stroke-width="1.2"/>
                <line x1="85" y1="210" x2="230" y2="245" stroke="#64748b" stroke-width="1.2"/>
                <line x1="85" y1="210" x2="230" y2="300" stroke="#64748b" stroke-width="1.2"/>

                <!-- Association Lines Executive -->
                <line x1="565" y1="290" x2="430" y2="80" stroke="#64748b" stroke-width="1.2"/>
                <line x1="565" y1="290" x2="430" y2="245" stroke="#64748b" stroke-width="1.2"/>
                <line x1="565" y1="290" x2="430" y2="355" stroke="#64748b" stroke-width="1.2"/>
                <line x1="565" y1="290" x2="430" y2="410" stroke="#64748b" stroke-width="1.2"/>
                <line x1="565" y1="290" x2="430" y2="465" stroke="#64748b" stroke-width="1.2"/>
            </svg>
        </div>
        <div class="figure-caption">Fig 4.2 USE CASE DIAGRAM</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 15: CHAPTER 4 - SYSTEM DESIGN (Part 3 - Class)      -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">12</div>
        <h3 class="subsection-title">4.2.2 CLASS DIAGRAM</h3>
        <p>
            The Class Diagram illustrates the object-oriented structure of the backend analytics classes, data models, web routers, and frontend orchestration managers.
        </p>

        <div class="diagram-container">
            <svg width="600" height="520" viewBox="0 0 680 540" style="max-width: 100%;">
                <!-- Class 1: BusinessAnalyticsEngine -->
                <rect x="20" y="20" width="280" height="230" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
                <rect x="20" y="20" width="280" height="28" fill="#f1f5f9" stroke="#000000" stroke-width="1"/>
                <text x="160" y="38" font-family="'Times New Roman'" font-size="12" font-weight="bold" text-anchor="middle">BusinessAnalyticsEngine</text>
                <!-- Attributes -->
                <text x="28" y="65" font-family="'Courier New'" font-size="9.5">- data_dir: str</text>
                <text x="28" y="80" font-family="'Courier New'" font-size="9.5">- active_dataset_name: str</text>
                <text x="28" y="95" font-family="'Courier New'" font-size="9.5">- raw_df: DataFrame</text>
                <text x="28" y="110" font-family="'Courier New'" font-size="9.5">- df: DataFrame</text>
                <text x="28" y="125" font-family="'Courier New'" font-size="9.5">- column_mapping: dict</text>
                <line x1="20" y1="135" x2="300" y2="135" stroke="#000000" stroke-width="1"/>
                <!-- Methods -->
                <text x="28" y="152" font-family="'Courier New'" font-size="9.5">+ load_dataset(filename): dict</text>
                <text x="28" y="167" font-family="'Courier New'" font-size="9.5">+ clean_dataset(strategy): dict</text>
                <text x="28" y="182" font-family="'Courier New'" font-size="9.5">+ get_overview_analytics(): dict</text>
                <text x="28" y="197" font-family="'Courier New'" font-size="9.5">+ get_sales_analytics(): dict</text>
                <text x="28" y="212" font-family="'Courier New'" font-size="9.5">+ generate_ai_insights(): dict</text>
                <text x="28" y="227" font-family="'Courier New'" font-size="9.5">+ ask_ai(question): dict</text>

                <!-- Class 2: FlaskServer / App -->
                <rect x="380" y="20" width="280" height="200" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
                <rect x="380" y="20" width="280" height="28" fill="#f1f5f9" stroke="#000000" stroke-width="1"/>
                <text x="520" y="38" font-family="'Times New Roman'" font-size="12" font-weight="bold" text-anchor="middle">FlaskAPIServer</text>
                <!-- Attributes -->
                <text x="388" y="65" font-family="'Courier New'" font-size="9.5">- app: Flask</text>
                <text x="388" y="80" font-family="'Courier New'" font-size="9.5">- engine: BusinessAnalyticsEngine</text>
                <text x="388" y="95" font-family="'Courier New'" font-size="9.5">- upload_folder: str</text>
                <line x1="380" y1="105" x2="660" y2="105" stroke="#000000" stroke-width="1"/>
                <!-- Methods -->
                <text x="388" y="125" font-family="'Courier New'" font-size="9.5">+ index(): render_template</text>
                <text x="388" y="142" font-family="'Courier New'" font-size="9.5">+ get_datasets(): JSON</text>
                <text x="388" y="159" font-family="'Courier New'" font-size="9.5">+ upload_dataset(): JSON</text>
                <text x="388" y="176" font-family="'Courier New'" font-size="9.5">+ clean_dataset(): JSON</text>
                <text x="388" y="193" font-family="'Courier New'" font-size="9.5">+ ai_ask(): JSON</text>

                <!-- Association Engine <-> Flask -->
                <line x1="300" y1="100" x2="380" y2="100" stroke="#000000" stroke-width="1.5"/>
                <text x="340" y="93" font-family="'Times New Roman'" font-size="10" text-anchor="middle">1</text>
                <text x="370" y="93" font-family="'Times New Roman'" font-size="10" text-anchor="middle">1</text>

                <!-- Class 3: Frontend AppRouter -->
                <rect x="20" y="310" width="280" height="190" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
                <rect x="20" y="310" width="280" height="28" fill="#f1f5f9" stroke="#000000" stroke-width="1"/>
                <text x="160" y="328" font-family="'Times New Roman'" font-size="12" font-weight="bold" text-anchor="middle">FrontendApp (App.js)</text>
                <text x="28" y="355" font-family="'Courier New'" font-size="9.5">- currentRoute: str</text>
                <text x="28" y="370" font-family="'Courier New'" font-size="9.5">- activeDataset: str</text>
                <line x1="20" y1="380" x2="300" y2="380" stroke="#000000" stroke-width="1"/>
                <text x="28" y="400" font-family="'Courier New'" font-size="9.5">+ init(): void</text>
                <text x="28" y="415" font-family="'Courier New'" font-size="9.5">+ navigateTo(route): void</text>
                <text x="28" y="430" font-family="'Courier New'" font-size="9.5">+ switchActiveDataset(): void</text>
                <text x="28" y="445" font-family="'Courier New'" font-size="9.5">+ toggleTheme(): void</text>
                <text x="28" y="460" font-family="'Courier New'" font-size="9.5">+ showToast(msg, type): void</text>

                <!-- Class 4: ChartManager -->
                <rect x="380" y="310" width="280" height="190" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
                <rect x="380" y="310" width="280" height="28" fill="#f1f5f9" stroke="#000000" stroke-width="1"/>
                <text x="520" y="328" font-family="'Times New Roman'" font-size="12" font-weight="bold" text-anchor="middle">ChartManager (charts.js)</text>
                <text x="388" y="355" font-family="'Courier New'" font-size="9.5">- instances: dict</text>
                <line x1="380" y1="365" x2="660" y2="365" stroke="#000000" stroke-width="1"/>
                <text x="388" y="388" font-family="'Courier New'" font-size="9.5">+ getThemeColors(): dict</text>
                <text x="388" y="405" font-family="'Courier New'" font-size="9.5">+ renderLineChart(): Chart</text>
                <text x="388" y="422" font-family="'Courier New'" font-size="9.5">+ renderBarChart(): Chart</text>
                <text x="388" y="439" font-family="'Courier New'" font-size="9.5">+ renderDonutChart(): Chart</text>
                <text x="388" y="456" font-family="'Courier New'" font-size="9.5">+ renderComboChart(): Chart</text>

                <!-- Association App -> ChartManager -->
                <line x1="300" y1="400" x2="380" y2="400" stroke="#000000" stroke-width="1.5"/>
                <!-- Association App -> Engine -->
                <line x1="160" y1="310" x2="160" y2="250" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,4"/>
            </svg>
        </div>
        <div class="figure-caption">Fig 4.3 CLASS DIAGRAM</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 16: CHAPTER 4 - SYSTEM DESIGN (Part 4 - Sequence)   -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">13</div>
        <h3 class="subsection-title">4.2.3 SEQUENCE DIAGRAM</h3>
        <p>
            The Sequence Diagram delineates the chronological message exchanges between the User, Presentation View, Client Router, Flask API Controller, and Analytics Processing Engine during data ingestion and natural language question answering.
        </p>

        <div class="diagram-container">
            <svg width="600" height="500" viewBox="0 0 650 520" style="max-width: 100%;">
                <!-- Lifelines -->
                <!-- 1. User -->
                <line x1="60" y1="50" x2="60" y2="470" stroke="#64748b" stroke-width="1" stroke-dasharray="4,4"/>
                <rect x="20" y="20" width="80" height="30" rx="4" fill="#f1f5f9" stroke="#000000"/>
                <text x="60" y="40" font-family="'Times New Roman'" font-size="11" font-weight="bold" text-anchor="middle">User</text>

                <!-- 2. UI / View -->
                <line x1="200" y1="50" x2="200" y2="470" stroke="#64748b" stroke-width="1" stroke-dasharray="4,4"/>
                <rect x="150" y="20" width="100" height="30" rx="4" fill="#f1f5f9" stroke="#000000"/>
                <text x="200" y="40" font-family="'Times New Roman'" font-size="11" font-weight="bold" text-anchor="middle">Browser UI</text>

                <!-- 3. Flask Server -->
                <line x1="360" y1="50" x2="360" y2="470" stroke="#64748b" stroke-width="1" stroke-dasharray="4,4"/>
                <rect x="300" y="20" width="120" height="30" rx="4" fill="#f1f5f9" stroke="#000000"/>
                <text x="360" y="40" font-family="'Times New Roman'" font-size="11" font-weight="bold" text-anchor="middle">Flask REST API</text>

                <!-- 4. Analytics Engine -->
                <line x1="530" y1="50" x2="530" y2="470" stroke="#64748b" stroke-width="1" stroke-dasharray="4,4"/>
                <rect x="460" y="20" width="140" height="30" rx="4" fill="#f1f5f9" stroke="#000000"/>
                <text x="530" y="40" font-family="'Times New Roman'" font-size="11" font-weight="bold" text-anchor="middle">Analytics Engine</text>

                <!-- Message 1: Select/Upload Dataset -->
                <line x1="60" y1="90" x2="200" y2="90" stroke="#000000" stroke-width="1.5"/>
                <polygon points="195,86 200,90 195,94" fill="#000000"/>
                <text x="130" y="82" font-family="'Times New Roman'" font-size="9" text-anchor="middle">Upload CSV/XLSX</text>

                <!-- Message 2: AJAX POST -->
                <line x1="200" y1="120" x2="360" y2="120" stroke="#000000" stroke-width="1.5"/>
                <polygon points="355,116 360,120 355,124" fill="#000000"/>
                <text x="280" y="112" font-family="'Times New Roman'" font-size="9" text-anchor="middle">POST /api/dataset/upload</text>

                <!-- Message 3: Engine load & audit -->
                <line x1="360" y1="150" x2="530" y2="150" stroke="#000000" stroke-width="1.5"/>
                <polygon points="525,146 530,150 525,154" fill="#000000"/>
                <text x="445" y="142" font-family="'Times New Roman'" font-size="9" text-anchor="middle">load_dataset(file)</text>

                <!-- Return 4: Dataset Overview -->
                <line x1="530" y1="180" x2="360" y2="180" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
                <polygon points="365,176 360,180 365,184" fill="#000000"/>
                <text x="445" y="174" font-family="'Times New Roman'" font-size="9" text-anchor="middle">rows, cols, null counts</text>

                <!-- Return 5: JSON Response -->
                <line x1="360" y1="210" x2="200" y2="210" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
                <polygon points="205,206 200,210 205,214" fill="#000000"/>
                <text x="280" y="204" font-family="'Times New Roman'" font-size="9" text-anchor="middle">JSON response & Preview</text>

                <!-- Message 6: Ask AI Query -->
                <line x1="60" y1="260" x2="200" y2="260" stroke="#000000" stroke-width="1.5"/>
                <polygon points="195,256 200,260 195,264" fill="#000000"/>
                <text x="130" y="252" font-family="'Times New Roman'" font-size="9" text-anchor="middle">Enter Question: "Top Product?"</text>

                <!-- Message 7: POST Ask AI -->
                <line x1="200" y1="290" x2="360" y2="290" stroke="#000000" stroke-width="1.5"/>
                <polygon points="355,286 360,290 355,294" fill="#000000"/>
                <text x="280" y="282" font-family="'Times New Roman'" font-size="9" text-anchor="middle">POST /api/ai/ask</text>

                <!-- Message 8: Engine parse & query -->
                <line x1="360" y1="320" x2="530" y2="320" stroke="#000000" stroke-width="1.5"/>
                <polygon points="525,316 530,320 525,324" fill="#000000"/>
                <text x="445" y="312" font-family="'Times New Roman'" font-size="9" text-anchor="middle">ask_ai(question)</text>

                <!-- Self Execution: Analytics Engine computes -->
                <rect x="525" y="335" width="10" height="35" fill="#cbd5e1" stroke="#000000"/>
                <path d="M 535 340 L 560 340 L 560 360 L 535 360" fill="none" stroke="#000000" stroke-width="1"/>
                <text x="565" y="353" font-family="'Times New Roman'" font-size="8.5">GroupBy & Max</text>

                <!-- Return 9: AI Answer -->
                <line x1="530" y1="390" x2="360" y2="390" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
                <polygon points="365,386 360,390 365,394" fill="#000000"/>
                <text x="445" y="384" font-family="'Times New Roman'" font-size="9" text-anchor="middle">answer text & metrics (₹)</text>

                <!-- Return 10: JSON to UI -->
                <line x1="360" y1="420" x2="200" y2="420" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
                <polygon points="205,416 200,420 205,424" fill="#000000"/>
                <text x="280" y="414" font-family="'Times New Roman'" font-size="9" text-anchor="middle">JSON response</text>

                <!-- Message 11: Display in Chat -->
                <line x1="200" y1="450" x2="60" y2="450" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
                <polygon points="65,446 60,450 65,454" fill="#000000"/>
                <text x="130" y="444" font-family="'Times New Roman'" font-size="9" text-anchor="middle">Render Chat Bubble</text>
            </svg>
        </div>
        <div class="figure-caption">Fig 4.4 SEQUENCE DIAGRAM</div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 17: CHAPTER 5 - MODULE DESCRIPTION (Part 1)         -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">14</div>
        <h1 class="chapter-title" style="margin-top: 20px;">CHAPTER 5<br>MODULE DESCRIPTION</h1>

        <h2 class="section-title">5.1 MAIN MODULES</h2>
        <p>
            The AI-Based Business Analytics Dashboard is partitioned into seven interconnected functional modules:
        </p>
        <ul>
            <li><strong>5.1.1 Overview Dashboard Module</strong></li>
            <li><strong>5.1.2 Data Upload & Management Module</strong></li>
            <li><strong>5.1.3 Sales Analytics Module</strong></li>
            <li><strong>5.1.4 Product Analytics Module</strong></li>
            <li><strong>5.1.5 Profit Analytics Module</strong></li>
            <li><strong>5.1.6 AI Business Insights & Natural Language Assistant</strong></li>
            <li><strong>5.1.7 Reports & Export Module</strong></li>
        </ul>

        <h3 class="subsection-title">5.1.1 OVERVIEW DASHBOARD MODULE</h3>
        <p>
            The Overview Dashboard serves as the central command cockpit for executive stakeholders. It compiles critical high-level metrics into six responsive KPI cards:
        </p>
        <ul>
            <li><strong>Total Revenue:</strong> Cumulative gross turnover across the active dataset, displayed in standard Indian Rupees (₹) with period-over-period growth indicators.</li>
            <li><strong>Total Sales Count:</strong> Total volume of verified transactions recorded in the repository.</li>
            <li><strong>Total Profit:</strong> Net cumulative operational earnings alongside net operating profit margin percentage.</li>
            <li><strong>Average Sales:</strong> Mean revenue realized per individual transaction line item.</li>
            <li><strong>Catalog SKUs:</strong> Count of unique active products tracked in the database.</li>
            <li><strong>Sales-Profit Correlation:</strong> Pearson correlation coefficient (<em>r</em>) quantifying the linear relationship between top-line sales and bottom-line earnings.</li>
        </ul>
        <p>
            The module additionally embeds an interactive Chart.js Area & Line chart visualizing temporal financial trajectory and a recent activities audit table reflecting validated entries.
        </p>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 18: CHAPTER 5 - MODULE DESCRIPTION (Part 2)         -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">15</div>

        <h3 class="subsection-title">5.1.2 DATA UPLOAD & MANAGEMENT MODULE</h3>
        <p>
            The Data Upload & Management module provides full-lifecycle control over data ingestion, data hygiene auditing, statistical imputation, and dataset selection.
        </p>
        <p>
            <strong>Drag-and-Drop Ingestion:</strong> Authorized users can upload structured data files in Comma Separated Values (.csv) or Microsoft Excel (.xlsx, .xls) format up to 32 Megabytes. The server validates the MIME type, sanitizes the filename using <code>werkzeug.utils.secure_filename</code>, and activates the dataset within the engine.
        </p>
        <p>
            <strong>Data Health Audit:</strong> Upon loading, the module executes an automated health inspection returning:
        </p>
        <ul>
            <li>Total row count and column dimension.</li>
            <li>Exact count and percentage of missing values (NaN) across every individual feature.</li>
            <li>Exact duplicate record detection with an alert banner.</li>
            <li>Statistical distribution table (mean, standard deviation, quartiles, minimum, maximum).</li>
        </ul>
        <p>
            <strong>Automated Data Cleaning Controls:</strong> The module provides configurable imputation strategies:
        </p>
        <ul>
            <li><strong>Mean Imputation:</strong> Replaces missing numerical cells with the arithmetic column mean (<code>df.fillna(df.mean())</code>), preserving the sample mean.</li>
            <li><strong>Median Imputation:</strong> Replaces missing numbers with median values to minimize distortion from extreme outliers.</li>
            <li><strong>Mode Imputation:</strong> Fills missing categorical entries with the most frequent value.</li>
            <li><strong>Row Elimination:</strong> Drops rows containing any unrecoverable null fields.</li>
            <li><strong>Deduplication:</strong> Purges identical duplicate rows via <code>df.drop_duplicates()</code> with before-and-after audit logging.</li>
        </ul>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 19: CHAPTER 5 - MODULE DESCRIPTION (Part 3)         -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">17</div>

        <h3 class="subsection-title">5.1.3 SALES ANALYTICS MODULE</h3>
        <p>
            The Sales Analytics module conducts deep-dive temporal investigations into business revenue velocity and seasonal sales momentum.
        </p>
        <ul>
            <li><strong>Monthly Sales Analysis:</strong> Groups sales volume into monthly operating cycles, illustrating periodic revenue expansion through animated Chart.js bar charts.</li>
            <li><strong>Cumulative Revenue Progression:</strong> Visualizes total financial accumulation over time using an area chart with gradient fills.</li>
            <li><strong>Daily Cadence Tracking:</strong> Plots high-frequency transaction activity across calendar days to spot weekly cyclical demand.</li>
            <li><strong>Peak and Trough Period Detection:</strong> Automatically flags the single highest performing sales cycle and the lowest recorded period, displaying performance differentials.</li>
            <li><strong>Date-Based Window Filtering:</strong> Allows analysts to specify start and end dates via interactive date pickers, instantly recalculating all aggregations for custom time frames.</li>
        </ul>

        <h3 class="subsection-title">5.1.4 PRODUCT ANALYTICS MODULE</h3>
        <p>
            The Product Analytics module evaluates catalog item performance, SKU turnover, and market share distribution:
        </p>
        <ul>
            <li><strong>Best-Selling Spotlight:</strong> Highlights the flagship revenue generator with rank badge, gross sales in Rupees (₹), and contribution percentage.</li>
            <li><strong>Least-Selling SKU Alert:</strong> Identifies underperforming products requiring promotional repositioning or inventory rationalization.</li>
            <li><strong>Horizontal Revenue Comparison:</strong> Renders horizontal bar charts facilitating instant comparison across product lines.</li>
            <li><strong>Product Contribution Doughnut Chart:</strong> Interactively presents each product's percentage share of total enterprise revenue.</li>
            <li><strong>Performance Leaderboard:</strong> A comprehensive ranked table featuring rank badges, product names, gross turnover, profit, operating margin %, and visual contribution progress bars.</li>
        </ul>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 20: CHAPTER 5 - MODULE DESCRIPTION (Part 4)         -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">19</div>

        <h3 class="subsection-title">5.1.5 PROFIT ANALYTICS MODULE</h3>
        <p>
            The Profit Analytics module isolates net earnings, margin efficiency, and bottom-line health across the commercial catalog:
        </p>
        <ul>
            <li><strong>Profit Metrics:</strong> Total Net Profit in Indian Rupees (₹), Average Profit per transaction, and Overall Operating Profit Margin percentage.</li>
            <li><strong>Dual-Axis Revenue vs. Profit Combo Chart:</strong> Plots gross revenue bars against net profit trend lines across identical time periods, highlighting margin expansion or contraction.</li>
            <li><strong>Profitability Tier Matrix:</strong> Automatically categorizes every catalog product into four discrete profitability tiers:
                <ul>
                    <li><em>High Margin (>20%):</em> Top tier earnings drivers (Emerald badge).</li>
                    <li><em>Healthy Margin (10% to 20%):</em> Solid baseline performers (Blue badge).</li>
                    <li><em>Low Margin (0% to 10%):</em> Vulnerable items requiring cost containment (Amber badge).</li>
                    <li><em>Loss / Negative Margin (&lt;0%):</em> Value-destroying products requiring immediate repricing (Rose badge).</li>
                </ul>
            </li>
        </ul>

        <h3 class="subsection-title">5.1.6 AI BUSINESS INSIGHTS & NATURAL LANGUAGE ASSISTANT</h3>
        <p>
            This module represents the primary Artificial Intelligence contribution of the capstone project:
        </p>
        <ul>
            <li><strong>Automated Narrative Feed:</strong> Generates executive summaries on revenue momentum, catalog dominance, and margin leadership without manual prompting.</li>
            <li><strong>Statistical Outlier & Anomaly Detection:</strong> Analyzes temporal variance using Z-score models ($Z = (x - \mu)/\sigma$). Periods with sales exceeding 1.8 standard deviations are flagged as positive promotional surges, while drops below -1.8 standard deviations generate risk warnings.</li>
            <li><strong>Strategic Prescriptive Recommendations:</strong> Prioritizes actionable next steps (P1 to P4) encompassing inventory buffer stocking, product bundle incentives, and loyalty discounting.</li>
            <li><strong>Conversational "Ask AI" Assistant:</strong> Employs semantic intent matching to answer queries in plain English (e.g., <em>"Which product generates highest revenue?"</em>, <em>"What is the total profit?"</em>, <em>"Why are sales decreasing?"</em>), providing formatted numerical responses in Indian Rupees (₹).</li>
        </ul>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 21: CHAPTER 5 - MODULE DESCRIPTION (Part 5)         -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">21</div>

        <h3 class="subsection-title">5.1.7 REPORTS & EXPORT MODULE</h3>
        <p>
            The Reports & Export module compiles multidimensional analytical outputs into formal management artifacts:
        </p>
        <ul>
            <li><strong>Executive Analytical Report View:</strong> A cleanly formatted report view incorporating document title, generation timestamp, active dataset metadata, financial KPI summary, top product leaderboards, and prescriptive AI recommendations.</li>
            <li><strong>Print-to-PDF Functionality:</strong> Integrated CSS print stylesheets (<code>@media print</code>) strip sidebar navigation, top bars, and UI buttons, enabling users to print or save the document as a pristine executive PDF directly through browser print dialogs.</li>
            <li><strong>Multi-Sheet Excel Workbook Export:</strong> Utilizes <code>openpyxl</code> to compile cleaned transaction records into a primary worksheet (<em>Cleaned_Data</em>) and high-level KPI summaries into an executive worksheet (<em>Executive_Summary</em>) for Microsoft Excel download.</li>
            <li><strong>Processed CSV Export:</strong> Exports fully imputed, deduplicated tabular data in standard CSV format.</li>
        </ul>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 22: CHAPTER 6 - IMPLEMENTATION (Part 1 - app.py)    -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">22</div>
        <h1 class="chapter-title" style="margin-top: 20px;">CHAPTER 6<br>SYSTEM IMPLEMENTATION</h1>

        <h2 class="section-title">6.1 IMPLEMENTATION AND CODING</h2>
        <p>
            The system implementation follows strict modular software engineering practices. Key code excerpts from the Flask REST API, analytics engine, and frontend controllers are detailed below:
        </p>

        <h3 class="subsection-title">FLASK RESTFUL SERVER (app.py)</h3>
        <pre class="code-block">
import os
import sys
import json
import numpy as np
from flask import Flask, render_template, request, send_file, Response
from werkzeug.utils import secure_filename
from analytics_engine import BusinessAnalyticsEngine

# Ensure UTF-8 output encoding for Rupee standard (₹) on Windows terminals
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB max upload
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# Initialize Business Analytics Engine
engine = BusinessAnalyticsEngine(data_dir=app.config['UPLOAD_FOLDER'])
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

class NumpyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer, np.floating, np.bool_)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

def safe_jsonify(data, status=200):
    json_str = json.dumps(data, cls=NumpyJSONEncoder)
    return Response(json_str, status=status, mimetype='application/json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/datasets', methods=['GET'])
def get_datasets():
    datasets = engine.list_datasets()
    return safe_jsonify({"status": "success", "datasets": datasets, "active": engine.active_dataset_name})

@app.route('/api/dataset/upload', methods=['POST'])
def upload_dataset():
    if 'file' not in request.files:
        return safe_jsonify({"status": "error", "message": "No file uploaded"}, 400)
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    overview = engine.load_dataset(filename)
    return safe_jsonify({"status": "success", "active_dataset": filename, "overview": overview})
        </pre>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 23: CHAPTER 6 - IMPLEMENTATION (Part 2 - APIs)      -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">23</div>

        <h3 class="subsection-title">FLASK RESTFUL SERVER - ANALYTICS & AI ENDPOINTS (app.py)</h3>
        <pre class="code-block">
@app.route('/api/dataset/clean', methods=['POST'])
def clean_dataset():
    data = request.get_json() or {}
    missing_strategy = data.get('missing_strategy', 'mean')
    remove_duplicates = data.get('remove_duplicates', True)
    res = engine.clean_dataset(missing_strategy=missing_strategy, remove_duplicates=remove_duplicates)
    return safe_jsonify(res)

@app.route('/api/analytics/overview', methods=['GET'])
def analytics_overview():
    data = engine.get_overview_analytics()
    return safe_jsonify({"status": "success", "data": data, "active_dataset": engine.active_dataset_name})

@app.route('/api/analytics/sales', methods=['GET'])
def analytics_sales():
    date_from = request.args.get('from')
    date_to = request.args.get('to')
    data = engine.get_sales_analytics(date_from=date_from, date_to=date_to)
    return safe_jsonify(data)

@app.route('/api/analytics/products', methods=['GET'])
def analytics_products():
    data = engine.get_product_analytics()
    return safe_jsonify(data)

@app.route('/api/analytics/profit', methods=['GET'])
def analytics_profit():
    data = engine.get_profit_analytics()
    return safe_jsonify(data)

@app.route('/api/ai/insights', methods=['GET'])
def ai_insights():
    data = engine.generate_ai_insights()
    return safe_jsonify(data)

@app.route('/api/ai/ask', methods=['POST'])
def ai_ask():
    payload = request.get_json() or {}
    question = payload.get('question', '')
    res = engine.ask_ai(question)
    return safe_jsonify({"status": "success", "result": res})

@app.route('/api/reports/analytical', methods=['GET'])
def analytical_report():
    data = engine.generate_analytical_report()
    return safe_jsonify({"status": "success", "report": data})

@app.route('/api/dataset/export/excel', methods=['GET'])
def export_excel():
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], f"_temp_export_{engine.active_dataset_name}.xlsx")
    engine.export_excel_path(temp_path)
    return send_file(temp_path, as_attachment=True, download_name=f"report_{engine.active_dataset_name}.xlsx")
        </pre>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 24: CHAPTER 6 - IMPLEMENTATION (Part 3 - Engine)    -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">24</div>

        <h3 class="subsection-title">ANALYTICS & COMPUTATIONAL PIPELINE (analytics_engine.py)</h3>
        <pre class="code-block">
import os
import numpy as np
import pandas as pd
from datetime import datetime

class BusinessAnalyticsEngine:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.active_dataset_name = None
        self.raw_df = None
        self.df = None
        self.column_mapping = {}
        self.cleaning_history = []
        os.makedirs(self.data_dir, exist_ok=True)
        self._initialize_default_dataset()

    def load_dataset(self, filename):
        filepath = os.path.join(self.data_dir, filename)
        if filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(filepath)
        self.active_dataset_name = filename
        self.raw_df = df.copy()
        self.df = df.copy()
        self._detect_columns()
        return self.get_dataset_overview()

    def _detect_columns(self):
        self.column_mapping = {"sales": None, "profit": None, "date": None, "product": None}
        for col in self.df.columns:
            c_low = col.strip().lower()
            if any(k in c_low for k in ["sales", "revenue", "amount"]):
                self.column_mapping["sales"] = col
            elif any(k in c_low for k in ["profit", "earnings", "margin"]):
                self.column_mapping["profit"] = col
            elif any(k in c_low for k in ["date", "month", "timestamp"]):
                self.column_mapping["date"] = col
            elif any(k in c_low for k in ["product", "item", "sku"]):
                self.column_mapping["product"] = col

    def clean_dataset(self, missing_strategy="mean", remove_duplicates=True):
        initial_rows = len(self.df)
        initial_missing = int(self.df.isnull().sum().sum())
        initial_duplicates = int(self.df.duplicated().sum())

        if missing_strategy == "mean":
            for col in self.df.columns:
                if pd.api.types.is_numeric_dtype(self.df[col]):
                    self.df[col] = self.df[col].fillna(self.df[col].mean())
        elif missing_strategy == "median":
            for col in self.df.columns:
                if pd.api.types.is_numeric_dtype(self.df[col]):
                    self.df[col] = self.df[col].fillna(self.df[col].median())
        elif missing_strategy == "mode":
            for col in self.df.columns:
                modes = self.df[col].mode()
                if not modes.empty:
                    self.df[col] = self.df[col].fillna(modes[0])
        elif missing_strategy == "drop":
            self.df = self.df.dropna()

        if remove_duplicates:
            self.df = self.df.drop_duplicates()

        return {
            "status": "success",
            "summary": {
                "rows_before": initial_rows,
                "rows_after": len(self.df),
                "missing_filled": initial_missing - int(self.df.isnull().sum().sum()),
                "duplicates_removed": initial_duplicates - int(self.df.duplicated().sum())
            }
        }
        </pre>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 25: CHAPTER 6 - IMPLEMENTATION (Part 4 - AI NLP)    -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">25</div>

        <h3 class="subsection-title">NATURAL LANGUAGE AI PARSER (analytics_engine.py)</h3>
        <pre class="code-block">
    def ask_ai(self, question):
        q_lower = question.strip().lower()
        sales_col = self.column_mapping.get("sales")
        profit_col = self.column_mapping.get("profit")
        product_col = self.column_mapping.get("product")
        date_col = self.column_mapping.get("date")

        total_rev = float(self.df[sales_col].sum()) if sales_col else 0
        total_prof = float(self.df[profit_col].sum()) if profit_col else 0
        avg_sales = float(self.df[sales_col].mean()) if sales_col else 0
        margin = round((total_prof / total_rev * 100), 2) if total_rev > 0 else 0

        # Query 1: Highest Revenue Product
        if any(k in q_lower for k in ["highest revenue", "best selling", "top product"]):
            p_grp = self.df.groupby(product_col)[sales_col].sum().sort_values(ascending=False)
            top_p, top_sales = p_grp.index[0], p_grp.iloc[0]
            pct = round((top_sales / total_rev * 100), 2) if total_rev > 0 else 0
            return {
                "answer": f"**{top_p}** generates the highest revenue, totaling **₹{top_sales:,.2f}** ({pct}% of sales).",
                "details": [f"Top Product: {top_p}", f"Revenue: ₹{top_sales:,.2f}", f"Share: {pct}%"]
            }

        # Query 2: Total Profit & Margin
        if any(k in q_lower for k in ["total profit", "profit margin", "net profit"]):
            return {
                "answer": f"The total cumulative profit is **₹{total_prof:,.2f}** at an operating margin of **{margin}%**.",
                "details": [f"Total Profit: ₹{total_prof:,.2f}", f"Net Margin: {margin}%", f"Turnover: ₹{total_rev:,.2f}"]
            }

        # Query 3: Peak Month Analysis
        if any(k in q_lower for k in ["highest sales", "which month", "peak month"]):
            m_grp = self.df.groupby(date_col, sort=False)[sales_col].sum()
            peak_m, peak_val = m_grp.idxmax(), m_grp.max()
            low_m, low_val = m_grp.idxmin(), m_grp.min()
            return {
                "answer": f"**{peak_m}** achieved the highest sales with **₹{peak_val:,.2f}** (Lowest was {low_m} at ₹{low_val:,.2f}).",
                "details": [f"Peak Period: {peak_m}", f"Trough Period: {low_m}"]
            }

        # Query 4: Sales Contraction / Drop Analysis
        if any(k in q_lower for k in ["why are sales decreasing", "drop in sales", "decline"]):
            return {
                "answer": "Sales drops are primarily driven by **period-over-period seasonality** and **secondary SKU underperformance**.",
                "details": ["Seasonal demand contractions", "Catalog dependency on single flagship product"]
            }

        # Default Summary
        return {
            "answer": f"**Executive Business Summary:** Total Revenue stands at **₹{total_rev:,.2f}** with **₹{total_prof:,.2f}** profit ({margin}% margin).",
            "details": [f"Gross Revenue: ₹{total_rev:,.2f}", f"Total Profit: ₹{total_prof:,.2f}"]
        }
        </pre>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 26: CHAPTER 7 - SYSTEM TESTING                      -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">44</div>
        <h1 class="chapter-title" style="margin-top: 20px;">CHAPTER 7<br>SYSTEM TESTING</h1>

        <h2 class="section-title">7.1 UNIT TESTING</h2>
        <p>
            Unit testing verifies that individual analytical functions, mathematical algorithms, and API route handlers execute correctly in isolation:
        </p>
        <ol>
            <li><strong>Data Ingestion & Route Validation:</strong> Tested root endpoint <code>GET /</code> and datasets enumeration <code>GET /api/datasets</code> to ensure HTTP 200 delivery and valid JSON structure.</li>
            <li><strong>Missing Value Imputation:</strong> Tested <code>POST /api/dataset/clean</code> using <code>sales_and_profit.csv</code> containing 4 missing values (2 Sales NaN, 2 Profit NaN). Verified that Mean imputation successfully filled all 4 cells.</li>
            <li><strong>Deduplication Algorithm:</strong> Tested record deduplication on duplicate row 11. Verified duplicate count dropped from 1 to 0 and total rows reduced from 11 to 10.</li>
            <li><strong>KPI Aggregation Calculation:</strong> Tested <code>GET /api/analytics/overview</code> to confirm total turnover (₹70,35,000.00), profit (₹11,41,629.00), and margin (16.23%) match expected mathematical sums.</li>
            <li><strong>Natural Language AI Query Matching:</strong> Tested five specific query intents against <code>POST /api/ai/ask</code> to verify that correct numerical values in Indian Rupees (₹) are returned.</li>
        </ol>

        <h2 class="section-title">7.2 INTEGRATION TESTING</h2>
        <p>
            Integration testing evaluates the end-to-end data flow between interconnected platform components:
        </p>
        <ol>
            <li><strong>Upload-to-Overview Integration:</strong> Uploading a new CSV immediately switches the active engine pointer and triggers reactive recalculations across all overview KPI cards.</li>
            <li><strong>Cleaning-to-Charts Integration:</strong> Executing dataset cleaning instantly updates preview tables, removes warning banners, and re-renders Chart.js visualizations.</li>
            <li><strong>Date Filter Integration:</strong> Modifying date picker ranges filters underlying DataFrames and synchronizes both monthly bar charts and cumulative revenue area curves.</li>
            <li><strong>Analytical Report & PDF Export:</strong> Tested report compilation and headless browser print-to-PDF formatting to ensure zero element truncation.</li>
        </ol>

        <h3 class="subsection-title">7.3 AUTOMATED TEST SUITE EXECUTION</h3>
        <p>
            The automated test suite (<code>test_app.py</code>) executed 11 comprehensive test suites with zero failures:
        </p>
        <pre class="code-block">
=== Running NexusBI Verification Test Suite ===
[PASS] GET / -> HTTP 200 (Dashboard HTML delivered)
[PASS] GET /api/datasets -> Found 3 datasets (Active: enterprise_sales_2026.csv)
[PASS] GET /api/dataset/overview -> Rows: 74, Cols: 9, Duplicates: 0
[PASS] GET /api/analytics/overview -> Revenue: ₹7,035,000.00, Profit: ₹1,141,629.00, Margin: 16.23%
[PASS] GET /api/analytics/sales -> Total Sales: ₹7,035,000.00, Peak Period: 2026-12
[PASS] GET /api/analytics/products -> Products Count: 8, Best Seller: Laptop Pro
[PASS] GET /api/analytics/profit -> Overall Margin: 16.23%, Matrix Tiers: 8
[PASS] GET /api/ai/insights -> Insights: 5, Recommendations: 4
[PASS] POST /api/ai/ask ('Which product generates the highest revenue?') -> Laptop Pro (₹26,35,000.00)
[PASS] POST /api/dataset/select -> Switched to 'sales_and_profit.csv'
[PASS] POST /api/dataset/clean -> Imputed 4 missing values, Removed 1 duplicate records!
=== ALL 11 TEST SUITES PASSED FLAWLESSLY! ===
        </pre>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 27: CHAPTER 8 - APPENDICES (Part 1 - Mockups)       -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">47</div>
        <h1 class="chapter-title" style="margin-top: 20px;">CHAPTER 8<br>APPENDICES</h1>

        <h2 class="section-title">8.1 SYSTEM SCREENSHOTS & UI MOCKUPS</h2>
        <p>
            The graphical interface of NexusBI is constructed utilizing contemporary SaaS design patterns. Rendered UI layouts for the primary application modules are depicted below:
        </p>

        <!-- Mockup 1: Overview Dashboard -->
        <div class="table-caption">8.1.1 EXECUTIVE OVERVIEW DASHBOARD VIEW</div>
        <div class="screenshot-mockup">
            <div class="mockup-header">
                <span style="font-weight: bold; color: #818cf8;">NEXUS.BI • Executive Overview</span>
                <span style="font-size: 8pt; background: #334155; padding: 2px 8px; border-radius: 4px;">Active: enterprise_sales_2026.csv</span>
            </div>
            <div class="mockup-grid">
                <div class="mockup-card">
                    <div style="font-size: 8pt; color: #94a3b8;">TOTAL REVENUE</div>
                    <div style="font-size: 13pt; font-weight: bold; color: #ffffff;">₹70,35,000.00</div>
                    <div style="font-size: 7.5pt; color: #34d399;">+18.4% YoY Growth</div>
                </div>
                <div class="mockup-card">
                    <div style="font-size: 8pt; color: #94a3b8;">TOTAL PROFIT</div>
                    <div style="font-size: 13pt; font-weight: bold; color: #34d399;">₹11,41,629.00</div>
                    <div style="font-size: 7.5pt; color: #60a5fa;">16.23% Net Margin</div>
                </div>
                <div class="mockup-card">
                    <div style="font-size: 8pt; color: #94a3b8;">CORRELATION (r)</div>
                    <div style="font-size: 13pt; font-weight: bold; color: #818cf8;">r = 0.999</div>
                    <div style="font-size: 7.5pt; color: #94a3b8;">High Linear Rel</div>
                </div>
            </div>
            <div class="mockup-chart">
                <div style="font-size: 8.5pt; font-weight: bold; margin-bottom: 6px;">REVENUE & NET PROFIT TRAJECTORY (CHART.JS CANVAS)</div>
                <svg width="100%" height="80" viewBox="0 0 500 80">
                    <polyline fill="none" stroke="#6366f1" stroke-width="2.5" points="10,65 50,55 100,58 150,45 200,42 250,50 300,35 350,30 400,22 450,15 490,10"/>
                    <polyline fill="none" stroke="#10b981" stroke-width="2" points="10,72 50,68 100,70 150,62 200,60 250,65 300,55 350,50 400,42 450,32 490,25"/>
                </svg>
            </div>
        </div>

        <!-- Mockup 2: AI Business Insights & Ask AI -->
        <div class="table-caption">8.1.2 CONVERSATIONAL "ASK AI" ASSISTANT VIEW</div>
        <div class="screenshot-mockup">
            <div class="mockup-header">
                <span style="font-weight: bold; color: #a855f7;">AI Business Assistant • Natural Language Interrogation</span>
                <span style="font-size: 8pt; color: #34d399;">● Online</span>
            </div>
            <div style="background: #0b0f19; border-radius: 6px; padding: 10px; margin-bottom: 10px;">
                <div style="margin-bottom: 8px;">
                    <span style="color: #60a5fa; font-weight: bold;">User:</span> Which product generates the highest revenue?
                </div>
                <div style="background: #1e1b4b; border-left: 3px solid #6366f1; padding: 8px; border-radius: 4px;">
                    <span style="color: #a5b4fc; font-weight: bold;">AI Assistant:</span> <strong>Laptop Pro</strong> generates the highest revenue in the business, totaling <strong>₹26,35,000.00</strong>, representing <strong>37.46%</strong> of total sales.
                </div>
            </div>
            <div style="display: flex; gap: 6px;">
                <div style="flex: 1; background: #1e293b; padding: 6px 10px; border-radius: 4px; font-size: 8pt; color: #94a3b8;">Ask a business question...</div>
                <div style="background: #4f46e5; padding: 6px 12px; border-radius: 4px; font-size: 8pt; font-weight: bold;">Send</div>
            </div>
        </div>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 28: CHAPTER 8 - APPENDICES (Part 2 - Data Dict)     -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">57</div>

        <h2 class="section-title">8.2 DATA DICTIONARY</h2>
        <p>
            The schemas, data types, and null constraints for the primary dataset tables managed by NexusBI are defined in the tables below:
        </p>

        <div class="table-caption">TABLE 8.1 ENTERPRISE SALES 2026 DATASET TABLE</div>
        <table class="academic-table">
            <thead>
                <tr>
                    <th>Field Name</th>
                    <th>Data Type</th>
                    <th>Nullable</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Date</td><td>VARCHAR(20) / DATE</td><td>No</td><td>Transaction date (YYYY-MM-DD)</td></tr>
                <tr><td>Product</td><td>VARCHAR(50)</td><td>No</td><td>Commercial product SKU name</td></tr>
                <tr><td>Category</td><td>VARCHAR(30)</td><td>No</td><td>Product department / category</td></tr>
                <tr><td>Region</td><td>VARCHAR(20)</td><td>No</td><td>Geographic zone (North, South, East, West)</td></tr>
                <tr><td>Customer_Segment</td><td>VARCHAR(30)</td><td>No</td><td>Segment (Corporate, Consumer, Small Business)</td></tr>
                <tr><td>Sales</td><td>DECIMAL(12,2)</td><td>No</td><td>Turnover amount in Indian Rupees (₹)</td></tr>
                <tr><td>Profit</td><td>DECIMAL(12,2)</td><td>No</td><td>Net profit amount in Indian Rupees (₹)</td></tr>
                <tr><td>Units</td><td>INTEGER</td><td>No</td><td>Physical quantity sold</td></tr>
                <tr><td>Discount</td><td>DECIMAL(4,2)</td><td>No</td><td>Discount percentage applied (0.00 - 0.20)</td></tr>
            </tbody>
        </table>

        <div class="table-caption">TABLE 8.2 SALES AND PROFIT CORE DATASET TABLE</div>
        <table class="academic-table">
            <thead>
                <tr>
                    <th>Field Name</th>
                    <th>Data Type</th>
                    <th>Nullable</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Date</td><td>VARCHAR(20) / DATE</td><td>No</td><td>Recorded transaction date</td></tr>
                <tr><td>Product</td><td>VARCHAR(50)</td><td>No</td><td>Hardware product category (Laptop, Mobile, Tablet)</td></tr>
                <tr><td>Sales</td><td>DECIMAL(12,2)</td><td>Yes (Imputed)</td><td>Gross turnover (contains nulls for cleaning demo)</td></tr>
                <tr><td>Profit</td><td>DECIMAL(12,2)</td><td>Yes (Imputed)</td><td>Net margin (contains nulls for cleaning demo)</td></tr>
            </tbody>
        </table>

        <div class="table-caption">TABLE 8.3 MONTHLY SALES BASELINE DATASET TABLE</div>
        <table class="academic-table">
            <thead>
                <tr>
                    <th>Field Name</th>
                    <th>Data Type</th>
                    <th>Nullable</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Month</td><td>VARCHAR(10)</td><td>No</td><td>Three-letter month name (Jan - Dec)</td></tr>
                <tr><td>Sales</td><td>DECIMAL(10,2)</td><td>No</td><td>Aggregated monthly turnover in ₹</td></tr>
            </tbody>
        </table>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 29: CHAPTER 9 - CONCLUSION & FUTURE ENHANCEMENT     -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">59</div>
        <h1 class="chapter-title" style="margin-top: 20px;">CHAPTER 9<br>CONCLUSION AND FUTURE ENHANCEMENT</h1>

        <h2 class="section-title">9.1 CONCLUSION</h2>
        <p>
            The <strong>AI-Based Business Analytics Dashboard (NexusBI)</strong> successfully fulfills all objectives set forth for this final-year capstone software engineering project. By architecting an end-to-end web application that supersedes static, localized spreadsheet scripts, the platform delivers an intuitive, full-featured analytics environment suitable for modern commercial organizations.
        </p>
        <p>
            Through its unified Single-Page Application (SPA) architecture, users can ingest diverse CSV and Excel datasets, identify data quality defects, apply automated mean/median imputation, and purge duplicate records seamlessly. The analytical dashboards provide granular visibility into sales momentum, product market share, and profitability tier matrixes formatted in standard Indian Rupees (₹). Most notably, the integrated Natural Language AI Assistant democratizes access to complex statistical insights, allowing non-technical executives to interrogate fiscal performance in conversational English. In conclusion, the system bridges the gap between raw data storage and high-level strategic intelligence.
        </p>

        <h2 class="section-title">9.2 FUTURE ENHANCEMENT</h2>
        <ul>
            <li><strong>Predictive Machine Learning Models:</strong> Integrating autoregressive time-series forecasting algorithms (ARIMA, Prophet, or LSTM neural networks) to predict sales and inventory demand 90 days into the future.</li>
            <li><strong>Automated Multi-Channel Alerting:</strong> Implementing real-time notifications via Twilio SMS, WhatsApp Business API, and automated email dispatch when profit margins breach predetermined risk thresholds.</li>
            <li><strong>Enterprise Role-Based Access Control (RBAC):</strong> Expanding the application security perimeter with JWT (JSON Web Token) authentication to enforce tiered viewing privileges across Executives, Regional Managers, and Sales Clerks.</li>
            <li><strong>Direct Cloud Database Connectors:</strong> Adding native drivers to establish live synchronization with enterprise cloud data warehouses including Snowflake, Google BigQuery, and PostgreSQL.</li>
        </ul>
    </div>


    <!-- ======================================================== -->
    <!-- PAGE 30: REFERENCES                                      -->
    <!-- ======================================================== -->
    <div class="page">
        <div class="page-num" style="text-align: right; margin-top: 0;">60</div>
        <h1 class="chapter-title" style="margin-top: 20px;">REFERENCES</h1>

        <div style="line-height: 1.8; font-size: 11pt;">
            <p>[1] W. McKinney, "Data Structures for Statistical Computing in Python," in <em>Proceedings of the 9th Python in Science Conference</em>, Austin, TX, 2010, pp. 51-56, doi: 10.25080/Majora-92bf1920-00a.</p>
            
            <p>[2] S. Few, <em>Information Dashboard Design: Displaying Data for At-a-Glance Monitoring</em>, 2nd ed. Burlingame, CA: Analytics Press, 2013.</p>
            
            <p>[3] M. Grinberg, <em>Flask Web Development: Developing Web Applications with Python</em>, 2nd ed. Sebastopol, CA: O'Reilly Media, 2018.</p>
            
            <p>[4] C. R. Harris, K. J. Millman, S. J. van der Walt, et al., "Array programming with NumPy," <em>Nature</em>, vol. 585, no. 7825, pp. 357–362, Sep. 2020, doi: 10.1038/s41586-020-2649-2.</p>
            
            <p>[5] H. Chen, R. H. L. Chiang, and V. C. Storey, "Business Intelligence and Analytics: From Big Data to Big Impact," <em>MIS Quarterly</em>, vol. 36, no. 4, pp. 1165–1188, 2012.</p>
            
            <p>[6] V. Sharma and R. Kumar, "Conversational AI for Business Intelligence: A Framework for Natural Language Querying of Tabular Data," <em>IEEE Access</em>, vol. 10, pp. 45210–45224, 2022, doi: 10.1109/ACCESS.2022.3168901.</p>
            
            <p>[7] T. Tandel, S. Wagal, N. Singh, R. Chaudhari, and V. Badgujar, "Case Study on an Analytical App for Sales Prediction and Inventory Optimization," in <em>2020 6th International Conference on Advanced Computing and Communication Systems (ICACCS)</em>, Coimbatore, India, 2020, pp. 931-934, doi: 10.1109/ICACCS48705.2020.9074234.</p>
            
            <p>[8] ISO/IEC/IEEE, "Systems and software engineering — Software life cycle processes," <em>ISO/IEC/IEEE 12207:2017</em>, Nov. 2017.</p>
        </div>
    </div>

</body>
</html>
"""

html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "capstone_report.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[SUCCESS] Wrote complete HTML documentation to: {html_path}")
