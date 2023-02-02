def main() -> None:
    from math import sqrt

    res = []
    number = int(input())
    dev = 2
    while dev <= int(sqrt(number)):
        if number % dev == 0:
            res.append(dev)
            number = number // dev
        else:
            dev += 1
    res.append(number)
    print(*res, sep=" ")


if __name__ == '__main__':
    main()
