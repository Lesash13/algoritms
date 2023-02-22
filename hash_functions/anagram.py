def counter(amount, data):
    hash_arr = {}
    for i in range(amount):
        sub = ''.join(sorted(data[i]))
        if sub in hash_arr.keys():
            value = hash_arr[sub]
            value += ' ' + str(i)
            hash_arr[sub] = value

        else:
            hash_arr[sub] = str(i)
    print(*hash_arr.values(), sep='\n')


def main() -> None:
    amount = int(input())
    data = input().split()

    counter(amount, data)


if __name__ == '__main__':
    main()
