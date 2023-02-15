def main() -> None:
    happy = 0
    children = int(input())
    needs = sorted(list(map(int, input().split())), reverse=True)
    cookies = int(input())
    cookies_size = sorted(list(map(int, input().split())))
    for i in range(children):
        if cookies_size and needs[i] <= cookies_size[-1]:
            cookies_size.pop()
            happy += 1
    print(happy)


if __name__ == '__main__':
    main()
