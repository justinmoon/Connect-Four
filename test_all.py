import unittest
from connect4 import *

def copy_board(board):
	tmp_board = []
	for i in range(len(board)):
		tmp_board.append(board[i][:])
	return tmp_board

class Test(unittest.TestCase):



	print "gameboard\n"
	print_board(game_board)

	def setUp(self):
		pass

	def test_horizontal_winner_2(self):
		""" winner """
		tmp_board = copy_board(game_board)
		
		for i in range(4):
			tmp_board[0][i] = "| X |"

		print "horizongal test: winner"
		print_board(tmp_board)

		assert horizontal_winner(tmp_board) == True

	def test_horizontal_winner_1(self):
		""" loser """
		tmp_board = copy_board(game_board)
		
		tmp_board[0][1] = "| X |"		
		
		print "horizongal test: loser"
		print_board(tmp_board)

		assert horizontal_winner(tmp_board) == False



	def test_vertical_winner_1(self):
		""" winner """
		tmp_board = copy_board(game_board)
		
		for i in range(2,6):
			tmp_board[i][0] = "| X |"

		print "vertical test: winner # 1"
		print_board(tmp_board)		

		assert vertical_winner(tmp_board) == True

	def test_vertical_winner_2(self):
		""" loser """
		print "gameboard\n"
		tmp_board = copy_board(game_board)
		for i in range(2,5):
			tmp_board[i][0] = "| X |"
		print_board(tmp_board)
		assert vertical_winner(tmp_board) == False

	def test_NE_diagonal_winner_1(self):
		""" winner """
		board = copy_board(game_board)
		row, col = 5, 2

		for i in range(4):
			board[row-i][col+i] = "| X |"

		print "NE diagonal winner #1"
		print_board(board)

		assert NE_diagonal_winner(board) == True

	def test_NE_diagonal_winner_2(self):
		""" loser """
		board = copy_board(game_board)
		
		for i in range(2,6):
			board[i][0] = "| X |"

		print "NE diagonal loser #1"
		print_board(board)	

		assert NE_diagonal_winner(board) == False

	def test_NW_diagonal_winner_1(self):
		""" winner """
		board = copy_board(game_board)
		row, col = 5, 5

		for i in range(4):
			board[row-i][col-i] = "| X |"

		print "NW diagonal winner #1"
		print_board(board)

		assert NW_diagonal_winner(board) == True

	def test_NW_diagonal_winner_2(self):
		""" loser """
		board = copy_board(game_board)
		
		for i in range(2,6):
			board[i][6] = "| X |"

		print "NW diagonal loser #1"
		print_board(board)	

		assert NW_diagonal_winner(board) == False

if __name__ == '__main__':
	unittest.main()