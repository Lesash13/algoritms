import string
import random


def heads_arr(base, module, data):
    data_len = len(data) + 1
    hash_info = [0] * data_len
    for i in range(1, data_len):
        hash_info[i] = (hash_info[i - 1] * base + data[i - 1]) % module

    return hash_info


def tails_arr(base, module, data):
    data_len = len(data)
    hash_info = [0] * (data_len + 1)
    step = 0
    for i in reversed(range(0, data_len)):
        hash_info[i] = (hash_info[i + 1] + data[i] * (base ** step)) % module
        step += 1

    return hash_info


def main() -> None:
    base = int(input())
    module = int(input())
    data = input()
    parts_amount = int(input())

    heads = heads_arr(base, module, bytes(data.strip(), encoding='ascii'))
    tails = tails_arr(base, module, bytes(data.strip(), encoding='ascii'))
    print('heads', heads)
    print('tails', tails)

    for i in range(parts_amount):
        s, e = input().strip().split()
        start, end = int(s), int(e)
        print((base ** (len(data) - start)))
        print((len(data) - start))
        res = heads[-1] - tails[end - 1] - (heads[start - 1] * (base ** (len(data) - start))) % module
        #res = (tails[start] - tails[end + 1])  # // ((base ** (len(data) - end)) % module)) % module
        print(res)


if __name__ == '__main__':
    main()
