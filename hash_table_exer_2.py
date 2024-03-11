def main():
    with open("nyc_weather.csv", "r") as file:
        data = file.read()
    data_split = data.split("\n")

    data_dict = {}

    for i in range(1, len(data_split)):
        data_dict[data_split[i].split(",")[0]] = data_split[i].split(",")[1]

    print(f"Temperature on Jan 9 is: {data_dict['Jan 9']}")
    print(f"Temperature on Jan 4 is: {data_dict['Jan 4']}")


if __name__ == '__main__':
    main()