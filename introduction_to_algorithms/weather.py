def main() -> None:
    input()
    weather_data = list(map(int, input().split(" ")))
    res = 0
    i = 0
    data = [weather_data[0] - 1]
    data += weather_data
    data.append(weather_data[len(weather_data) - 1] - 1)
    while i < len(data):
        if (data[i] > data[i - 1]) and (data[i] > data[i + 1]):
            res += 1
        i += 1

    print(res)


if __name__ == '__main__':
    main()
