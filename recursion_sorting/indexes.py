
def main() -> None:
    amount = int(input())
    inp = list(map(int, input().split()))
    k = int(input())
    res = [None] * (amount * (amount - 1) // 2)
    index: int = 0
    if len(inp) == 2:
        print(abs(inp[0] - inp[1]))
    else:
        for i in range(0, amount - 1):
            for j in range(i + 1, amount):
                res[index] = (abs(inp[i] - inp[j]))
                index += 1
        res.sort()

        print(res[k - 1])


if __name__ == '__main__':
    main()
