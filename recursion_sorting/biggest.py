import sys


def calc(amount, values):
    for i in range(0, amount - 1):
        if (str(values[i]) + str(values[i + 1])) < (str(values[i + 1]) + str(values[i])):
            values[i], values[i + 1] = values[i + 1], values[i]
            return calc(amount, values)

    return values


def main() -> None:
    sys.setrecursionlimit(2800)
    amount = int(input())
    values = [int(num) for num in input().split(' ')]
    print(*calc(amount, values), sep='')


if __name__ == '__main__':
    main()
