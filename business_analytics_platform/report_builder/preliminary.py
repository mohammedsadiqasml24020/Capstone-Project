from report_builder.config import wrap_page, get_b64

def get_preliminary_pages():
    pages = []
    
    # PAGE 1: TITLE / COVER PAGE (Exact Clone of Sample Template with Real AMET Logo)
    p1 = f"""
    <div style="text-align: center; display: flex; flex-direction: column; justify-content: space-between; height: 100%;">
        <div>
            <!-- Real AMET University Logo Header from Template -->
            <div style="margin-top: 15px; margin-bottom: 25px;">
                <img src="{get_b64('amet_university_logo.png')}" style="width: 250px; height: auto;" alt="AMET UNIVERSITY">
            </div>

            <div style="font-size: 15.5pt; font-weight: bold; letter-spacing: 0.5px; margin: 30px 0 20px 0; text-transform: uppercase;">
                AI-BASED BUSINESS ANALYTICS DASHBOARD
            </div>
            
            <div style="font-size: 12pt; font-style: italic; margin-bottom: 12px;">Submitted by</div>
            
            <div style="font-size: 14pt; font-weight: bold; margin-bottom: 5px; letter-spacing: 0.5px;">MOHAMMED SADIQ A</div>
            <div style="font-size: 12.5pt; font-weight: bold; margin-bottom: 18px;">Reg. No (ASML24020)</div>

            <div style="font-size: 12pt; font-style: italic; margin-bottom: 15px;">of</div>
            <div style="font-size: 13pt; font-weight: bold; margin-bottom: 22px;">AMET UNIVERSITY</div>

            <div style="font-size: 13pt; font-weight: bold; margin: 15px 0; letter-spacing: 0.5px;">A CAPSTONE PROJECT REPORT</div>

            <div style="font-size: 11pt; font-style: italic; margin: 10px 0;">Submitted to the</div>
            <div style="font-size: 12.5pt; font-weight: bold; margin-bottom: 15px;">FACULTY OF ADVANCED COMPUTING SCIENCES</div>

            <div style="font-size: 11pt; font-style: italic; margin: 10px 0;">In partial fulfillment of requirements for the award of the degree of</div>
            
            <div style="font-size: 13pt; font-weight: bold; margin: 12px 0; line-height: 1.35;">
                BACHELOR OF SCIENCE -<br>
                ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING
            </div>
        </div>

        <div style="margin-bottom: 10px;">
            <div style="font-size: 12pt; font-weight: bold; margin-top: 15px;">AMET UNIVERSITY</div>
            <div style="font-size: 11pt; line-height: 1.35; margin-top: 5px;">135, East Coast Road, Kanathur - 603 112</div>
            <div style="font-size: 11pt; line-height: 1.35;">Tamil Nadu, India</div>
            <div style="font-size: 12pt; font-weight: bold; margin-top: 12px; letter-spacing: 1px;">NOVEMBER 2026</div>
        </div>
    </div>
    """
    pages.append(wrap_page(p1, ""))

    # PAGE 2: BONAFIDE CERTIFICATE
    p2 = """
    <h1 class="chap-title" style="margin-top: 40px;">BONAFIDE CERTIFICATE</h1>
    <p style="line-height: 1.8; font-size: 12pt; margin-top: 30px; text-align: justify;">
        Certified that this project report titled <strong>&ldquo;AI-BASED BUSINESS ANALYTICS DASHBOARD&rdquo;</strong> is the bonafide work of <strong>MOHAMMED SADIQ A (Reg No: ASML24020)</strong> who carried out the project under supervision. Certified further, that to the best of my knowledge, the work report or dissertation on the basics of which a degree or award was conferred on an earlier occasion on this or any other candidate.
    </p>

    <div style="display: flex; justify-content: space-between; margin-top: 70px;">
        <div style="width: 45%; line-height: 1.4; font-size: 11pt;">
            <strong>Supervisor</strong><br>
            <br>
            <strong>Mr. Tamilarasan D, M.C.A.,</strong><br>
            Assistant Professor,<br>
            Department of ACS,<br>
            AMET University,<br>
            Kanathur - 603 112.
        </div>
        <div style="width: 45%; line-height: 1.4; font-size: 11pt; text-align: right;">
            <strong>Head of the Department</strong><br>
            <br>
            <strong>Dr. C.N. Ravi, Ph.D.,</strong><br>
            Head of the Department,<br>
            Department of CSE,<br>
            AMET University,<br>
            Kanathur - 603 112.
        </div>
    </div>

    <div style="margin-top: 60px; font-size: 11pt;">
        Submitted for Project Viva Examination held on ______________________
    </div>

    <div style="display: flex; justify-content: space-between; margin-top: 60px; font-size: 11pt; font-weight: bold;">
        <div>Internal Examiner</div>
        <div>External Examiner</div>
    </div>
    """
    pages.append(wrap_page(p2, ""))

    # PAGE 3: ABSTRACT
    p3 = """
    <h1 class="chap-title">ABSTRACT</h1>
    <p style="text-align: justify;">
        The <strong>AI-Based Business Analytics Dashboard (NexusBI)</strong> is an innovative project introducing an integrated web application to revolutionize enterprise analytics and business intelligence operations. The system focuses on maximizing analytical efficiency, streamlining data cleaning processes, eliminating manual tracking errors, and enabling data-driven decision-making for enhanced business performance across modern retail, manufacturing, and distribution enterprises.
    </p>
    <p style="text-align: justify;">
        Through a user-friendly, feature-rich web application built with Python Flask, Pandas, and interactive Chart.js, the system empowers business managers, data analysts, and executive teams to oversee business analytics tasks seamlessly. The automated CSV/Excel data upload and preprocessing modules facilitate real-time data ingestion, fostering complete transparency, duplicate elimination, missing-value imputation, and integrity in transactional and revenue management.
    </p>
    <p style="text-align: justify;">
        Advanced analytical concepts simplify multidimensional revenue and profit computations, daily and monthly performance trajectories, and category contribution breakdowns in Indian Rupees (₹ INR), significantly mitigating operational discrepancies and enhancing fiscal reporting precision. The platform incorporates automated rule-based AI business insights and a natural language business assistant capable of resolving plain-English analytical inquiries on demand.
    </p>
    <p style="text-align: justify;">
        Comprehensive reporting functionalities allow export to PDF, Excel, and sanitized CSV formats. In-depth reports on revenue surges, product profit margins, and sales distributions provide stakeholders with indispensable visibility into customer consumption patterns and supplier margins. Data-driven decision-making capabilities enable proactive address of revenue declines, optimized inventory allocations, and streamlined cost management.
    </p>
    <p style="text-align: justify;">
        In conclusion, the AI-Based Business Analytics Dashboard represents a well-crafted and original full-stack web application, redefining modern enterprise decision support systems. This system aims to transform cost optimization, elevate stakeholder satisfaction, and empower organizations to achieve unparalleled success by prioritizing efficiency, computational accuracy, and AI-driven data intelligence.
    </p>
    """
    pages.append(wrap_page(p3, '<div class="roman-num">i</div>'))

    # PAGE 4: ACKNOWLEDGEMENT
    p4 = """
    <h1 class="chap-title">ACKNOWLEDGEMENT</h1>
    <p style="text-align: justify;">
        I offer our gratitude to the <strong>Lord Almighty</strong> who graced us and helped us all along to complete the project successfully. I would like to acknowledge the people who helped us to develop this project and who made it possible to do so.
    </p>
    <p style="text-align: justify;">
        First and foremost, we sincerely thank <strong>AMET University</strong> for providing a vibrant academic atmosphere, world-class computational laboratories, and institutional resources enabling us to complete this work successfully.
    </p>
    <p style="text-align: justify;">
        I owe my sincere thanks to <strong>Dr. C.N. Ravi, Ph.D.</strong>, Head of the Department, Department of CSE, AMET University for taking a keen interest in the project and for guiding throughout the work even under his busy schedule and also for his valuable guidance, coordination and his efforts to bring out the best in me, his availability at all times and through providing questions and timely suggestions and motivation to complete this project.
    </p>
    <p style="text-align: justify;">
        I express my sincere thanks to my project guide <strong>Mr. Tamilarasan D, M.C.A.</strong>, Assistant Professor, Project Supervisor, Department of ACS for his valuable guidance, coordination, and his efforts to bring out the best of me, his availability at all times and thought-providing questions and timely suggestions.
    </p>
    <p style="text-align: justify;">
        I am also very thankful to <strong>Mr. Aakaash M, M.C.A.</strong>, Assistant Professor and Faculty Advisor, Department of ACS. I greatly benefited from the invaluable guidance and coordination of his efforts to bring out the best in me.
    </p>
    <p style="text-align: justify;">
        I also express my thanks to all the faculty members of the Department of ACS, AMET University for their constant support and encouragement. I also express our thanks to all the non-teaching staff members for their cooperative assistance in the laboratory facilities.
    </p>
    <p style="text-align: justify;">
        Finally, I express my deepest gratitude to my Parents and friends for their constant support, understanding, and encouragement throughout my degree tenure.
    </p>
    """
    pages.append(wrap_page(p4, '<div class="roman-num">iv</div>'))

    # PAGE 5: TABLE OF CONTENTS (Part 1)
    p5 = """
    <h1 class="chap-title">TABLE OF CONTENTS</h1>
    <div class="toc-row" style="font-weight: bold; border-bottom: 1.5px solid #000; padding-bottom: 4px; margin-bottom: 10px;">
        <div class="toc-left">
            <div class="toc-num">CHAPTER</div>
            <div class="toc-title">TITLE</div>
        </div>
        <div class="toc-page">PAGE NO</div>
    </div>

    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">ABSTRACT (ENGLISH)</div></div><div class="toc-dots"></div><div class="toc-page">i</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">ACKNOWLEDGEMENT</div></div><div class="toc-dots"></div><div class="toc-page">iv</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">TABLE OF CONTENTS</div></div><div class="toc-dots"></div><div class="toc-page">v</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">LIST OF FIGURES</div></div><div class="toc-dots"></div><div class="toc-page">vii</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">LIST OF TABLES</div></div><div class="toc-dots"></div><div class="toc-page">vii</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">ABBREVIATIONS</div></div><div class="toc-dots"></div><div class="toc-page">viii</div></div>
    
    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num">1</div><div class="toc-title">INTRODUCTION</div></div><div class="toc-dots"></div><div class="toc-page">9</div></div>
    
    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num">2</div><div class="toc-title">SYSTEM ANALYSIS</div></div><div class="toc-dots"></div><div class="toc-page">10</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">2.1 EXISTING SYSTEM</div></div><div class="toc-dots"></div><div class="toc-page">10</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">2.2 PROPOSED SYSTEM</div></div><div class="toc-dots"></div><div class="toc-page">10</div></div>

    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num">3</div><div class="toc-title">SYSTEM REQUIREMENTS</div></div><div class="toc-dots"></div><div class="toc-page">11</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">3.1 HARDWARE REQUIREMENTS</div></div><div class="toc-dots"></div><div class="toc-page">11</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">3.2 SOFTWARE REQUIREMENTS</div></div><div class="toc-dots"></div><div class="toc-page">11</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">3.3 SOFTWARE REQUIREMENT SPECIFICATION</div></div><div class="toc-dots"></div><div class="toc-page">11</div></div>

    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num">4</div><div class="toc-title">SYSTEM DESIGN</div></div><div class="toc-dots"></div><div class="toc-page">18</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">4.1 ARCHITECTURE DIAGRAM</div></div><div class="toc-dots"></div><div class="toc-page">18</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">4.2 UML DIAGRAM</div></div><div class="toc-dots"></div><div class="toc-page">19</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">4.2.1 USE CASE DIAGRAM</div></div><div class="toc-dots"></div><div class="toc-page">19</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">4.2.2 CLASS DIAGRAM</div></div><div class="toc-dots"></div><div class="toc-page">20</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">4.2.3 SEQUENCE DIAGRAM</div></div><div class="toc-dots"></div><div class="toc-page">21</div></div>

    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num">5</div><div class="toc-title">MODULE DESCRIPTION</div></div><div class="toc-dots"></div><div class="toc-page">22</div></div>
    """
    pages.append(wrap_page(p5, '<div class="roman-num">vi</div>'))

    # PAGE 6: TABLE OF CONTENTS (Part 2)
    p6 = """
    <div class="toc-row" style="font-weight: bold; border-bottom: 1.5px solid #000; padding-bottom: 4px; margin-bottom: 10px; margin-top: 25px;">
        <div class="toc-left">
            <div class="toc-num">CHAPTER</div>
            <div class="toc-title">TITLE</div>
        </div>
        <div class="toc-page">PAGE NO</div>
    </div>

    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">5.1 MAIN MODULES</div></div><div class="toc-dots"></div><div class="toc-page">22</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">5.1.1 EXECUTIVE OVERVIEW DASHBOARD</div></div><div class="toc-dots"></div><div class="toc-page">22</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">5.1.2 DATA UPLOAD &amp; CLEANING</div></div><div class="toc-dots"></div><div class="toc-page">23</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">5.1.3 SALES PERFORMANCE ANALYTICS</div></div><div class="toc-dots"></div><div class="toc-page">25</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">5.1.4 PRODUCT &amp; CATEGORY ANALYTICS</div></div><div class="toc-dots"></div><div class="toc-page">26</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">5.1.5 PROFIT MARGIN ANALYTICS</div></div><div class="toc-dots"></div><div class="toc-page">27</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">5.1.6 AI BUSINESS INSIGHTS &amp; Q&amp;A</div></div><div class="toc-dots"></div><div class="toc-page">28</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 40px;">5.1.7 REPORTING &amp; MULTI-FORMAT EXPORT</div></div><div class="toc-dots"></div><div class="toc-page">29</div></div>

    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num">6</div><div class="toc-title">IMPLEMENTATION AND TESTING</div></div><div class="toc-dots"></div><div class="toc-page">30</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">6.1 IMPLEMENTATION AND CODING</div></div><div class="toc-dots"></div><div class="toc-page">30</div></div>

    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num">7</div><div class="toc-title">SYSTEM TESTING</div></div><div class="toc-dots"></div><div class="toc-page">52</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">7.1 UNIT TESTING</div></div><div class="toc-dots"></div><div class="toc-page">52</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">7.2 INTEGRATION TESTING</div></div><div class="toc-dots"></div><div class="toc-page">53</div></div>

    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num">8</div><div class="toc-title">APPENDICES</div></div><div class="toc-dots"></div><div class="toc-page">55</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">8.1 SCREENSHOTS</div></div><div class="toc-dots"></div><div class="toc-page">55</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">8.2 DATA DICTIONARY</div></div><div class="toc-dots"></div><div class="toc-page">65</div></div>

    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num">9</div><div class="toc-title">CONCLUSION AND FUTURE ENHANCEMENT</div></div><div class="toc-dots"></div><div class="toc-page">67</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">9.1 CONCLUSION</div></div><div class="toc-dots"></div><div class="toc-page">67</div></div>
    <div class="toc-row"><div class="toc-left"><div class="toc-num"></div><div class="toc-title" style="padding-left: 20px;">9.2 FUTURE ENHANCEMENT</div></div><div class="toc-dots"></div><div class="toc-page">67</div></div>

    <div class="toc-row" style="font-weight: bold; margin-top: 10px;"><div class="toc-left"><div class="toc-num"></div><div class="toc-title">REFERENCES</div></div><div class="toc-dots"></div><div class="toc-page">68</div></div>
    """
    pages.append(wrap_page(p6, '<div class="roman-num">vi</div>'))

    # PAGE 7: LIST OF FIGURES & LIST OF TABLES
    p7 = """
    <h1 class="chap-title" style="margin-bottom: 15px;">LIST OF FIGURES</h1>
    <table class="academic-table" style="margin-bottom: 30px;">
        <thead>
            <tr>
                <th style="width: 25%;">FIGURE NO</th>
                <th style="width: 55%;">NAME</th>
                <th style="width: 20%;">PAGE NO</th>
            </tr>
        </thead>
        <tbody>
            <tr><td style="text-align: center;">4.1</td><td>ARCHITECTURE DIAGRAM</td><td style="text-align: center;">18</td></tr>
            <tr><td style="text-align: center;">4.2</td><td>USE CASE DIAGRAM</td><td style="text-align: center;">19</td></tr>
            <tr><td style="text-align: center;">4.3</td><td>CLASS DIAGRAM</td><td style="text-align: center;">20</td></tr>
            <tr><td style="text-align: center;">4.4</td><td>SEQUENCE DIAGRAM</td><td style="text-align: center;">21</td></tr>
        </tbody>
    </table>

    <h1 class="chap-title" style="margin-bottom: 15px; margin-top: 30px;">LIST OF TABLES</h1>
    <table class="academic-table">
        <thead>
            <tr>
                <th style="width: 25%;">TABLE NO</th>
                <th style="width: 55%;">NAME</th>
                <th style="width: 20%;">PAGE NO</th>
            </tr>
        </thead>
        <tbody>
            <tr><td style="text-align: center;">8.1</td><td>USER &amp; SESSION TABLE</td><td style="text-align: center;">65</td></tr>
            <tr><td style="text-align: center;">8.2</td><td>DATASET INVENTORY TABLE</td><td style="text-align: center;">65</td></tr>
            <tr><td style="text-align: center;">8.3</td><td>SALES TRANSACTION TABLE</td><td style="text-align: center;">65</td></tr>
            <tr><td style="text-align: center;">8.4</td><td>PRODUCT PROFITABILITY TABLE</td><td style="text-align: center;">66</td></tr>
            <tr><td style="text-align: center;">8.5</td><td>AI INSIGHTS AUDIT TABLE</td><td style="text-align: center;">66</td></tr>
        </tbody>
    </table>
    """
    pages.append(wrap_page(p7, '<div class="roman-num">vii</div>'))

    # PAGE 8: ABBREVIATIONS
    p8 = """
    <h1 class="chap-title">ABBREVIATIONS</h1>
    <div style="margin-top: 30px; line-height: 2.2; font-size: 11.5pt;">
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">HTML</div><div style="width: 30px;">-</div><div>HYPERTEXT MARKUP LANGUAGE</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">CSS</div><div style="width: 30px;">-</div><div>CASCADING STYLE SHEETS</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">JS</div><div style="width: 30px;">-</div><div>JAVASCRIPT</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">AJAX</div><div style="width: 30px;">-</div><div>ASYNCHRONOUS JAVASCRIPT AND XML</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">HTTP</div><div style="width: 30px;">-</div><div>HYPERTEXT TRANSFER PROTOCOL</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">API</div><div style="width: 30px;">-</div><div>APPLICATION PROGRAMMING INTERFACE</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">REST</div><div style="width: 30px;">-</div><div>REPRESENTATIONAL STATE TRANSFER</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">JSON</div><div style="width: 30px;">-</div><div>JAVASCRIPT OBJECT NOTATION</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">CSV</div><div style="width: 30px;">-</div><div>COMMA SEPARATED VALUES</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">XLSX</div><div style="width: 30px;">-</div><div>MICROSOFT EXCEL OPEN XML SPREADSHEET</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">NLP</div><div style="width: 30px;">-</div><div>NATURAL LANGUAGE PROCESSING</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">KPI</div><div style="width: 30px;">-</div><div>KEY PERFORMANCE INDICATOR</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">SPA</div><div style="width: 30px;">-</div><div>SINGLE PAGE APPLICATION</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">BI</div><div style="width: 30px;">-</div><div>BUSINESS INTELLIGENCE</div></div>
        <div style="display: flex;"><div style="width: 140px; font-weight: bold;">INR</div><div style="width: 30px;">-</div><div>INDIAN RUPEE (&#8377;)</div></div>
    </div>
    """
    pages.append(wrap_page(p8, '<div class="roman-num">viii</div>'))

    return pages
