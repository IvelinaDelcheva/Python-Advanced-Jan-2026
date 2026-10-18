garden_size = int(input())
garden = []
bunny = []
initial_pos = []
eggs = 5

for row in range(garden_size):
    input_line = list(input())
    garden.append(input_line)
    for col in range(garden_size):
        if garden[row][col] == 'B':
            bunny = [row, col]
            initial_pos = [row, col]
            garden[row][col] = '.'

while True:
    command = input()

    if eggs >= 10 or eggs <= 0:
        break

    if command == 'stop':
        break

    row, col = bunny

    if command == 'up':
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'left':
        col -= 1
    elif command == 'right':
        col += 1

    if (row < 0 or row >= len(garden) or col < 0 or col >= len(garden)):
        bunny = initial_pos

    elif garden[row][col] == '.':
        bunny = [row, col]
    elif garden[row][col] == 'E':
        garden[row][col] = '.'
        eggs += 1
        bunny = [row, col]
    elif garden[row][col] == 'T':
        eggs -= 1
        bunny = [row, col]
        garden[row][col] = '.'
    elif garden[row][col] == 'F':
        eggs *= 2
        bunny = [row, col]
        garden[row][col] = '.'

garden[bunny[0]][bunny[1]] = 'B'
if eggs >= 10:
    print(f"Easter Bunny wins! Collected eggs: {eggs}.")
elif eggs <= 0:
    print("Game over! Easter Bunny has no eggs left.")
else:
    print(f"Easter Bunny stopped hunting with {eggs} eggs.")

for row in garden:
    print(''.join(row))
