base = 911
module = 1000159


def get_hash(data):
    hash_res = 0
    base_val = 1
    for char in data[::-1]:
        hash_res = (hash_res + ord(char) * base_val) % module
        base_val = (base_val * base) % module

    return hash_res


def counter(n_length, k_repeats, data):
    hash_arr = [(-1, 0)] * module

    res = set()
    sub = get_hash(data[0:0 + n_length])
    # print(get_hash(data[1:1 + n_length]))
    for i in range(0, len(data) - n_length):
        # print(hash_arr.keys())
        # print(sub)
        value = hash_arr[sub]
        if value[0] != -1:
            value[1] += 1
            if value[1] >= int(k_repeats):
                res.add(value[0])
            hash_arr[sub] = value
        else:
            hash_arr[sub] = [i, 1]
        # print(data[i:i + n_length])
        sub = ((sub - (ord(data[i]) * (base ** (n_length-1) % module)) % module) * base + ord(data[i + n_length])) % module
    print(*res)
    # print(hash_arr)


def main() -> None:
    n_length, k_repeats = input().split()
    data = input()

    counter(int(n_length), k_repeats, data)


if __name__ == '__main__':
    main()
