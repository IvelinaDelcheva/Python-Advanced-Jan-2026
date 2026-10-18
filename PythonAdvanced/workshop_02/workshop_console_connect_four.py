class InvalidColumnError(Exception):
    pass

class FullColumnError(Exception):
    pass

def create_matrix(r, c):
    return [[0 for _ in range(c)] for _ in range(r)]

def print_matrix(ma):
    return [print(r) for r in ma]


def validate_column_choice(col, max_idx):
    if not (0 <= col < max_idx):
        raise InvalidColumnError

def place_player_choice( ma, c, pl_n):
    for r in range(len(ma) - 1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = pl_n
            return r, c
    raise FullColumnError

def is_player_num(ma, r, c, pl_n):
    try:
        return ma[r][c] == pl_n
    except IndexError:
        return False

def is_vertical_win(ma, r, c, pl_n, slots):
    return all(is_player_num(ma, r + idx, c, pl_n) for idx in range(slots))


def is_horizontal_win(ma, r, c, pl_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r, c + idx, pl_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r, c - idx, pl_n):
            filled += 1
        else:
            break

    return filled >= slots

def is_left_diagonal_win(ma, r, c, pl_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c + idx, pl_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c - idx, pl_n):
            filled += 1
        else:
            break

    return filled >= slots


def is_right_diagonal_win(ma, r, c, pl_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c + idx, pl_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c - idx, pl_n):
            filled += 1
        else:
            break

    return filled >= slots

def is_winner(ma, r, c, pl_n, slots):
    return (is_vertical_win(ma, r, c, pl_n, slots) or
            is_horizontal_win(ma, r, c, pl_n, slots) or
            is_left_diagonal_win(ma, r, c, pl_n, slots) or
            is_right_diagonal_win(ma, r, c, pl_n, slots))




rows = 6
cols = 7
matrix = create_matrix(rows, cols)
print_matrix(matrix)

counter = 1
player_n = 1
SLOTS = 4

while True:
    try:
        column_num = int(input(f'Player {player_n} please choose a column: ')) - 1
        validate_column_choice(column_num, cols)
        r, c = place_player_choice(matrix, column_num, player_n)
        print_matrix(matrix)
    except ValueError:
        print('Please choose a valid number!')
        continue
    except InvalidColumnError:
        print('Please choose column within the range [1-7]')
        continue
    except FullColumnError:
        print('This column is full! Please choose another column!')
        continue

    if is_winner(matrix, r, c, player_n, SLOTS):
        print(f'The winner is Player {player_n}')
        break

    counter += 1
    if counter >= rows * cols:
        print('Game Over! ')

    player_n = 2 if player_n == 1 else 1




