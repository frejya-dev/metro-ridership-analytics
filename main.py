from pathlib import Path

from src.loader import load_data
from src.analyzer import calculate_summary
from src.charts import create_monthly_ridership_chart


def format_number(value):
    return f"{value:,.0f}"


def main():
    file_path = "data/raw/systemwide_ridership.csv"
    chart_path = "output/charts/monthly_ridership.png"

    metro_data = load_data(file_path)
    summary = calculate_summary(metro_data)

    Path("output/charts").mkdir(parents=True, exist_ok=True)

    create_monthly_ridership_chart(metro_data, chart_path)

    print("=" * 50)
    print("LA Metro Data Analytics")
    print("=" * 50)

    print("\nDataset loaded successfully.")
    print(f"\nRecords: {summary['records']}")

    print(f"\nTotal Ridership: {format_number(summary['total_ridership'])}")
    print(f"Average Monthly Ridership: {format_number(summary['average_monthly'])}")

    print(
        f"\nHighest Month: {summary['highest_month']} "
        f"({format_number(summary['highest_value'])})"
    )
    print(
        f"Lowest Month: {summary['lowest_month']} "
        f"({format_number(summary['lowest_value'])})"
    )

    print(
        f"\nLatest Month: {summary['latest_month']} "
        f"({format_number(summary['latest_value'])})"
    )
    print(f"Month-over-Month Change: {summary['monthly_change']:.1f}%")

    print(f"\nChart saved to: {chart_path}")


if __name__ == "__main__":
    main()