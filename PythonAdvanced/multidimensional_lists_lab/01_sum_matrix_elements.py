n_rows, n_cols = [int(el) for el in input().split(', ')]

matrix = []
sum_numbers = 0
for _ in range(n_rows):
    data = [int(el) for el in input().split(', ')]
    matrix.append(data)
    sum_numbers += sum(data)


print(sum_numbers)
print(matrix)