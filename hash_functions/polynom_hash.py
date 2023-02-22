def main() -> None:
    base = int(input())
    module = int(input())
    data = input()[::-1]

    hash_res = 0
    base_val = 1

    for char in data:
        hash_res = ((hash_res + ord(char) * base_val) % module)
        base_val = (base_val * base) % module

    print(int(hash_res))


if __name__ == '__main__':
    main()
