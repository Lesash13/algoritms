def calc(amount, opened_brackets):
    res = []

    if amount == 0 == opened_brackets:
        return ['']

    if amount != 0:
        a = calc(amount - 1, opened_brackets + 1)
        a[:] = [f'({el}' for el in a]
        res += a

    if opened_brackets != 0:
        b = calc(amount, opened_brackets - 1)
        b[:] = [f'){el}' for el in b]
        res += b
    return res


def main() -> None:
    amount = int(input())
    print(*calc(amount, 0), sep='\n')


if __name__ == '__main__':
    main()
