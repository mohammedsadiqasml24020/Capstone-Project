import os
import sys
import json
import numpy as np

# Ensure UTF-8 output encoding for Rupee standard (₹) on Windows terminals
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
from flask import Flask, render_template, request, jsonify, send_file, Response
from werkzeug.utils import secure_filename
from analytics_engine import BusinessAnalyticsEngine

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB max upload
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# Initialize Business Analytics Engine
engine = BusinessAnalyticsEngine(data_dir=app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class NumpyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer, np.floating, np.bool_)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

app.json_encoder = NumpyJSONEncoder

# Helper for safe JSON response
def safe_jsonify(data, status=200):
    json_str = json.dumps(data, cls=NumpyJSONEncoder)
    return Response(json_str, status=status, mimetype='application/json')

# ----------------- MAIN VIEW -----------------
@app.route('/')
def index():
    return render_template('index.html')

# ----------------- DATASET MANAGEMENT APIS -----------------
@app.route('/api/datasets', methods=['GET'])
def get_datasets():
    try:
        datasets = engine.list_datasets()
        return safe_jsonify({"status": "success", "datasets": datasets, "active": engine.active_dataset_name})
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

@app.route('/api/dataset/select', methods=['POST'])
def select_dataset():
    try:
        data = request.get_json() or {}
        filename = data.get('filename')
        if not filename:
            return safe_jsonify({"status": "error", "message": "Filename parameter is required"}, 400)
        overview = engine.load_dataset(filename)
        return safe_jsonify({"status": "success", "active_dataset": filename, "overview": overview})
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

@app.route('/api/dataset/upload', methods=['POST'])
def upload_dataset():
    try:
        if 'file' not in request.files:
            return safe_jsonify({"status": "error", "message": "No file part in upload request"}, 400)
        file = request.files['file']
        if file.filename == '':
            return safe_jsonify({"status": "error", "message": "No selected file"}, 400)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            # Switch engine active dataset
            overview = engine.load_dataset(filename)
            return safe_jsonify({
                "status": "success",
                "message": f"Successfully uploaded and activated {filename}",
                "active_dataset": filename,
                "overview": overview
            })
        else:
            return safe_jsonify({"status": "error", "message": "Invalid file type. Allowed: .csv, .xlsx, .xls"}, 400)
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

@app.route('/api/dataset/overview', methods=['GET'])
def dataset_overview():
    try:
        overview = engine.get_dataset_overview()
        return safe_jsonify(overview)
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

@app.route('/api/dataset/clean', methods=['POST'])
def clean_dataset():
    try:
        data = request.get_json() or {}
        missing_strategy = data.get('missing_strategy', 'mean')
        remove_duplicates = data.get('remove_duplicates', True)
        res = engine.clean_dataset(missing_strategy=missing_strategy, remove_duplicates=remove_duplicates)
        return safe_jsonify(res)
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

@app.route('/api/dataset/reset', methods=['POST'])
def reset_dataset():
    try:
        res = engine.reset_dataset()
        return safe_jsonify({"status": "success", "overview": res})
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

@app.route('/api/dataset/export/csv', methods=['GET'])
def export_csv():
    try:
        csv_bytes = engine.export_csv_bytes()
        filename = f"cleaned_{engine.active_dataset_name or 'dataset.csv'}"
        if not filename.endswith('.csv'):
            filename = filename.rsplit('.', 1)[0] + '.csv'
        return Response(
            csv_bytes,
            mimetype="text/csv",
            headers={"Content-disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

@app.route('/api/dataset/export/excel', methods=['GET'])
def export_excel():
    try:
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], f"_temp_export_{engine.active_dataset_name}.xlsx")
        engine.export_excel_path(temp_path)
        return send_file(
            temp_path,
            as_attachment=True,
            download_name=f"analytics_report_{engine.active_dataset_name.split('.')[0]}.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

# ----------------- MODULE 1: OVERVIEW DASHBOARD -----------------
@app.route('/api/analytics/overview', methods=['GET'])
def analytics_overview():
    try:
        data = engine.get_overview_analytics()
        return safe_jsonify({"status": "success", "data": data, "active_dataset": engine.active_dataset_name})
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

# ----------------- MODULE 3: SALES ANALYTICS -----------------
@app.route('/api/analytics/sales', methods=['GET'])
def analytics_sales():
    try:
        date_from = request.args.get('from')
        date_to = request.args.get('to')
        data = engine.get_sales_analytics(date_from=date_from, date_to=date_to)
        return safe_jsonify(data)
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

# ----------------- MODULE 4: PRODUCT ANALYTICS -----------------
@app.route('/api/analytics/products', methods=['GET'])
def analytics_products():
    try:
        data = engine.get_product_analytics()
        return safe_jsonify(data)
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

# ----------------- MODULE 5: PROFIT ANALYTICS -----------------
@app.route('/api/analytics/profit', methods=['GET'])
def analytics_profit():
    try:
        data = engine.get_profit_analytics()
        return safe_jsonify(data)
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

# ----------------- MODULE 6: AI BUSINESS INSIGHTS & ASK AI -----------------
@app.route('/api/ai/insights', methods=['GET'])
def ai_insights():
    try:
        data = engine.generate_ai_insights()
        return safe_jsonify(data)
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

@app.route('/api/ai/ask', methods=['POST'])
def ai_ask():
    try:
        payload = request.get_json() or {}
        question = payload.get('question', '')
        if not question:
            return safe_jsonify({"status": "error", "message": "Question is required"}, 400)
        res = engine.ask_ai(question)
        return safe_jsonify({"status": "success", "result": res})
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

# ----------------- MODULE 7: REPORTS & EXPORT -----------------
@app.route('/api/reports/analytical', methods=['GET'])
def analytical_report():
    try:
        data = engine.generate_analytical_report()
        return safe_jsonify({"status": "success", "report": data})
    except Exception as e:
        return safe_jsonify({"status": "error", "message": str(e)}, 500)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"===============================================================")
    print(f"🚀 AI-Powered Business Analytics Platform")
    print(f"🌐 Server running at: http://127.0.0.1:{port}")
    print(f"📂 Active Dataset: {engine.active_dataset_name}")
    print(f"===============================================================")
    app.run(host='0.0.0.0', port=port, debug=False)
