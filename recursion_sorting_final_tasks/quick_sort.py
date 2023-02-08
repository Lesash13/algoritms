# ID = 82011367
from typing import List


def partition(data: List[list], left: int, right: int) -> (List[list], int):
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


def values_conversion(data) -> List[list]:
    return [-int(data[1]), int(data[2]), data[0]]


def quick_sort(data: List[list], left: int, right: int):
    if left < right:
        data, pivot = partition(data, left, right)
        data = quick_sort(data, left, pivot)
        data = quick_sort(data, pivot + 1, right)
    return data


def main() -> None:
    amount: int = int(input())
    data: List[list] = [values_conversion(input().split()) for _ in range(amount)]
    quick_sort(data, 0, amount - 1)
    print(*(list(zip(*data))[2]), sep="\n")


if __name__ == '__main__':
    main()
