def calc(budget, cost):
    can_pay = 0
    for i in cost:
        if i <= budget:
            can_pay += 1
            budget = budget - i

    return can_pay


def main() -> None:
    budget = int(list(input().split(' '))[1])
    cost = sorted([int(num) for num in input().split(' ')])
    print(calc(budget, cost))


if __name__ == '__main__':
    main()
