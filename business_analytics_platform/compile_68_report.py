import os, sys

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from report_builder.styles import CSS
from report_builder.preliminary import get_preliminary_pages
from report_builder.chapters_1_3 import get_chapters_1_to_3
from report_builder.chapter_4 import get_chapter_4
from report_builder.chapter_5 import get_chapter_5
from report_builder.chapter_6 import get_chapter_6
from report_builder.chapters_7_9 import get_chapters_7_to_9

def main():
    base_dir = r"C:\Users\Sadiq\.gemini\antigravity\scratch\business_analytics_platform"
    docs_dir = os.path.join(base_dir, "docs")
    os.makedirs(docs_dir, exist_ok=True)

    app_lines = open(os.path.join(base_dir, "app.py"), "r", encoding="utf-8").readlines()
    eng_lines = open(os.path.join(base_dir, "analytics_engine.py"), "r", encoding="utf-8").readlines()

    all_pages = []

    # 1. Prelims (Pages 1-8)
    p_prelim = get_preliminary_pages()
    print(f"Prelims: {len(p_prelim)} pages")
    all_pages.extend(p_prelim)

    # 2. Chapters 1 to 3 (Pages 9-17)
    p_1_3 = get_chapters_1_to_3()
    print(f"Chapters 1-3: {len(p_1_3)} pages")
    all_pages.extend(p_1_3)

    # 3. Chapter 4 (Pages 18-21)
    p_4 = get_chapter_4()
    print(f"Chapter 4: {len(p_4)} pages")
    all_pages.extend(p_4)

    # 4. Chapter 5 (Pages 22-29)
    p_5 = get_chapter_5()
    print(f"Chapter 5: {len(p_5)} pages")
    all_pages.extend(p_5)

    # 5. Chapter 6 (Pages 30-51)
    p_6 = get_chapter_6(app_lines, eng_lines)
    print(f"Chapter 6: {len(p_6)} pages")
    all_pages.extend(p_6)

    # 6. Chapters 7 to 9 & References (Pages 52-68)
    p_7_9 = get_chapters_7_to_9()
    print(f"Chapters 7-9: {len(p_7_9)} pages")
    all_pages.extend(p_7_9)

    print(f"TOTAL PAGES COMPILED: {len(all_pages)}")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI-Based Business Analytics Dashboard - Capstone Project Report (68 Pages)</title>
    <style>
        {CSS}
    </style>
</head>
<body>
    {''.join(all_pages)}
</body>
</html>
"""
    output_html_path = os.path.join(docs_dir, "capstone_report_68.html")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[SUCCESS] Wrote 68-page report HTML to: {output_html_path}")

if __name__ == "__main__":
    main()
