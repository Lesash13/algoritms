def main() -> None:
    n, k = map(int, input().split())
    n1, n2 = 1, 1
    if n in [0, 1]:
        res = 1
    else:
        for _ in range(int(n) - 1):
            n1, n2 = n2, (n2 + n1) % 10 ** k
        res = n2

    print(res)


if __name__ == '__main__':
    main()
