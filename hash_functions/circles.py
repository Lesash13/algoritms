def counter(amount):
    res = {}
    for i in range(amount):
        res[input()] = ''

    print(*res.keys(), sep='\n')


def main() -> None:
    amount = int(input())

    counter(amount)


if __name__ == '__main__':
    main()
