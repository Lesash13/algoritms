def main() -> None:
    number = int(input())
    result = ""
    if number == 0:
        print(number)
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    print(result)


if __name__ == '__main__':
    main()
