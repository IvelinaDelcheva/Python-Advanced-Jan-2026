rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

primary_diagonal = [matrix[row][row] for row in range(rows)]
secondary_diagonal = [matrix[row][-1 - row] for row in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

