presents = int(input())
size_neighborhood = int(input())
neighborhood = []
santa = []
nice_kids = 0
kids_received_p = 0

for row in range(size_neighborhood):
    neighborhood.append(input().split())
    for col in range(size_neighborhood):
        if neighborhood[row][col] == 'S':
            santa = [row, col]
        elif neighborhood[row][col] == 'V':
            nice_kids += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while (command := input()) != 'Christmas morning' and presents > 0:

    s_row = santa[0] + directions[command][0]
    s_col = santa[1] + directions[command][1]

    if s_row in range(size_neighborhood) and s_col in range(size_neighborhood):
        if neighborhood[s_row][s_col] == 'C':
            for dir, values in directions.items():
                s_next_r = s_row + values[0]
                s_next_c = s_col + values[1]

                if s_next_r in range(size_neighborhood) and s_next_c in range(size_neighborhood):
                    if neighborhood[s_next_r][s_next_c] in ('V', 'X'):
                        presents -= 1
                        if neighborhood[s_next_r][s_next_c] == 'V':
                            nice_kids -= 1
                        neighborhood[s_next_r][s_next_c] = '-'
                        if presents <= 0:
                            break

        if neighborhood[s_row][s_col] == 'V':
            presents -= 1
            kids_received_p += 1
            nice_kids -= 1
        neighborhood[santa[0]][santa[1]] = '-'
        santa = [s_row, s_col]
        neighborhood[s_row][s_col] = 'S'

        if presents <= 0:
            break

if presents <= 0:
    print(f"Santa ran out of presents!")
[print(*x) for x in neighborhood]
if nice_kids == 0:
    print(f"Good job, Santa! {kids_received_p} happy nice kid/s.")
elif presents <= 0 and nice_kids > 0:
    print(f"No presents for {nice_kids} nice kid/s.")
