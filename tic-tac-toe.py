import random

board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(f"|{row[0]}|{row[1]}|{row[2]}|")
    print()

def check_win(player):
    # h, v, d
    for r in range(3):
        # h
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True
        # v
        if board[0][r] == board[1][r] == board[2][r] == player:
            return True
    
    # d
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def Xplayer_move():
    while True:
        try:
            position = input("Player X | Please enter your move number: (ex:0,3) ")
            row, col = map(int, position.strip().replace(" ", "").split(","))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("This field is occupied.")
        except:
            print("Invalid input. Enter two numbers 0-2 separated by a comma.")


def Ocomputer_move(): #r = row, c = col - column
    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty:
        row, col = random.choice(empty)
        board[row][col] = "O"
        print(f"Player O | Please entered: {row},{col}")

def welcome():
    print("\nWelcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:\n")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 40)
    print("Let's start the game")
    print("-" * 40)

welcome()

for _ in range(5):
    print_board()
    Xplayer_move()

    if check_win("X"):
        print_board()
        print("Congratulations, you WON!🎉")
        break

    Ocomputer_move() 

    if check_win("0"):
        print_board()
        print("TOO BAD, you lost")
        break

    elif all(board[r][c] != " " for r in range(3) for c in range(3)):
        print_board()
        print("DRAW")
        break