# Data Cleaning & Reporting Automation

## Overview
This project demonstrates how Python can be used to automate data cleaning, transformation, and reporting workflows. It processes a raw dataset, removes duplicate and inconsistent records, fills missing values, and generates a clean report with summary metrics and dashboard-style output.

The project is designed to showcase practical data preparation skills and reporting automation for business analysis tasks.

## Date
Created on: 2026-09-02

## Project Objective
The main goal of this project is to automate the process of cleaning messy raw data and preparing it for reporting. This helps reduce manual effort, improve data quality, and create faster and more reliable business reporting.

## Key Features
- Data cleaning and preprocessing using Python
- Handling missing values
- Removing duplicate records
- Standardizing inconsistent entries
- Converting raw sales data into a clean dataset
- Generating Excel-based reporting output
- Producing a Power BI-friendly summary file
- Creating a browser dashboard for easy viewing

## Tools and Technologies Used
- Python
- CSV data handling
- OpenPyXL for Excel automation
- Dashboard HTML output for browser-based reporting
- Microsoft Excel for report viewing
- Power BI-ready data export

## Project Workflow
1. Load raw sales data from a CSV file
2. Identify duplicates and inconsistent values
3. Clean and normalize fields such as names, products, dates, and regions
4. Save the cleaned dataset
5. Generate summary metrics and Excel dashboard
6. Prepare Power BI-friendly export data
7. Publish a browser-friendly dashboard view

## Folder Structure
- `data/` - contains the raw dataset
- `output/` - contains generated reports and outputs
- `scripts/` - contains the Python automation script
- `tests/` - contains validation tests
- `dashboard.html` - browser dashboard output
- `README.md` - project documentation

## Data Description
The project uses a sample sales dataset that includes fields such as:
- Order ID
- Customer Name
- Region
- Product
- Sales Amount
- Order Date
- Status
- Quantity
- City

## Data Cleaning Tasks Performed
- Removed duplicate rows
- Filled missing values with sensible defaults
- Standardized capital letters and spacing
- Normalized date formats
- Converted inconsistent text to a consistent format
- Cleaned product and city fields
- Handled missing statuses and invalid numerical values

## Output Files
After running the automation, the following files are generated:

- `output/cleaned_sales_data.csv` - cleaned data export
- `output/report_summary.xlsx` - Excel summary dashboard
- `output/powerbi_sales_summary.csv` - Power BI-ready summary data
- `output/visual_summary.txt` - human-readable summary text
- `dashboard.html` - HTML dashboard for easy viewing in a browser

## How to Run the Project
1. Open a terminal in the project folder.
2. Activate the virtual environment if needed.
3. Run the following command:

```bash
python scripts/clean_and_report.py
```

## How to View the Dashboard
You can open the generated dashboard in a browser:

- `dashboard.html`
- `output/dashboard.html`

The HTML dashboard is useful for GitHub-like preview and browser-based presentation.

## Expected Outcome
This project demonstrates how automation can improve the quality and usability of raw business data while reducing time spent on repetitive reporting tasks.

It helps in understanding:
- Data preprocessing
- Data validation and cleaning
- Automation in reporting
- Business intelligence preparation
- Reporting efficiency

## Benefits
- Saves time on manual data cleaning
- Reduces reporting errors
- Improves data quality and consistency
- Helps convert raw data into meaningful dashboard insights
- Makes reporting more efficient and scalable

## Author
Author: Soundarya Umesh Barigidad,

Information Science Engineering Student
