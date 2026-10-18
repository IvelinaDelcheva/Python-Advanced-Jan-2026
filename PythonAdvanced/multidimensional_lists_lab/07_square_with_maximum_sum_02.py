rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_number = 0
sub_matrix = []
mat_positions = ()

for row in range(rows - 1):
    for col in range(cols - 1):
        current_el, next_el, below_el, diagonal = matrix[row][col], matrix[row][col + 1], matrix[row + 1][col] , matrix[row + 1][col + 1]
        sum_matrix = current_el + next_el + below_el + diagonal
        if sum_matrix > max_number:
            max_number = sum_matrix
            sub_matrix = [[current_el, next_el], [below_el, diagonal]]

[print(*row) for row in sub_matrix]
print(max_number)
