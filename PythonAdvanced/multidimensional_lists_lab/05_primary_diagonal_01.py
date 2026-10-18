matrix_size = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(matrix_size)]

diagonal_sum = sum(matrix[row_index][row_index] for row_index in range(matrix_size))

print(diagonal_sum)