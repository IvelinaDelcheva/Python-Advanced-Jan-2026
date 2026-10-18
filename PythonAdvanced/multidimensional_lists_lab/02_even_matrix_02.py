n_rows = int(input())

matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0] for _ in range(n_rows)]

print(matrix)