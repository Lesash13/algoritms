def transported(matrix, matrix_lines, columns):
    for i in range(columns):
        for j in range(matrix_lines):
            print(matrix[j][i], end=' ')
        print('')


def main() -> None:
    matrix_lines = int(input())
    columns = int(input())
    matrix = [input().split(' ') for _ in range(matrix_lines)]
    transported(matrix, matrix_lines, columns)


if __name__ == '__main__':
    main()
