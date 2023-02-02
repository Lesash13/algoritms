def main() -> None:
    a = int(input(), 2)
    b = int(input(), 2)
    print(str(bin(a + b))[2::])


if __name__ == '__main__':
    main()
