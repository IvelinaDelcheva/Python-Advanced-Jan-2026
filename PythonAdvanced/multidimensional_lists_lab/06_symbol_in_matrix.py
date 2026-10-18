n = int(input())

matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

symbol = input()

for index_row in range(n):
    for index_col in range(n):
        if matrix[index_row][index_col] == symbol:
            position = (index_row, index_col)
            print(position)
            exit()

else:
    print(f"{symbol} does not occur in the matrix")



