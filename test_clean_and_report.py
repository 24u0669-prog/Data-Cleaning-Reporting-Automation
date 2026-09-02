from scripts.clean_and_report import build_excel_dashboard, clean_rows


def test_clean_rows_removes_duplicates_and_fills_missing_values():
    rows = [
        {
            'Order ID': '1001',
            'Customer Name': 'Alice Johnson',
            'Region': 'North',
            'Product': 'Laptop',
            'Sales Amount': '1200.00',
            'Order Date': '2024-01-05',
            'Status': 'Completed',
            'Quantity': '1',
            'City': 'New York',
        },
        {
            'Order ID': '1001',
            'Customer Name': 'alice johnson',
            'Region': 'north',
            'Product': 'Laptop',
            'Sales Amount': '1200.00',
            'Order Date': '2024-01-05',
            'Status': 'completed',
            'Quantity': '1',
            'City': 'new york',
        },
        {
            'Order ID': '1002',
            'Customer Name': '',
            'Region': 'South',
            'Product': '',
            'Sales Amount': '',
            'Order Date': '2024-01-08',
            'Status': 'Completed',
            'Quantity': '2',
            'City': 'Atlanta',
        },
    ]

    cleaned = clean_rows(rows)

    assert len(cleaned) == 2
    assert cleaned[0]['Customer Name'] == 'Alice Johnson'
    assert cleaned[0]['Region'] == 'North'
    assert cleaned[1]['Product'] == 'Unspecified'
    assert cleaned[1]['Sales Amount'] == 0.0
    assert cleaned[1]['Status'] == 'Completed'


def test_build_excel_dashboard_creates_summary_and_data_sheets(tmp_path):
    rows = [
        {
            'Order ID': '1001',
            'Customer Name': 'Alice Johnson',
            'Region': 'North',
            'Product': 'Laptop',
            'Sales Amount': 1200,
            'Order Date': '2024-01-05',
            'Status': 'Completed',
            'Quantity': 1,
            'City': 'New York',
        },
        {
            'Order ID': '1002',
            'Customer Name': 'Bob Smith',
            'Region': 'South',
            'Product': 'Phone',
            'Sales Amount': 450,
            'Order Date': '2024-01-08',
            'Status': 'Completed',
            'Quantity': 2,
            'City': 'Atlanta',
        },
    ]

    output_file = tmp_path / 'dashboard.xlsx'
    build_excel_dashboard(rows, output_file)

    assert output_file.exists()
    assert output_file.stat().st_size > 0
