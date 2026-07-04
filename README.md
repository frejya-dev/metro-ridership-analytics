# LA Metro Ridership Analytics

A Python analytics application that loads, analyzes, and visualizes Los Angeles Metro ridership data.

## Overview

This project demonstrates a simple end-to-end analytics workflow using Python. It reads monthly Metro ridership data from a CSV file, calculates key performance metrics, generates a publication-ready chart, and exports both a text summary and a PDF report.

The project is intentionally organized into reusable modules to reflect a real-world analytics codebase rather than a single script.

## Features

- Load CSV data with pandas
- Calculate summary statistics
- Identify highest and lowest ridership months
- Calculate month-over-month change
- Generate a professional bar chart using Matplotlib
- Export a text summary report
- Export a PDF report using ReportLab

## Project Structure

```
metro-ridership-analytics/
│
├── data/
│   └── raw/
│       └── systemwide_ridership.csv
│
├── output/
│   ├── charts/
│   └── reports/
│
├── src/
│   ├── loader.py
│   ├── analyzer.py
│   ├── charts.py
│   ├── reporter.py
│   └── pdf_report.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Technologies

- Python
- pandas
- matplotlib
- ReportLab

## Example Output

Running

```bash
python main.py
```

generates:

- Monthly ridership chart
- Text analytics report
- PDF summary report

## Future Improvements

- Interactive dashboard
- Trend analysis
- Moving averages
- Ridership forecasting
- Additional visualizations

## Author

Frejya Lindh