def counter(n_length, k_repeats, data):
    hash_arr = {}
    res = set()
    for i in range(len(data) - int(n_length)):
        sub = data[i:i + int(n_length)]
        if sub in hash_arr.keys():
            value = hash_arr[sub]
            value[1] += 1
            if value[1] >= int(k_repeats):
                res.add(value[0])
            hash_arr[sub] = value
        else:
            hash_arr[sub] = [i, 1]
    print(*res)


def main() -> None:
    n_length, k_repeats = input().split()
    data = input()

    counter(n_length, k_repeats, data)


if __name__ == '__main__':
    main()
