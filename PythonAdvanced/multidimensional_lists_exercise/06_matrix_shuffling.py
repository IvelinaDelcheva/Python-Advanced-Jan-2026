rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for x in range(rows)]


while True:

    input_line = input()

    if input_line == 'END':
        break

    command = input_line.split()

    if command[0] != 'swap' or len(command) > 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]

    if row1 not in range(rows) and row2 not in range(rows) and col1 not in range(cols) and col2 not in range(cols):
        print("Invalid input!")
        continue

    if command[0] == 'swap':
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*r) for r in matrix]


