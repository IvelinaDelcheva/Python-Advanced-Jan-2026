matrix = [line.split() for line in input().split('|')]

flattened = []

for index in range(len(matrix) - 1, -1, -1):
    flattened.extend(matrix[index])

print(*flattened)