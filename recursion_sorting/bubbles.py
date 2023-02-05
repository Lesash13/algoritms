def calc(amount, values):
    was_changed = False
    while True:
        cycle = False
        for i in range(0, amount - 1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                cycle = True
                was_changed = True
        if cycle:
            print(*values)
        else:
            break
    if not was_changed:
        print(*values)


def main() -> None:
    amount = int(input())
    values = [int(num) for num in input().split(' ')]
    calc(amount, values)


if __name__ == '__main__':
    main()
