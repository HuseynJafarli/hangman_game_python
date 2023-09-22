def initialize_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

def display_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')
    print(' 1 2 3 4 5 6 7 ')

def is_valid_move(board, column):
    return column >= 0 and column < 7 and board[0][column] == ' '

def make_move(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            break

def check_for_win(board):
    # Logic to check for a win goes here
    
    return False

# def switch_player(current_player):
#     return 'O' if current_player == 'X' else 'X'

def main():
    board = initialize_board()
    current_player = 'X'
    game_won = False

    while not game_won:
        display_board(board)
        column = int(input(f"Player {current_player}, choose a column (1-7): ")) - 1

        if is_valid_move(board, column):
            make_move(board, column, current_player)
            game_won = check_for_win(board)
            if not game_won:
                current_player = switch_player(current_player)
        else:
            print("Invalid move. Please choose a valid column.")

    display_board(board)
    print(f"Player {current_player} wins!")

if __name__ == "__main__":
    main()

#Needs updates for win situations.