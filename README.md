# Data Cleaning & Reporting Automation

This project demonstrates an automated data cleaning and reporting workflow using Python. It reads a raw sales dataset, cleans missing values and duplicate records, standardizes inconsistent text, and generates a summary report with visuals.

## Features
- Missing value handling
- Duplicate removal
- Standardized text and date formatting
- Automated Excel report generation
- Clean summary chart and KPI output

## Project structure
- `data/raw_sales_data.csv` – sample raw data
- `scripts/clean_and_report.py` – data cleaning and reporting logic
- `output/cleaned_sales_data.csv` – cleaned dataset
- `output/report_summary.xlsx` – Excel summary report
- `output/visual_summary.png` – chart summary

## Run the project
```bash
python scripts/clean_and_report.py
```

## Open the dashboard
After running the script, open the generated browser dashboard here:
- `dashboard.html` in the project root
- `output/dashboard.html` in the output folder

This HTML version is suitable for browser preview and GitHub-style sharing links.

## Expected outcome
The script will:
1. Load the raw data
2. Clean the dataset
3. Save the cleaned output
4. Generate an Excel report, Power BI summary, and a browser dashboard

## Author
**Soundarya Umesh Barigidad**
Information Science Engineering Student
