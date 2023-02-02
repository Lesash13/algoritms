# ID = 81737343

def count_points(can_press_together, values) -> int:
    count_list: list = [0] * 10
    for val in values:
        if val != ".":
            count_list[int(val)] += 1

    can_push: list = list(
        filter(lambda digit_amount: digit_amount <= can_press_together and digit_amount != 0, count_list))

    return len(can_push)


def main() -> None:
    can_press_together: int = int(input()) * 2
    values: str = "".join(input() for _ in range(4))
    print(count_points(can_press_together, values))


if __name__ == '__main__':
    main()
