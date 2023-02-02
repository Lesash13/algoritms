def main() -> None:
    import re

    phrase = input()
    phrase_converted = re.sub(r'[^a-zA-Z0-9]', '', phrase).lower()
    res = True
    for i in range(0, len(phrase_converted)):
        if phrase_converted[i] != phrase_converted[len(phrase_converted) - 1 - i]:
            res = False
    print(res)


if __name__ == '__main__':
    main()
