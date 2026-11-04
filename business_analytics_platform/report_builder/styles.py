CSS = """
@page {
    size: A4 portrait;
    margin: 25mm 20mm 25mm 25mm;
}
@page :first {
    margin: 20mm;
}
* {
    box-sizing: border-box;
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
    page-break-inside: avoid;
    height: 245mm;
    max-height: 245mm;
    overflow: hidden;
    position: relative;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.page-content {
    flex-grow: 1;
}
.page-num {
    text-align: center;
    font-size: 11pt;
    font-family: 'Times New Roman', Times, serif;
    margin-top: 5px;
    padding-bottom: 5px;
}
.roman-num {
    text-align: center;
    font-size: 11pt;
    font-style: italic;
    font-family: 'Times New Roman', Times, serif;
    margin-top: 5px;
    padding-bottom: 5px;
}
h1.chap-title {
    text-align: center;
    font-size: 14pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-top: 10px;
    margin-bottom: 22px;
    letter-spacing: 0.5px;
    line-height: 1.4;
}
h2.sec-title {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 16px;
    margin-bottom: 8px;
    text-transform: uppercase;
}
h3.subsec-title {
    font-size: 11.5pt;
    font-weight: bold;
    margin-top: 12px;
    margin-bottom: 6px;
    text-transform: uppercase;
}
p {
    margin-top: 0;
    margin-bottom: 10px;
    text-indent: 0;
    line-height: 1.5;
}
ul, ol {
    margin-top: 0;
    margin-bottom: 10px;
    padding-left: 25px;
}
li {
    margin-bottom: 5px;
    line-height: 1.45;
}
table.academic-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
    margin-bottom: 14px;
    font-size: 9.5pt;
}
table.academic-table th, table.academic-table td {
    border: 1px solid #000000;
    padding: 5px 8px;
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
    margin-top: 10px;
    margin-bottom: 6px;
    font-size: 10.5pt;
}
.figure-caption {
    text-align: center;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: 14px;
    font-size: 10.5pt;
}
.code-container {
    background-color: #f8f9fa;
    border: 1px solid #ccc;
    padding: 8px 10px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 8.5pt;
    line-height: 1.35;
    white-space: pre-wrap;
    word-break: break-all;
    border-radius: 4px;
    margin: 6px 0;
}
.screenshot-frame {
    text-align: center;
    margin: 6px auto;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 4px;
    background: #f8fafc;
}
.screenshot-img {
    max-width: 95%;
    max-height: 175mm;
    object-fit: contain;
    border-radius: 4px;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
}
.screenshot-img-android {
    max-width: 55%;
    max-height: 180mm;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.15);
}
.toc-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 5px;
    font-size: 10.5pt;
}
.toc-left {
    display: flex;
    align-items: baseline;
    flex: 1;
}
.toc-num {
    width: 65px;
    flex-shrink: 0;
    font-weight: bold;
}
.toc-title {
    flex: 1;
    padding-right: 8px;
}
.toc-dots {
    flex-grow: 1;
    border-bottom: 1px dotted #555;
    margin: 0 6px;
    height: 12px;
}
.toc-page {
    font-weight: bold;
    flex-shrink: 0;
}
"""
