# ID = 81738655

def count_index(length, street, zero_indexes) -> list:
    res: list = []
    previous_value_res: int = 0
    for i in range(0, length):
        if street[i] == 0:
            res.append(0)
            continue
        nearest: int = abs(i - zero_indexes[0])
        if len(zero_indexes) == 1:
            res.append(nearest)
            continue
        for j in range(previous_value_res, len(zero_indexes)):
            min_value: int = abs(i - zero_indexes[j])
            if min_value < nearest:
                nearest = min_value
                previous_value_res = j
            if min_value > nearest:
                break

        res.append(nearest)
    return res


def zero_index_list(street: list) -> list:
    return [i for i, val in enumerate(street) if val == 0]


def main() -> None:
    length: int = int(input())
    street: list = list(map(int, input().split()))
    print(*count_index(length, street, zero_index_list(street)), sep=" ")


if __name__ == '__main__':
    main()
