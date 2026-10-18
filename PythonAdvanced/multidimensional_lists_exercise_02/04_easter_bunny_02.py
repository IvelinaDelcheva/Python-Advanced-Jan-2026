rows = int(input())
bunny = []
best_direction = ''
number_of_eggs = 0
collecting_positions = []
field = []
positions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    field.append([int(el) if el.isdigit() else el for el in input().split()])

    for col in range(rows):
        if field[row][col] == 'B':
            bunny = [row, col]

for pos, idx in positions.items():
    current_eggs = 0
    current_positions = []
    row = bunny[0] + idx[0]
    col = bunny[1] + idx[1]

    while 0 <= row < rows and 0 <= col < rows :
        if field[row][col] == 'X':
            break

        if field[row][col] > 0:
            current_eggs += field[row][col]
            current_positions.append([row, col])

        row += idx[0]
        col += idx[1]

    if current_eggs > number_of_eggs:
        number_of_eggs = current_eggs
        best_direction = pos
        collecting_positions = current_positions

print(best_direction)
print(*collecting_positions, sep='\n')
print(number_of_eggs)
