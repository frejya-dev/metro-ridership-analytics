def calculate_summary(df):
    total_ridership = df["Total Ridership"].sum()
    average_monthly = df["Total Ridership"].mean()

    highest_month = df.loc[df["Total Ridership"].idxmax()]
    lowest_month = df.loc[df["Total Ridership"].idxmin()]

    latest_month = df.iloc[-1]
    previous_month = df.iloc[-2]

    monthly_change = (
        (latest_month["Total Ridership"] - previous_month["Total Ridership"])
        / previous_month["Total Ridership"]
    ) * 100

    return {
        "records": len(df),
        "total_ridership": total_ridership,
        "average_monthly": average_monthly,
        "highest_month": highest_month["Month"],
        "highest_value": highest_month["Total Ridership"],
        "lowest_month": lowest_month["Month"],
        "lowest_value": lowest_month["Total Ridership"],
        "latest_month": latest_month["Month"],
        "latest_value": latest_month["Total Ridership"],
        "monthly_change": monthly_change,
    }