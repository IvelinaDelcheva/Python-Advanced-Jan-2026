n_rows = int(input())

matrix = []

for _ in range(n_rows):
    data = [int(el) for el in input().split(', ')]
    matrix.append(data)

flattened = [el for sublist in matrix for el in sublist]

print(flattened)

