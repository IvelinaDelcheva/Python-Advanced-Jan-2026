number_presents = int(input())
neighborhood_size = int(input())
nice_kids = 0
nice_kids_presents = 0
neighborhood = []
santa = []

for row in range(neighborhood_size):
    neighborhood.append(input().split())
    for col in range(neighborhood_size):
        if neighborhood[row][col] == 'S':
            santa = [row, col]
            neighborhood[row][col] = '-'
        elif neighborhood[row][col] == 'V':
            nice_kids += 1

while number_presents > 0:
    row, col = santa
    command = input()

    if command == 'Christmas morning':
        break

    if command == 'up':
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'left':
        col -= 1
    elif command == 'right':
        col += 1

    if neighborhood[row][col] == 'V':
        nice_kids_presents += 1
        nice_kids -= 1
        number_presents -= 1
        santa = [row, col]
        neighborhood[row][col] = '-'
    elif neighborhood[row][col] == 'X':
        santa = [row, col]
        neighborhood[row][col] = '-'
    elif neighborhood[row][col] == '-':
        santa = [row, col]
    elif neighborhood[row][col] == 'C':
        santa = [row, col]
        neighborhood[row][col] = '-'

        if neighborhood[row - 1][col] in ('V', 'X'):
            if neighborhood[row - 1][col] == 'V':
                nice_kids_presents += 1
                nice_kids -= 1
            number_presents -= 1
            neighborhood[row - 1][col] = '-'

        if neighborhood[row + 1][col] in ('V', 'X'):
            if neighborhood[row + 1][col] == 'V':
                nice_kids_presents += 1
                nice_kids -= 1
            number_presents -= 1
            neighborhood[row + 1][col] = '-'

        if neighborhood[row][col + 1] in ('V', 'X'):
            if neighborhood[row][col + 1] == 'V':
                nice_kids_presents += 1
                nice_kids -= 1
            number_presents -= 1
            neighborhood[row][col + 1] = '-'

        if neighborhood[row][col - 1] in ('V', 'X'):
            if neighborhood[row][col - 1] == 'V':
                nice_kids_presents += 1
                nice_kids -= 1
            number_presents -= 1
            neighborhood[row][col - 1] = '-'


last_row, last_col = santa
neighborhood[last_row][last_col] = 'S'
if number_presents <= 0:
    print("Santa ran out of presents!")

for row in neighborhood:
    print(*row)

if nice_kids <= 0:
    print(f"Good job, Santa! {nice_kids_presents} happy nice kid/s.")
elif nice_kids > 0:
    print(f"No presents for {nice_kids} nice kid/s.")


