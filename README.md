# LA Metro Ridership Analytics

![Python](https://img.shields.io/badge/Python-3.12-blue)
![pandas](https://img.shields.io/badge/pandas-2.x-purple)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF-success)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

This project demonstrates an end-to-end analytics workflow built with Python. Monthly Los Angeles Metro ridership data is imported from a CSV file, analyzed to calculate key performance metrics, visualized with Matplotlib, and exported as both text and PDF reports.

The codebase is organized into reusable modules to reflect a real-world analytics application, separating data loading, analysis, visualization, and reporting into individual components.

## Features

- Import monthly ridership data with pandas
- Calculate key ridership metrics and summary statistics
- Identify highest and lowest ridership months
- Calculate month-over-month ridership change
- Generate a Metro-inspired bar chart using Matplotlib
- Export a formatted text summary
- Generate a PDF analytics report with ReportLab
- Organize functionality into reusable Python modules

## Technologies

- Python
- pandas
- Matplotlib
- ReportLab

## Installation

Clone the repository:

```bash
git clone https://github.com/frejya-dev/metro-ridership-analytics.git
cd metro-ridership-analytics
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Project Structure

```text
metro-ridership-analytics/
│
├── data/
│   └── raw/
│       └── systemwide_ridership.csv
│
├── output/
│   ├── charts/
│   │   └── monthly_ridership.png
│   └── reports/
│       ├── summary.txt
│       └── ridership_report.pdf
│
├── images/
│   └── chart-preview.png
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

## Output

Running the application automatically generates:

- Monthly ridership summary
- Professional bar chart (.png)
- Text report (.txt)
- PDF analytics report (.pdf)

## Sample Visualization

![Metro Ridership Chart](![Metro Ridership Chart](images/chart-preview.png))

The chart is generated automatically from the source dataset using Matplotlib. The highest ridership month and latest month are highlighted to provide a quick visual summary of recent ridership trends.

## Skills Demonstrated

- Data loading and transformation
- Exploratory data analysis
- Data visualization
- Automated report generation
- Modular Python application design
- File organization and project structure

## Future Improvements

- Interactive dashboard
- Additional Metro-style visualizations
- Rolling averages and trend analysis
- Ridership forecasting
- Data validation
- Automated testing
- Support for multiple datasets

## Author

**Frejya Lindh**

Web Developer | Digital Platforms | UX & Analytics
