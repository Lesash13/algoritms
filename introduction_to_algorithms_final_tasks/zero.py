# ID = 81771506
from typing import List


def count_index(length, street, zero_indexes) -> List[int]:
    res: List[int] = [0] * length
    previous_value_res: int = 0
    for i in range(0, length):
        if street[i] == 0:
            res[i] = 0
            continue
        nearest: int = abs(i - zero_indexes[0])
        if len(zero_indexes) == 1:
            res[i] = nearest
            continue
        for j in range(previous_value_res, len(zero_indexes)):
            min_value: int = abs(i - zero_indexes[j])
            if min_value < nearest:
                nearest = min_value
                previous_value_res = j
            if min_value > nearest:
                break

        res[i] = nearest
    return res


def zero_index_list(street: List[int]) -> List[int]:
    return [i for i, val in enumerate(street) if val == 0]


def main() -> None:
    length: int = int(input())
    street: List[int] = [int(i) for i in input().split()]
    print(*count_index(length, street, zero_index_list(street)), sep=" ")


if __name__ == '__main__':
    main()
