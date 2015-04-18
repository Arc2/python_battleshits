from random import randint

def create_board(row,col):
    board = []
    for x in range(row):
        board.append(["O"] * col)
    return board

board = create_board(10,10)

def print_board(board):
    a='*  '
    for i in range(len(board[0])):
	a+=chr(i+65) + ' '
    print a
    s='*+'
    for i in range(len(board[0])):
	s+='--'
    print s
    j=1
    for row in board:
	if j<10:
            print str(j) + ' |' + " ".join(row)
	else:
	    print str(j) + '|'  + " ".join(row)
	j+=1

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

turns = 8

for turn in range(turns):
    print "Turn", turn+1
    guess_row = int(raw_input("Guess Row:"))-1
    guess_col = ord(raw_input("Guess Col:"))-65

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row >= len(board) or guess_col < 0 or guess_col >= len(board[0])):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn==turns-1:
            print "Game Over."
        print_board(board)
