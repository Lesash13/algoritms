def main() -> None:
    a, x, b, c = map(int, input().split())
    y = a * x * x + b * x + c
    print(y)


if __name__ == '__main__':
    main()