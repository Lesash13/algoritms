def main() -> None:
    input()
    phrase = list(input().split(" "))
    res = ""
    for i in phrase:
        if len(res) < len(i):
            res = i
    print(res)
    print(len(res))


if __name__ == '__main__':
    main()
