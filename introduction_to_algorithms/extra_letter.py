def main() -> None:
    char_arr = list(input())
    char_arr_2 = input()
    for i in char_arr:
        if char_arr_2.count(i):
            char_arr_2 = char_arr_2.replace(i, "", 1)
    print(char_arr_2)


if __name__ == '__main__':
    main()
