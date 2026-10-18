rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]
primary_diagonal = [matrix[row][row] for row in range(rows)]
secondary_diagonal = [matrix[row][-1 -row] for row in range(rows)]

diff = sum(primary_diagonal) - sum(secondary_diagonal)
print(abs(diff))