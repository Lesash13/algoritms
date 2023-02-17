def can_sort(part: list, max_num):
    res = True
    part.sort()
    index = 0
    for i in range(max_num-len(part) + 1, max_num):
        if part[index] != i:
            res = False
            break
        index += 1
    return res


def main() -> None:
    amount = int(input())
    arr = [int(num) for num in input().split(' ')]
    blocks = 0
    part = []

    for i in range(0, amount):
        if i == arr[i] and len(part) == 0:
            blocks += 1
            continue
        else:
            part.append(arr[i])
            if len(part) == 1:
                continue
            if can_sort(part, i):
                blocks += 1
                i += len(part)
                part = []
                continue

    print(blocks)


if __name__ == '__main__':
    main()
