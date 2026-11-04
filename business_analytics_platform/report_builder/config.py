import os, sys, base64

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r"C:\Users\Sadiq\.gemini\antigravity\scratch\business_analytics_platform"
docs_dir = os.path.join(base_dir, "docs")

def get_b64(fname):
    p = os.path.join(docs_dir, fname)
    if os.path.exists(p):
        return "data:image/png;base64," + base64.b64encode(open(p, "rb").read()).decode("utf-8")
    return ""

def wrap_page(content, page_num_html=""):
    return f"""<div class="page">
    <div class="page-content">
        {content}
    </div>
    {page_num_html}
</div>
"""
