def initialize_board(num_rows, num_cols):
    #Initializes a Connect Four board.
    board = []
    for row in range(num_rows):
        board.append(["-" for _ in range(num_cols)])
    return board


def print_board(board):
    #Prints the Connect Four board to the console.
    for row in board:
        print(" ".join(row))


def check_if_winner(board, player):
    # Check for vertical wins
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check for horizontal wins
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    return False


def is_board_full(board):
    #Checks if the board is full.
    for row in board:
        if "-" in row:
            return False
    return True


def play_game():
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))
    board = initialize_board(num_rows, num_cols)
    print_board(board)
    print("\nPlayer 1: x")
    print("Player 2: o")
    current_player = "x"
    #Ask user for height and inform user of player names and their respective tokens

    while True:
        player_name = "Player 1" if current_player == "x" else "Player 2"
        column = int(input(f"\n{player_name}: Which column would you like to choose? "))

        if column < 0 or column >= len(board[0]):
            print("Invalid column.")
            continue

        for row in range(num_rows - 1, -1, -1):
            if board[row][column] == "-":
                board[row][column] = current_player
                break
        else:
            print("Column is full.")
            continue

        print_board(board)

        if check_if_winner(board, current_player):
            print(f"{player_name} won the game!")
            break

        if is_board_full(board):
            print("Draw. Nobody wins.")
            break

        current_player = "o" if current_player == "x" else "x"
        #Determine the end of the game

if __name__ == "__main__":
    play_game()
