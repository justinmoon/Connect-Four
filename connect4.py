

game_board = [["|   |" for x in xrange(7)] for x in xrange(6)]


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

def move_by_column(col):
	""" User chooses a column. Piece is dropped into place. """


game_board[1][4] = "| x |"

print_board(game_board, 1)
# print_board(game_board, 0)
