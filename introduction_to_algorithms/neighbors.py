def main() -> None:
    matrix_lines = int(input())
    columns = int(input())
    matrix = []
    for i in range(matrix_lines):
        row = input().split()
        for i in range(columns):
            row[i] = int(row[i])
        matrix.append(row)

    x = int(input())
    y = int(input())
    res = []
    if x > 0:
        x1 = x - 1
        y1 = y
        res.append(matrix[x1][y1])
    if y > 0:
        x1 = x
        y1 = y - 1
        res.append(matrix[x1][y1])
    if x < matrix_lines - 1:
        x1 = x + 1
        y1 = y
        res.append(matrix[x1][y1])
    if y < columns - 1:
        x1 = x
        y1 = y + 1
        res.append(matrix[x1][y1])
    print(*sorted(res), sep=" ")


if __name__ == '__main__':
    main()
