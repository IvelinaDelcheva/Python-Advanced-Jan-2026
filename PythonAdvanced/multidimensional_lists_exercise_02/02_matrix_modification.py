rows = int(input())
matrix = [[int(num) for num in input().split()] for row in range(rows)]

input_line = input()
while input_line != 'END':

    command = input_line.split()[0]
    row, col, value = [int(num) for num in input_line.split()[1:]]

    if row not in range(rows) or col not in range(rows):
        print("Invalid coordinates")
    else:
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value

    input_line = input()

[print(*x) for x in matrix]
