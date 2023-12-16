def display_game(board):
    print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
    print(board)


def is_valid_move(position, board):
    if position == 'q':
        return True

    if not position.isdigit():
        return False

    position = int(position)
    
    if position < 0 or position > 6:
        return False

    if board[position] == '-':
        return False

    return True


def make_move(position, board):
    position = int(position)
    frog = board[position]

    if frog == 'G':
        if position + 2 <= 6 and board[position + 2] == '-':
            board[position], board[position + 2] = board[position + 2], board[position]
        elif position + 1 <= 6 and board[position + 1] == '-':
            board[position], board[position + 1] = board[position + 1], board[position]
    elif frog == 'B':
        if position - 2 >= 0 and board[position - 2] == '-':
            board[position], board[position - 2] = board[position - 2], board[position]
        elif position - 1 >= 0 and board[position - 1] == '-':
            board[position], board[position - 1] = board[position - 1], board[position]

def frog_leap_game():
    board = ['G', 'G', 'G', '-', 'B', 'B', 'B']

    while True:
        display_game(board)

        move = input("Enter the position to move (0-6, or 'q' to quit): ")

        if not is_valid_move(move, board):
            print("Invalid move! Please try again.")
            continue

        if move == 'q':
            print("Quitting the game.")
            break

        make_move(move, board)

        if board == ['B', 'B', 'B', '-', 'G', 'G', 'G']:
            display_game(board)
            print("Congratulations! You solved the puzzle.")
            break

if __name__ == "__main__":
    frog_leap_game()
