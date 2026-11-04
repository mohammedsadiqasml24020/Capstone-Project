# Full 68-page report builder
import os, sys, base64, html

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'C:\Users\Sadiq\.gemini\antigravity\scratch\business_analytics_platform'
docs_dir = os.path.join(base_dir, 'docs')

def get_b64(fname):
    p = os.path.join(docs_dir, fname)
    if os.path.exists(p):
        return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode('utf-8')
    return ''

print('Reading code files...')
app_lines = open(os.path.join(base_dir, 'app.py'), 'r', encoding='utf-8').readlines()
eng_lines = open(os.path.join(base_dir, 'analytics_engine.py'), 'r', encoding='utf-8').readlines()
print('Read OK')
