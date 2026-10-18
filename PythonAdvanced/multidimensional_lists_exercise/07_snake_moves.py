from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = deque(input())
matrix = []

for row in range(rows):
    matrix.append([""] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = snake[0]
        else:
            matrix[row][-1 - col] = snake[0]
        snake.rotate(-1)

for ls in matrix:
    print(''.join(ls))
