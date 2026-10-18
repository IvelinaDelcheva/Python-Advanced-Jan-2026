rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_number = 0
mat_positions = ()

for row in range(rows - 1):
    for col in range(cols - 1):
        sub_matrix = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if sub_matrix > max_number:
            max_number = sub_matrix
            mat_positions = (row, col)

for max_row in range(mat_positions[0] , mat_positions[0] + 2):
    for max_col in range(mat_positions[1], mat_positions[1] + 2):
        print(matrix[max_row][max_col], end=' ')
    print()
print(max_number)
