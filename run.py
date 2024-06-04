import numpy as np

def create_board():
    """
    Creates blank board
    """
    board = np.zeros((6, 7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        selection = int(input("Player One's up\nSelect a column between 1-6: "))
    else:
        selection = int(input("Player Two's up\nSelect a column between 1-6: "))

    turn += 1
    turn = turn % 2 

    print(selection)