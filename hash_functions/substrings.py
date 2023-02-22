import string
import random


def count(data):
    res = ''
    start = 0
    found = 0
    found_max = 0
    end = len(data) - 1

    while start <= end:
        if data[start] not in res:
            res += data[start]
            found += 1
        else:
            res = res[res.index(data[start]) + 1:] + data[start]
            found = len(res)
        if found_max < found:
            found_max = found
        start += 1

    return found_max


def main() -> None:
    print(count(input()))


if __name__ == '__main__':
    main()
