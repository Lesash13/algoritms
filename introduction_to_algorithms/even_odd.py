def main() -> None:
    a, b, c = map(int, input().split())
    if ((a % 2 == 1) and (b % 2 == 1) and (c % 2 == 1)) or ((a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)):
        print('WIN')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()
