def main() -> None:
    amount = int(input())
    inp = [map(int, input().split()) for _ in range(amount)]
    data = sorted([t for t in (set(tuple(i) for i in inp))])
    res = []
    start = data[0][0]
    end = data[0][1]
    for i in range(0, len(data) - 1):
        if data[i + 1][0] > end:  # 1
            res.append([start, end])
            start = data[i + 1][0]
            end = data[i + 1][1]
        else:
            if data[i + 1][1] <= end:
                continue  # 2
            else:
                end = data[i + 1][1]  # 3
    res.append([start, end])
    for i in res:
        print(*i, sep=' ')


if __name__ == '__main__':
    main()
