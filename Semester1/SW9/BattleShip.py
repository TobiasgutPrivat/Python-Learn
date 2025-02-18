import random

board = [["O" for i in range(5)] for j in range(5)]
guessBoard = [["O" for i in range(5)] for j in range(5)]
board[random.randint(0, 4)][random.randint(0, 4)] = "s"

def inputValidated(text: str, validate: callable) -> str:
    while True:
        value = input(text)
        if validate(value):
            return value
        else:
            print("Invalid input")

def printBoard(board):
    print("Your board:")
    print("  " + " ".join([str(i) for i in range(1, len(board[0])+1)]))
    for j in range(len(board)):
        print(f"{j + 1} " + " ".join([board[i][j] for i in range(len(board[0]))]))
    print()

for guess in range(10):
    printBoard(guessBoard)
    row = int(inputValidated("Enter the row: ",lambda x: x.isdigit() and 1 <= int(x) <= len(board[0]))) -1
    col = int(inputValidated("Enter the column: ",lambda x: x.isdigit() and 1 <= int(x) <= len(board))) -1

    if board[col][row] == "s":
        print("You hit a ship!")
        guessBoard[col][row] = "\033[1;91mS\033[0m"
        printBoard(guessBoard)
        break
    else:
        guessBoard[col][row] = "X"
        print("You missed.")
    print()
