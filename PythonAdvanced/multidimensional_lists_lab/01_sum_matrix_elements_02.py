n_rows, n_cols = [int(el) for el in input().split(', ')]


matrix = [[int(el) for el in input().split(', ')] for _ in range(n_rows)]
sum_numbers = [sum(ls) for ls in matrix]

print(sum(sum_numbers))
print(matrix)