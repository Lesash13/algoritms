# ID = 81771304
from typing import List


def count_points(can_press_each, values) -> int:
    amount_per_digit: List[int] = [0] * 10
    for val in values:
        if val != ".":
            amount_per_digit[int(val)] += 1

    can_press_together = can_press_each * 2

    can_push: List[int] = list(
        filter(lambda digit_amount: digit_amount <= can_press_together and digit_amount != 0, amount_per_digit))

    return len(can_push)


def main() -> None:
    can_press_each: int = int(input())
    values: str = "".join(input() for _ in range(4))
    print(count_points(can_press_each, values))


if __name__ == '__main__':
    main()
