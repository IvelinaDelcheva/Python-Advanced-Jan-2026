rows = int(input())
MIN_AMOUNT_NECTAR = 30
bee_matrix = []
bee = []
energy = 15
total_nectar = 0
restored_energy = 0
hive_reached = False
energy_restored = False

for row in range(rows):
    bee_matrix.append(list(input()))
    for col in range(rows):
        if bee_matrix[row][col] == 'B':
            bee_matrix[row][col] = '-'
            bee = [row, col]

while True:
    command = input()
    bee_matrix_length = len(bee_matrix)
    row, col = bee

    if command == 'up':
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'left':
        col -= 1
    elif command == 'right':
        col += 1

    if (row < 0 or row >= bee_matrix_length or col < 0 or col >= bee_matrix_length):
        if command == 'right':
            col = 0
        elif command == 'left':
            col = bee_matrix_length - 1
        elif command == 'up':
            row = bee_matrix_length - 1
        elif command == 'down':
            row = 0

    if bee_matrix[row][col].isdigit():
        total_nectar += int(bee_matrix[row][col])
        bee_matrix[row][col] = '-'
        energy -= 1
        bee = [row, col]

    elif bee_matrix[row][col] == '-':
        energy -= 1
        bee = [row, col]

    if energy <= 0 and total_nectar < 30:
        break

    if energy <= 0 and total_nectar >= 30:
        if not energy_restored:
            energy_restored = True
            energy += total_nectar - MIN_AMOUNT_NECTAR
            total_nectar = MIN_AMOUNT_NECTAR
        else:
            break

    if bee_matrix[row][col] == 'H':
        energy -= 1
        hive_reached = True
        bee = [row, col]
        break

if hive_reached and total_nectar >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
elif hive_reached and total_nectar < 30:
    print("Beesy did not manage to collect enough nectar.")
elif energy <= 0:
    print("This is the end! Beesy ran out of energy.")

last_row, last_col = bee
bee_matrix[last_row][last_col] = 'B'
for row in bee_matrix:
    print(*row, sep='')
