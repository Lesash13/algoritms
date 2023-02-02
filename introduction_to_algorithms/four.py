def main() -> None:
    res = False
    number = int(input())
    if number == 1:
        res = True
    if number == 4:
        res = True
    while number > 4:
        if number % 4 >= 1:
            break
        number = number / 4
        if number == 4:
            res = True

    print(res)


if __name__ == '__main__':
    main()
