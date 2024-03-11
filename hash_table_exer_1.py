def main():
    with open("nyc_weather.csv", "r") as file:
        data = file.read()

    data_split = data.split("\n")

    data_list = []
    for i in range(1, len(data_split)):
        data_list.append(data_split[i].split(",")[1])

    print(data_list)
    count = 0
    sum_temp = 0
    while count < 7:
        sum_temp += int(data_list[count])
        count += 1
    print(f"Average temperature in first wee of Jan is {round(float(sum_temp/7), 2)}")

    days = 0
    max_temp = 0
    while days < 10:
        if max_temp < int(data_list[days]):
            max_temp = int(data_list[days])
        days += 1

    print(f"Maximum temperature in first 10 days of Jan is {max_temp}")


if __name__ == '__main__':
    main()