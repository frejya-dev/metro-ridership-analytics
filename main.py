from pathlib import Path

from src.analyzer import calculate_summary
from src.charts import create_monthly_ridership_chart
from src.loader import load_data
from src.pdf_report import generate_pdf_report
from src.reporter import generate_summary_report


def format_number(value):
    return f"{value:,.0f}"


def main():
    file_path = "data/raw/systemwide_ridership.csv"
    chart_path = "output/charts/monthly_ridership.png"
    report_path = "output/reports/summary.txt"
    pdf_path = "output/reports/ridership_report.pdf"

    Path("output/charts").mkdir(parents=True, exist_ok=True)
    Path("output/reports").mkdir(parents=True, exist_ok=True)

    metro_data = load_data(file_path)
    summary = calculate_summary(metro_data)

    create_monthly_ridership_chart(metro_data, chart_path)
    generate_summary_report(summary, report_path)
    generate_pdf_report(summary, chart_path, pdf_path)

    print("=" * 50)
    print("LA Metro Ridership Analytics")
    print("=" * 50)

    print("\nDataset")
    print("--------")
    print(f"Records analyzed:           {len(metro_data)}")
    print("Time period:                Apr 2025 - Mar 2026")

    print("\nKey Metrics")
    print("-----------")
    print(f"Total Ridership:            {format_number(summary['total'])}")
    print(f"Average Monthly:            {format_number(summary['average'])}")

    print("\nHighlights")
    print("----------")
    print(
        f"Highest Ridership:          {summary['highest_month']} "
        f"({format_number(summary['highest_value'])})"
    )
    print(
        f"Lowest Ridership:           {summary['lowest_month']} "
        f"({format_number(summary['lowest_value'])})"
    )

    print("\nLatest Month")
    print("------------")
    print(
        f"{summary['latest_month']}:                 "
        f"{format_number(summary['latest_value'])}"
    )
    print(f"Month-over-Month Change:    {summary['mom_change']:+.1f}%")

    print("\nGenerated Files")
    print("---------------")
    print(f"✓ {chart_path}")
    print(f"✓ {report_path}")
    print(f"✓ {pdf_path}")


if __name__ == "__main__":
    main()