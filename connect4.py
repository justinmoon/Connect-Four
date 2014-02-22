

game_board = [["|   |" for x in xrange(7)] for x in xrange(6)]


def other_player(player):
	""" convenience method """
	return (player + 1) % 1

def print_intro():
	""" Prints the game intro. """
	print "Two players needed to play this game."
	p1 = ""
	while p1 != 	"X" and input != "O":
		p1 = str(raw_input("Player 1: Would you like X's or O's?")).upper()

	print "Player 1: You will control the " + pi

def print_board(board, player):
	"""Prints the board. Extra bars for nicer printed columns.
	The player is the number of the player (in number for now) """
	print "\n    player " + str(player) + " has moved. Player " + str((player+1)%1) + " is up."
	print ""

	def print_board_labels():
		labels = "   |"
		for entry in ["| " + str(x+1) + " |" for x in xrange(7)]:
			labels += entry
		print labels + "|"
		divider = ""
		for i in range(len(labels) - 2):  divider += "-"
		print "   " + divider

	print_board_labels()

	for row in board:
		this_row = "   |"
		for entry in row:
			this_row += entry 
		print this_row + "|"
	print ""

def valid_input(column):
	""" convenience method """
	return column in range(1,8,1)

def valid_move(column):
	""" Checks if the entered move is valid """
	if column in range(1,8,1):
		print game_board[0][column]
		return game_board[0][column] == "|   |"
	else: 
		return False

def move_by_column(col, user):
	""" User chooses a column. Piece is dropped into place. """
	move_input = ""
	while not valid_move(move_input):
		move_input = raw_input(user + "-master: select a column to drop your piece!")
	# this is the actual index of the move in our notation (starting at 0)
	move_index = move_input - 1

def declare_winner(board):
	""" This method will declare a winner. """
	if horizontal_winner(board):
		return horizontal_winner(board)
	if vertical_winner(board):
		return vertical_winner(board)
	if left_diagonal_winner(board):
		return left_diagonal_winner(board)
	if right_diagonal_winner(board):
		return right_diagonal_winner(board)
	return False

def horizontal_winner(board):
	""" Checks for horizontal winners. 
	These all Return winning player or false/none ??? """
	pass

def vertical_winner(board):
	""" Checks for vertical winners. 
	Return's winning player or false/none ??? """
	pass

def right_diagonal_winner(board):
	""" Checks for winners moving from bottom left to top right """
	pass

def left_diagonal_winner(board):
	""" Checks for winners moving from bottom right to top left """
	pass

for i in range(6):
	game_board[i][4] = "| X |"

print_board(game_board, 1)

print valid_move(45)
print valid_move("|   |")
print valid_move(4)
print valid_move(2)

print_board(game_board, 1)
# print_board(game_board, 0)


def run():
	print_intro()
