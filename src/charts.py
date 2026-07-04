import matplotlib.pyplot as plt


def create_monthly_ridership_chart(df, output_path):
    plt.figure(figsize=(10, 5))

    bars = plt.bar(
        df["Month"],
        df["Total Ridership"],
        color="#7057d8",
        edgecolor="#7057d8",
    )

    bars[-1].set_color("#1f5fd1")

    plt.title("Metro Ridership", fontsize=18, fontweight="bold", loc="left")
    plt.subtitle = None

    plt.ylabel("Total Ridership")
    plt.xticks(rotation=45, ha="right")

    plt.grid(axis="y", alpha=0.2)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()