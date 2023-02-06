def calc(id, amount_print):
    res = {}
    for i in sorted(id):
        if i not in res:
            res[i] = 1
        else:
            res[i] +=1
    return dict(sorted(res.items(), reverse=True, key=lambda x: x[1])[:int(amount_print)])


def main() -> None:
    input()
    id = input().split()
    amount_print = input()
    print(*calc(id, amount_print).keys())


if __name__ == '__main__':
    main()
