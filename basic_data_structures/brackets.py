def check(values):
    for _ in values:
        values = values.replace('()', '')
        values = values.replace('[]', '')
        values = values.replace('{}', '')
    return not values


def main() -> None:
    values = input()
    print(check(values))


if __name__ == '__main__':
    main()
