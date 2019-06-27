from random import randint

from board import Board

board = Board(10)

print("Let's play Battleships!")
board.print()


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board.fields)
ship_col = random_col(board.fields)
print(ship_row)
print(ship_col)

turns = 8

for turn in range(turns):
    print("Turn", turn+1)
    guess_row = int(input("Guess Row:"))-1
    guess_col = ord(input("Guess Col:"))-65

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row >= len(board.fields) or guess_col < 0 or guess_col >= len(board.fields[0])):
            print("Oops, that's not even in the ocean.")
        elif(board.fields[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board.fields[guess_row][guess_col] = "X"
        if turn == turns-1:
            print("Game Over.")
        board.print()
