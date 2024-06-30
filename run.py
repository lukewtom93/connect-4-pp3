import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    """
    Creates blank board
    """
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    
    return board

def print_board(board):
    """
    Rectifies numpy 0.0 index.
    Flips board to play from the bottom.
    """
    print(np.flip(board, 0))

def valid_location(board, col):
    """
    Checking location on the board is free
    to play into.
    """
    return board[ROW_COUNT-1][col] == 0

def next_open_row(board, col):
    """
    Checks for empty rows
    """
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def drop_peice(board, row, col, peice):
    """
    Drops players peice into the board
    """
    board[row][col] = peice

def winning_move(board, peice):
    """
    Checks for 4 peices in a row
    """
    #Horizontal row
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == peice and board[r][c+1] == peice and board[r][c+2] == peice and board[r][c+3]:
                return True


board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input("Player One's up\nSelect a column between 0-6: \n"))

        if valid_location(board, col):
            row = next_open_row(board, col)
            drop_peice(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 wins")
                game_over = True
    else:
        col = int(input("Player Two's up\nSelect a column between 0-6: \n"))

        if valid_location(board, col):
            row = next_open_row(board, col)
            drop_peice(board, row, col, 2)

    print_board(board)

    turn += 1
    turn = turn % 2 

    print(col)