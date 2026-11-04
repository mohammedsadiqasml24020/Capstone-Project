# Generator for exact 68-page report
import os
import sys
import base64
import html

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'C:\Users\Sadiq\.gemini\antigravity\scratch\business_analytics_platform'
docs_dir = os.path.join(base_dir, 'docs')
os.makedirs(docs_dir, exist_ok=True)

# Helper to load image as base64 data URI
def get_b64(filename):
    path = os.path.join(docs_dir, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')
    return ''

print('Ready to build script')
