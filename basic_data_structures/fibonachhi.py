def main() -> None:
    def fibonacci(n):
        if n in [0, 1]:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    print(fibonacci(int(input())))


if __name__ == '__main__':
    main()
