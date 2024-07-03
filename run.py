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
    # Horizontal row
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == peice and board[r][c+1] == peice and board[r][c+2] == peice and board[r][c+3]:
                return True
    
    # Vertical row
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == peice and board[r+1][c] == peice and board[r+2][c] == peice and board[r+3][c]:
                return True
    
    # Positive Diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == peice and board[r+1][c+1] == peice and board[r+2][c+2] == peice and board[r+3][c+3]:
                return True

    # Negative Diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT, 3):
            if board[r][c] == peice and board[r-1][c+1] == peice and board[r-2][c+2] == peice and board[r-3][c+3]:
                return True

def replay_game(replay):
    """
    Replays or exits the game based on user answer
    """
    
    if replay == 'Y':
        run_game()

    while replay != 'Y':
        if replay != 'N':
            error_replay = input('Please answer (Y) for yes, or (N) for no: ').capitalize()
            if error_replay == 'Y':
                run_game()
            elif error_replay == 'N':
                print('Thanks for playing')
                break
        else:
            print('Thanks for playing')
            break
    return replay
        
    
        

        

    

def run_game():

    print("Welcome to connect 4\nPlease input player one's name")
    user_1 = input('Player One: ')
    print("Please input player Two's name")
    user_2 = input('Player Two: ')
    board = create_board()
    print(board)
    game_over = False
    turn = 0

    while not game_over:
        if turn == 0:

            try:
                col = int(input(f"{user_1} is up\nSelect a column between 0-6: "))
                if col > ROW_COUNT:
                    raise ValueError(f'{col} is not a column.')
                    
            except ValueError as e:
                print(f'Oops!\n{e}')
                continue

            if valid_location(board, col):
                row = next_open_row(board, col)
                drop_peice(board, row, col, 1)

                if winning_move(board, 1):
                    print(f"{user_1} wins")
                    game_over = True
                    replay = input('replay Y/N?: ').capitalize()
                    replay_game(replay)
                    
                    
        else:
            
            try:
                col = int(input(f"{user_2} is up\nSelect a column between 0-6: "))
                if col > ROW_COUNT:
                    raise ValueError(f'{col} is not a column.')
                    
            except ValueError as e:
                print(f'Oops!\n{e}')
                continue

            if valid_location(board, col):
                row = next_open_row(board, col)
                drop_peice(board, row, col, 2)

                if winning_move(board, 2):
                    print(f"{user_2} wins")
                    game_over = True
                    replay_game(replay)
                    

        print_board(board)

        turn += 1
        turn = turn % 2 

    
    
        
        

run_game()



    