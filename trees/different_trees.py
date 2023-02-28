def calc(val):
    if val == 0:
        return 1
    return calc(val - 1) * val


n = int(input())

print(int(calc(2 * n) / (calc(n) * calc(n + 1))))
