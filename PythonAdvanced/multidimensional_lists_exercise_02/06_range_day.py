rows = 5
count_targets = 0
shotgun_range = []
my_position = []
hit_targets = []

for row in range(rows):
    shotgun_range.append(input().split())
    for col in range(rows):
        if shotgun_range[row][col] == 'A':
            my_position = [row, col]
        elif shotgun_range[row][col] == 'x':
            count_targets += 1

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

n_commands = int(input())

for _ in range(n_commands):
    input_line = input().split()
    action, direction = input_line[:2]

    if count_targets <= 0:
        break

    if action == 'move':
        steps = int(input_line[2])
        row, col = my_position
        if direction == 'up':
            row -= steps
        elif direction == 'down':
            row += steps
        elif direction  == 'left':
            col -= steps
        elif direction == 'right':
            col += steps

        if 0 <= row < rows and 0 <= col < rows:
            if shotgun_range[row][col] == '.':
                shotgun_range[my_position[0]][my_position[1]] = '.'
                my_position = [row, col]
    elif action == 'shoot':
        row, col = my_position

        while 0 <= row < rows and 0 <= col < rows:

            if shotgun_range[row][col] == 'x':
                count_targets -= 1
                hit_targets.append([row, col])
                shotgun_range[row][col] = '.'
                break

            row += moves[direction][0]
            col += moves[direction][1]

if count_targets <= 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {count_targets} targets left.")
print(*hit_targets, sep='\n')