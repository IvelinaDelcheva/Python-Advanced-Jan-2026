rows = int(input())
bunny = []
number_of_eggs = 0
collecting_positions = []
position = ''

field = []
positions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


for row in range(rows):
    field.append([int(el)if el.isdigit() else el for el in input().split()])

    for col in range(rows):
        if field[row][col] == 'B':
            bunny.extend([row, col])



for pos, idx in positions.items():
    current_eggs = 0
    current_positions = []
    row_b = bunny[0] + idx[0]
    col_b = bunny[1] + idx[1]

    while row_b in range(rows) and col_b in range(rows):
        if field[row_b][col_b] == 'X':
            break

        if field[row_b][col_b] > 0:
            current_eggs += field[row_b][col_b]
            current_positions.append([row_b, col_b])

            if current_eggs > number_of_eggs:
                position = pos
                number_of_eggs = current_eggs
                collecting_positions = current_positions

        row_b += idx[0]
        col_b += idx[1]

print(position)
[print(x) for x in collecting_positions]
print(number_of_eggs)




