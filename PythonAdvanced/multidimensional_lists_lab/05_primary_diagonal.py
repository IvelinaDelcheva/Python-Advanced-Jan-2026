matrix_size = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(matrix_size)]

diagonal_sum = 0

for row_index in range(matrix_size):
    for column_index in range(matrix_size):
        if row_index == column_index:
            diagonal_sum += matrix[row_index][column_index]

print(diagonal_sum)