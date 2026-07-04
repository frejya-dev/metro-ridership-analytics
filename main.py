from src.loader import load_data


def main():
    file_path = "data/raw/systemwide_ridership.csv"

    metro_data = load_data(file_path)

    print("\nMetro Ridership Dataset\n")
    print(metro_data)


if __name__ == "__main__":
    main()