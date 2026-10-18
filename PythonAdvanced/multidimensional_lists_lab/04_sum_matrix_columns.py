rows, columns = [int(el) for el in input().split(', ')]

matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

for col_index in range(columns):
    sum_column = 0
    for row_index in range(rows):
        sum_column += matrix[row_index][col_index]
    print(sum_column)


