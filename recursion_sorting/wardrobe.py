def calc(values):
    d = {'0': 0, '1': 0, '2': 0}

    if values > 0:
        for color in input().split(' '):
            d[color] += 1

    return '0 ' * d['0'] + '1 ' * d['1'] + '2 ' * d['2']


def main() -> None:
    values = int(input())
    print(calc(values))


if __name__ == '__main__':
    main()
