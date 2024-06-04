import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    """
    Creates blank board
    """
    board = np.zeros((6, 7))
    return board

def valid_location(board, col):
    """
    Checking location on the board is free
    to play into.
    """
    return board[5][col] == 0

def next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def drop_peice(board, row, col, peice):
    board[row][col] = peice

board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input("Player One's up\nSelect a column between 0-6: "))

        if valid_location(board, col):
            row = next_open_row(board, col)
            drop_peice(board, row, col, 1)
    else:
        col = int(input("Player Two's up\nSelect a column between 0-6: "))

        if valid_location(board, col):
            row = next_open_row(board, col)
            drop_peice(board, row, col, 2)

    print(board)

    turn += 1
    turn = turn % 2 

    print(col)