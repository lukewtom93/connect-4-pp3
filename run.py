import numpy as np

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


board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input("Player One's up\nSelect a column between 0-6: "))
    else:
        col = int(input("Player Two's up\nSelect a column between 0-6: "))

    turn += 1
    turn = turn % 2 

    print(col)