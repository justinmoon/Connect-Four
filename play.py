from connect4 import *




# tmp_board = game_board[:]

# tmp_board[1][1] = "| X |"

# print "this is tmp_board"
# print_board(tmp_board)

# print "this is game_board"
# print_board(game_board)

# print "-------" * 10
# print ""


# tmp_board_2 = []
# for i in range(len(game_board)):
# 	tmp_board_2.append(game_board[i][:])

# print "this is tmp_board 2"
# print_board(tmp_board_2)

# print "this is game_board 2"
# print_board(game_board)

# tmp_board_2[0][0] = "| O |"

# print "this is tmp_board 2"
# print_board(tmp_board_2)

# print "this is game_board 2"
# print_board(game_board)

def copy_board(board):
	tmp_board = []
	for i in range(len(board)):
		tmp_board.append(board[i][:])
	return tmp_board

board = copy_board(game_board)

board[5][6] = "| X |"

# print_board(board)