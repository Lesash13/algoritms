def calc(days_size, days, amount):
    i = 0
    while i < days_size:
        if days[i] >= amount:
            return str(i + 1)
        i += 1
    return str(-1)


def main() -> None:
    days_size = int(input())
    days = [int(num) for num in input().split(' ')]
    amount = int(input())
    print(" ".join([calc(days_size, days, amount), calc(days_size, days, amount * 2)]))


if __name__ == '__main__':
    main()
