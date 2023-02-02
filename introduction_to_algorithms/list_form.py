def main() -> None:
    input()
    list_form = int(input().replace(" ", "")) + int(input())
    res = ""
    for i in str(list_form):
        i += " "
        res += i
    print(res.strip())


if __name__ == '__main__':
    main()
