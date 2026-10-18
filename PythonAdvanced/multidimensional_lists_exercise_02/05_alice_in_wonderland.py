rows = int(input())
# wonderland = [[int(el) if el.isdigit() else el for el in input().split()] for row in range(rows)]
# alice = [(row, col) for row in range(rows) for col in range(rows) if wonderland[row][col] == 'A']

wonderland = []
alice = []
for row in range(rows):
    wonderland.append(input().split())
    for col in range(rows):
        if wonderland[row][col] == "A":
            wonderland[row][col] = '*'
            alice = [row, col]

tea_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while tea_bags < 10:
    curr_direction = input()
    move = directions[curr_direction]

    row_a = alice[0] + move[0]
    col_a = alice[1] + move[1]

    if row_a not in range(rows) or col_a not in range(rows):
        print("Alice didn't make it to the tea party.")
        break

    if wonderland[row_a][col_a] == 'R':
        print("Alice didn't make it to the tea party.")
        wonderland[row_a][col_a] = '*'
        break

    if wonderland[row_a][col_a].isdigit():
        tea_bags += int(wonderland[row_a][col_a])
    alice = [row_a, col_a]
    wonderland[row_a][col_a] = '*'

else:
    print("She did it! She went to the party.")
[print(*line) for line in wonderland]



