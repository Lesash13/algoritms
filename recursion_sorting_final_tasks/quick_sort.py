# ID = 82112592
from typing import List, Tuple


def partition(data: List[Tuple], left: int, right: int) -> (List[Tuple], int):
    pivot = data[(left + right) // 2]

    while left <= right:

        while data[left] < pivot:
            left += 1

        while data[right] > pivot:
            right -= 1

        if left >= right:
            break

        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

    return data, right


def values_conversion(name: str, solved: str, errors: str) -> Tuple:
    return -int(solved), int(errors), name


def quick_sort(data: List[Tuple], left: int, right: int):
    if left < right:
        data, pivot = partition(data, left, right)
        data = quick_sort(data, left, pivot)
        data = quick_sort(data, pivot + 1, right)
    return data


def main() -> None:
    amount: int = int(input())
    data: List[Tuple] = [values_conversion(*input().split()) for _ in range(amount)]
    quick_sort(data, 0, amount - 1)
    print(*[user[2] for user in data], sep="\n")


if __name__ == '__main__':
    main()
