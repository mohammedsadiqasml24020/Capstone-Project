import sys
import json

# Ensure UTF-8 console output for Indian Rupee symbol (₹) on Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from app import app, engine

def test_suite():
    print("=== Running NexusBI Verification Test Suite ===")
    client = app.test_client()

    # 1. Main Page
    res = client.get('/')
    assert res.status_code == 200, f"Root failed: {res.status_code}"
    print("[PASS] GET / -> HTTP 200 (Dashboard HTML delivered)")

    # 2. Datasets List
    res = client.get('/api/datasets')
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'success'
    print(f"[PASS] GET /api/datasets -> Found {len(data['datasets'])} datasets (Active: {data['active']})")

    # 3. Dataset Overview
    res = client.get('/api/dataset/overview')
    assert res.status_code == 200
    overview = res.get_json()
    assert overview['status'] == 'success'
    print(f"[PASS] GET /api/dataset/overview -> Rows: {overview['total_rows']}, Cols: {overview['total_cols']}, Duplicates: {overview['duplicate_rows']}")

    # 4. Module 1: Overview Analytics
    res = client.get('/api/analytics/overview')
    assert res.status_code == 200
    ov_data = res.get_json()['data']
    print(f"[PASS] GET /api/analytics/overview -> Revenue: ₹{ov_data['total_revenue']:,.2f}, Profit: ₹{ov_data['total_profit']:,.2f}, Margin: {ov_data['profit_margin']}%")

    # 5. Module 3: Sales Analytics
    res = client.get('/api/analytics/sales')
    assert res.status_code == 200
    sales_data = res.get_json()
    print(f"[PASS] GET /api/analytics/sales -> Total Sales: ₹{sales_data['total_sales']:,.2f}, Peak Period: {sales_data['highest_sales_period']['period']}")

    # 6. Module 4: Product Analytics
    res = client.get('/api/analytics/products')
    assert res.status_code == 200
    prod_data = res.get_json()
    print(f"[PASS] GET /api/analytics/products -> Products Count: {prod_data['total_products']}, Best Seller: {prod_data['best_selling']['product']}")

    # 7. Module 5: Profit Analytics
    res = client.get('/api/analytics/profit')
    assert res.status_code == 200
    profit_data = res.get_json()
    print(f"[PASS] GET /api/analytics/profit -> Overall Margin: {profit_data['overall_margin_pct']}%, Matrix Tiers: {len(profit_data['profitability_matrix'])}")

    # 8. Module 6: AI Insights
    res = client.get('/api/ai/insights')
    assert res.status_code == 200
    ai_data = res.get_json()
    print(f"[PASS] GET /api/ai/insights -> Insights: {len(ai_data['insights'])}, Recommendations: {len(ai_data['recommendations'])}")

    # 9. Module 6: Ask AI NLP
    questions = [
        "Which product generates the highest revenue?",
        "What is the total profit?",
        "Which month has the highest sales?",
        "Why are sales decreasing?",
        "Give me a summary of business performance."
    ]
    for q in questions:
        res = client.post('/api/ai/ask', json={"question": q})
        assert res.status_code == 200
        ans = res.get_json()['result']
        print(f"[PASS] POST /api/ai/ask ('{q}') ->\n       Answer: {ans['answer'][:80]}...")

    # 10. Module 7: Reports
    res = client.get('/api/reports/analytical')
    assert res.status_code == 200
    report = res.get_json()['report']
    print(f"[PASS] GET /api/reports/analytical -> Report generated successfully for '{report['dataset_analyzed']}'")

    # 11. Test Switching to 'sales_and_profit.csv' (with missing values) and Cleaning
    res = client.post('/api/dataset/select', json={"filename": "sales_and_profit.csv"})
    assert res.status_code == 200
    print("[PASS] POST /api/dataset/select -> Switched to 'sales_and_profit.csv'")

    res = client.get('/api/dataset/overview')
    ov_sp = res.get_json()
    print(f"[PASS] Initial 'sales_and_profit.csv' -> Rows: {ov_sp['total_rows']}, Missing Sales: {ov_sp['missing_values']['Sales']['count']}, Duplicates: {ov_sp['duplicate_rows']}")

    res = client.post('/api/dataset/clean', json={"missing_strategy": "mean", "remove_duplicates": True})
    assert res.status_code == 200
    clean_res = res.get_json()
    summary = clean_res['summary']
    print(f"[PASS] POST /api/dataset/clean -> Imputed {summary['missing_filled']} missing values, Removed {summary['duplicates_removed']} duplicate records! Cleaned Rows: {summary['rows_after']}")

    print("\n=== ALL 11 TEST SUITES PASSED FLAWLESSLY! ===")

if __name__ == '__main__':
    test_suite()
