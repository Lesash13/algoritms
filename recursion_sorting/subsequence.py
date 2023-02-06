def calc(text, subtext):
    if len(text) == 0 or len(subtext) == 0 or len(subtext) > len(text):
        return False
    cur = 0
    for j in range(len(text)):
        if subtext[cur] == text[j]:
            cur += 1
            if cur == len(subtext):
                return True
    return False


def main() -> None:
    subtext = input()
    text = input()
    print(calc(text, subtext))


if __name__ == '__main__':
    main()
