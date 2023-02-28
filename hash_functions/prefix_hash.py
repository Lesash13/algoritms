def heads_arr(base, module, data):
    data_len = len(data) + 1
    hash_info = [0] * data_len
    for i in range(1, data_len):
        hash_info[i] = (hash_info[i - 1] * base + data[i - 1]) % module

    return hash_info


def fast_pow(base, power, module):
    m = base % module
    t = 1
    while power:
        if power % 2:
            t *= m
            t %= module
        m *= m
        m %= module
        power //= 2
    return t % module


def main() -> None:
    base = int(input())
    module = int(input())
    data = input()
    parts_amount = int(input())

    heads = heads_arr(base, module, bytes(data.strip(), encoding='ascii'))

    for i in range(parts_amount):
        s, e = input().strip().split()
        start, end = int(s), int(e)

        res = heads[end] - heads[start - 1] * fast_pow(base, end - (start - 1), module)
        print(res % module)


if __name__ == '__main__':
    main()
