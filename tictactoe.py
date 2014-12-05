import random


def drawBoard(board):

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


def inputPlayerLetter():
    letter = ''
    while not(letter == 'X'or letter == 'O'):
        print("Choose a letter")
        letter = input()
        letter = letter.upper()

    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']


def playAgain():

    print("Play  again")
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWin(bo, ltr):

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


def getBoardCopy(board):

    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):

    return board[move] == ' '


def getPlayerMove(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Next move? (1-9)')
        move = input()
    return int(move)


def chooseRandomMove(board, moveList):

    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, comLett):

    if comLett == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, comLett, i)
            if isWin(copy, comLett):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWin(copy, playerLetter):
                return i

    move = chooseRandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMove(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Tic-tac-toe ')

while True:

    theBoard = [' '] * 10
    playerLetter, comLett = inputPlayerLetter()
    turn = 'player'

    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWin(theBoard, playerLetter):
                drawBoard(theBoard)
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('is tie')
                    break
                else:
                    turn = 'computer'

        else:

            move = getComputerMove(theBoard, comLett)
            makeMove(theBoard, comLett, move)

            if isWin(theBoard, comLett):
                drawBoard(theBoard)
                print('Computer win')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
