import random


def draw_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def input_player_letter():
    letter = ''
    while not(letter == 'X'or letter == 'O'):
        print("Choose a letter")
        letter = input()
        letter = letter.upper()

    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']


def play_again():

    print("Play again")
    return input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def is_win(bo, ltr):

    return((bo[7] == ltr and bo[8] == ltr and bo[9] == ltr)
           or
           (bo[4] == ltr and bo[5] == ltr and bo[6] == ltr)
           or
           (bo[1] == ltr and bo[2] == ltr and bo[3] == ltr)
           or
           (bo[7] == ltr and bo[4] == ltr and bo[1] == ltr)
           or
           (bo[8] == ltr and bo[5] == ltr and bo[2] == ltr)
           or
           (bo[9] == ltr and bo[6] == ltr and bo[3] == ltr)
           or
           (bo[7] == ltr and bo[5] == ltr and bo[3] == ltr)
           or
           (bo[9] == ltr and bo[5] == ltr and bo[1] == ltr))


def get_board_copy(board):

    copy_board = []

    for i in board:
        copy_board.append(i)

    return copy_board


def is_space_free(board, move):

    return board[move] == ' '


def get_player_move(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('Next move? (1-9)')
        move = input()
    return int(move)


def choose_random_move(board, moveList):

    possible_moves = []
    for i in moveList:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, com_lett):

    if com_lett == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, com_lett, i)
            if is_win(copy, com_lett):
                return i

    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_win(copy, player_letter):
                return i

    move = choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    if is_space_free(board, 5):
        return 5

    return choose_random_move(board, [2, 4, 6, 8])


def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

print('Tic-tac-toe ')

while True:

    playing_board = [' '] * 10
    player_letter, com_lett = inputplayer_letter()
    turn = 'player'

    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            draw_board(playing_board)
            move = get_player_move(playing_board)
            make_move(playing_board, player_letter, move)

            if is_win(playing_board, player_letter):
                draw_board(playing_board)
                game_is_playing = False
            else:
                if is_board_full(playing_board):
                    draw_board(playing_board)
                    print('is tie')
                    break
                else:
                    turn = 'computer'

        else:

            move = get_computer_move(playing_board, com_lett)
            make_move(playing_board, com_lett, move)

            if is_win(playing_board, com_lett):
                draw_board(playing_board)
                print('Computer win')
                game_is_playing = False
            else:
                if is_board_full(playing_board):
                    draw_board(playing_board)
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
