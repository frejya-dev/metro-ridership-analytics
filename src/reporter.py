from pathlib import Path


def generate_summary_report(summary, output_path):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("LOS ANGELES METRO RIDERSHIP SUMMARY\n")
        file.write("=" * 38 + "\n\n")

        file.write("Dataset\n")
        file.write("-------\n")
        file.write("Source: LA Metro By the Numbers\n")
        file.write("Period: April 2025 – March 2026\n\n")

        file.write("Key Metrics\n")
        file.write("-----------\n")
        file.write(f"Total Ridership           : {summary['total']:,.0f}\n")
        file.write(f"Average Monthly Ridership : {summary['average']:,.0f}\n")
        file.write(
            f"Highest Month             : {summary['highest_month']} "
            f"({summary['highest_value']:,.0f})\n"
        )
        file.write(
            f"Lowest Month              : {summary['lowest_month']} "
            f"({summary['lowest_value']:,.0f})\n"
        )
        file.write(
            f"Latest Month              : {summary['latest_month']} "
            f"({summary['latest_value']:,.0f})\n"
        )
        file.write(f"Month-over-Month Change   : {summary['mom_change']:+.1f}%\n\n")

        file.write("Observations\n")
        file.write("------------\n")
        file.write("- Ridership remained relatively stable throughout the reporting period.\n")
        file.write(f"- {summary['highest_month']} recorded the highest monthly ridership.\n")
        file.write(
            f"- {summary['latest_month']} ended the period with "
            f"{summary['mom_change']:+.1f}% month-over-month change.\n"
        )

        file.write("\nGenerated automatically with Python.\n")