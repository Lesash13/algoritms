def calc(amount, values):
    for i in range(amount - 2):
        if values[i] < values[i + 1] + values[i + 2]:
            print(values[i] + values[i + 1] + values[i + 2])
            break
        else:
            i += 1


def main() -> None:
    amount = int(input())
    values = sorted([int(num) for num in input().split(' ')], reverse=True)
    calc(amount, values)


if __name__ == '__main__':
    main()
