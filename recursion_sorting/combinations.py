d = {'2': 'abc',
     '3': 'def',
     '4': 'ghi',
     '5': 'jkl',
     '6': 'mno',
     '7': 'pqrs',
     '8': 'tuv',
     '9': 'wxyz'}


def combinations(input_string):
    data = []
    if len(input_string) == 0:
        return ['']
    word = d[input_string[-1]]

    for num in combinations(input_string[:-1:]):
        for w in word:
            data.append(num + w)

    return data


def main():
    print(*combinations(input()))


if __name__ == '__main__':
    main()
