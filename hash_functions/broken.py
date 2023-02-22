import string
import random


def count_hash(data):
    base = 1000
    module = 123987123
    hash_res = 0
    base_val = 1
    for char in data:
        hash_res = ((hash_res + ord(char) * base_val) % module)
        base_val = (base_val * base) % module

    return int(hash_res)


def main() -> None:
    symbols = string.ascii_lowercase
    str1 = ''.join(random.choice(symbols) for _ in range(10))

    hash = count_hash(str1[::-1])

    while True:
        str2 = ''.join(random.choice(symbols) for _ in range(20))
        hash2 = count_hash(str2[::-1])
        if hash2 == hash:
            print(str2)
            print(str1)
            break


if __name__ == '__main__':
    main()
