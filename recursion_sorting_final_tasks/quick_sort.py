# ID = 81771506
from typing import List


def compare(person1, person2):  # if person1 better than person 2
    if int(person1[1]) == int(person2[1]):  # wins equals
        if int(person1[2]) == int(person2[2]):  # errors equals
            return person1[0] <= person2[0]  # name earlier in alphabet
        return int(person1[2]) < int(person2[2])
    return int(person1[1]) > int(person2[1])


def partition(data, left: int, right: int):
    pivot = data[(left + right) // 2]

    while left <= right:

        while not compare(data[left], pivot):
            left += 1

        while not compare(pivot, data[right]):
            right -= 1

        if left >= right:
            break
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

    return data, right


def quick_sort(data, left: int, right: int):
    if left < right:
        data, pivot = partition(data, left, right)
        data = quick_sort(data, left, pivot)
        data = quick_sort(data, pivot + 1, right)
    return data


def main() -> None:
    amount: int = int(input())
    data: List[list] = [input().split() for _ in range(amount)]
    quick_sort(data, 0, amount - 1)
    for d in reversed(data):
        print(d[0])


if __name__ == '__main__':
    main()
