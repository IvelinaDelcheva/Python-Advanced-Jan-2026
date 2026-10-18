from math import ceil

def setup():
    player_1_name = input('Player one name: ')
    player_2_name = input('Player two name: ')
    player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'? ").upper()

    while player_1_sign not in ['X', 'O']:
        player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'? ").upper()

    player_2_sign = 'X' if player_1_sign == 'O' else 'O'
    player_1 = [player_1_name, player_1_sign]
    player_2 = [player_2_name, player_2_sign]
    board = [[' ', ' ', ' '] for _ in range(3)]
    print(f'This is the numeration of the board:')
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f'{player_1[0]} starts first!')

    return player_1, player_2, board

def check_row(g_board, player_sign):
    for row in g_board:
        if row.count(player_sign) == 3:
            return True
    return False


def check_col(g_board, player_sign):
    for col in range(3):
        sign_count = 0
        for row in range(3):
            if g_board[row][col] == player_sign:
                sign_count += 1
        if sign_count == 3:
            return True
    return False

def check_diagonal(g_board, player_sign):
    primary_diagonal = 0
    secondary_diagonal = 0
    for index in range(len(g_board)):
        if g_board[index][index] == player_sign:
            primary_diagonal += 1

        if g_board[index][len(g_board) - index - 1] == player_sign:
            secondary_diagonal += 1
    if primary_diagonal == 3 or secondary_diagonal == 3:
        return True
    return False

def check_if_won(g_board, player_sign):
    if check_row(g_board, player_sign) or check_col(g_board, player_sign) or check_diagonal(g_board, player_sign):
        return True
    return False


def play(current_player, other_player, game_board, player_turn):
    is_winner = False
    while True:
        try:
            position = int(input(f'{current_player[0]} choose free position [1-9]: '))
        except ValueError:
            print('Please choose a valid number [1-9]')
            continue

        if position not in range(1, 10):
            print('Please choose a number in the range [1-9]')
            continue

        row = ceil(position / 3) - 1
        col = position % 3 - 1

        if game_board[row][col] == ' ':
            game_board[row][col] = current[1]
            player_turn += 1
            break
        else:
            print('This position is already taken!')
            print('Please choose free position!')
            continue

    if player_turn >= 5:
        if check_if_won(board, current_player[1]):
            print(f'{current_player[0]} won!!!')
            print(f'You loose {other_player[0]}! You are looser! Xa-Xa-Xa!!!')
            print(f'Are you haappy now {current_player[0]}? :D')
            print_board(game_board)
            is_winner = True
    return player_turn, is_winner

def print_board(game_board):
    for board_row in game_board:
        print(f'| {' | '.join(board_row)} |')

player_1, player_2, board = setup()

turn = 0
winner = False
current, other = player_1, player_2

while turn < 9:
    turn, winner = play(current, other, board, turn)
    if winner:
        break
    print_board(board)
    current, other = other, current

else:
    print("Cat's game!")









