import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


METRO_BLUE = "#0054A6"
METRO_PURPLE = "#7257D8"
METRO_PURPLE_DARK = "#4B35A8"
LIGHT_GRAY = "#CCCCCC"
TEXT_GRAY = "#666666"
TEXT_BLACK = "#111111"


def format_millions(value, position):
    return f"{value / 1_000_000:.0f}M"


def create_monthly_ridership_chart(df, output_path):
    plt.figure(figsize=(12, 6))

    highest_index = df["Total Ridership"].idxmax()
    latest_index = len(df) - 1

    colors = [METRO_PURPLE] * len(df)
    colors[highest_index] = METRO_PURPLE_DARK
    colors[latest_index] = METRO_BLUE

    plt.bar(
        df["Month"],
        df["Total Ridership"],
        color=colors,
        edgecolor=colors,
        width=0.72,
    )

    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(format_millions))

    ax.set_title(
        "Metro Ridership",
        fontsize=22,
        fontweight="bold",
        color=TEXT_BLACK,
        loc="left",
        pad=28,
    )

    plt.text(
        0,
        1.02,
        "Systemwide Monthly Boardings (Apr 2025 – Mar 2026)",
        transform=ax.transAxes,
        fontsize=11,
        color=TEXT_GRAY,
    )

    plt.ylabel("Total Ridership", fontsize=11, labelpad=18,)
    plt.xticks(rotation=45, ha="right")

    plt.grid(axis="y", alpha=0.18)
    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(LIGHT_GRAY)
    ax.spines["bottom"].set_color(LIGHT_GRAY)

    latest_month = df.iloc[latest_index]

    plt.text(
        latest_index,
        latest_month["Total Ridership"] + 300000,
        f"{latest_month['Total Ridership'] / 1_000_000:.1f}M",
        ha="center",
        fontsize=10,
        fontweight="bold",
        color=METRO_BLUE,
    )

    highest_month = df.iloc[highest_index]

    plt.text(
        highest_index,
        highest_month["Total Ridership"] + 300000,
        "Highest",
        ha="center",
        fontsize=10,
        fontweight="bold",
        color=METRO_PURPLE_DARK,
    )

    plt.tight_layout()
    plt.subplots_adjust(top=0.86)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()