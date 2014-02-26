from random import random
from math import floor

""" 
add an option to abort at any time by entering draw, making both players agree

have the program keep track of games won in a match

have a match class, which could have a tournament subclass
the match class could take in player names and store the games-won tally

 """


def create_board():
    return [["|   |" for x in xrange(7)] for x in xrange(6)]

players = []

class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.token = "| " + self.mark + " |"
        self.wins = 0
        if len(players) == 1:
            self.next = players[0]
            players[0].next = self
        elif len(players) > 1:
            print "too many players"
        else:
            self.next = None    
        players.append(self)

def other_player(player):
    """ convenience method """
    return (player + 1) % 1

def make_mark(mark):
    print "| %s |" % mark

def print_board(board):
    """
    Prints the board. Extra bars for nicer printed columns.
    The player is the number of the player (in number for now) 
    """

    def print_board_labels():
        """ prints the row of numbers above the game board """
        labels = "   |"
        for entry in ["| " + str(x+1) + " |" for x in xrange(7)]:
            labels += entry

        divider = ""
        for i in range(len(labels) - 2):  divider += "-"

        print "   " + divider
        print labels + "|"
        
    for row in board:
        this_row = "   |"
        for entry in row:
            this_row += entry 
        print this_row + "|"

    print_board_labels()
    print ""

def valid_input(column):
    """ convenience method """
    return column in range(1,8,1)

def valid_move(column,board):
    """ returns 0 if not valid number, 1 if not space remaining, 2 if totally valid """
    if column.isdigit():
        # converts from 1-7 indices to 0-6 indices
        column_int = int(column) -1
        if column_int in range(7):
            if board[0][column_int] == "|   |":
                return 2
            else:
                return 1
    else:
        return 0

def space_remaining(col, board):
    return board[0][col-1] == "|   |"

def move_by_column(player, board):
    """ Player chooses a column. Piece is dropped into place. """
    raw_move_input = raw_input(player.name + ", Select a column to drop your piece: ")
    validity = valid_move(raw_move_input,board)
    while not validity == 2:
        if validity == 0:
            raw_move_input = raw_input(player.name + ", Please enter a number between 1 and 7: ")
        elif validity == 1:
            raw_move_input = raw_input(player.name + ", That column is full. Please enter another: ")
        else:
            print "major system malfunction"
            return
        validity = valid_move(raw_move_input,board)

    move_index = int(raw_move_input) - 1
    # this is the actual index of the move in our notation (starting at 0)
    

    for i in range(5,-1,-1):
        if board[i][move_index] == "|   |":
            board[i][move_index] =  "| " + player.mark + " |"
            break


def game_over(board):
    """ This method will declare a winner. """
    top_row = board[0][:]
    if "|   |" not in top_row:
        return "draw"
    elif horizontal_winner(board):
        return "winner"
    elif vertical_winner(board):
        return "winner"
    elif NE_diagonal_winner(board):
        return "winner"
    elif NW_diagonal_winner(board):
        return "winner"
    else: 
        return False

def horizontal_winner(board):
    """ Checks for horizontal winners. 
    These all Return winning player or false/none ??? """
    for row in range(6):
        for col in range(4):
            condition_one = board[row][col] != "|   |"
            condition_two = len(set(board[row][col:col+4])) == 1
            if (condition_one) and (condition_two):
                return True
    return False

def vertical_winner(board):
    """ Checks for vertical winners. 
    Return's winning player or false/none ??? """

    for col in range(7):
        for row in range(3):
            list = []
            for i in range(4):
                list.append(board[row+i][col])
            
            condition_one = board[row][col] != "|   |"
            condition_two = len(set(list)) == 1
            
            if (condition_one) and (condition_two):
                return True

    return False

# remake these with 1 base function and pass in East or West which are 
# passed into a dictionary and converted into +/- and passed into base function

def NE_diagonal_winner(board):
    """ Checks for winners moving from bottom left to top right: 
    to North East Direction """
    row_range = range(5,-1,-1)
    col_range = range(7)
    for row in row_range:
        for col in col_range:
            if (row-3 in row_range) and (col+3 in col_range):
                list = []
                for i in range(4):
                    list.append(board[row-i][col+i])
                if (board[row][col] != "|   |") and (len(set(list)) == 1):
                    return True
    return False

def NW_diagonal_winner(board):
    """ Checks for winners moving from bottom left to top right: 
    to North West Direction """
    row_range = range(5,-1,-1)
    col_range = range(7)
    for row in row_range:
        for col in col_range:
            if (row-3 in row_range) and (col-3 in col_range):
                list = []
                for i in range(4):
                    list.append(board[row-i][col-i])
                if (board[row][col] != "|   |") and (len(set(list)) == 1):
                    return True
    return False



def left_diagonal_winner(board):
    """ Checks for winners moving from bottom right to top left """
    pass


def collect_players(counter, marks, players):
    new_player_name = raw_input("Player " + str(counter) + ", please enter your name: ").capitalize()
    if counter == 1:
        new_player_mark = raw_input(new_player_name + ", would you like to be X's or O's? ").upper()
        while new_player_mark not in marks:
            new_player_mark = raw_input(new_player_name + ", enter X or O: ").upper()
        marks.remove(new_player_mark)
    else:
        new_player_mark = marks[0]
    
    # this is still monkey business
    new_player = Player(new_player_name,new_player_mark)
    return

def print_scoreboard():
    win0, win1 = " win", " win"   
    if players[0].wins > 1:
        win0 = " wins"
    if players[1].wins > 1:
        win1 = " wins"

    print " "*15 + "Scoreboard:"    
    print " "*15 + players[0].name + ": " + str(players[0].wins) + win0
    print " "*15 + players[1].name + ": " + str(players[1].wins) + win1
    return

def run(first_game = True, current_player = None):

    print "\nWelcome to 'Connect 4 by Moen'\n"

    global game_board
    game_board = create_board()

    if first_game == True and current_player == None:
        # getting players
        counter = 1
        marks = ["X","O"]
        while counter < 3:
            collect_players(counter, marks, players)
            counter += 1

        print "{0} will control the {1}'s and {2} will control the {3}'s\n".format(
                    players[0].name,players[0].mark,players[1].name,players[1].mark)
        
        random_num = int(floor(random() + 0.5))
        current_player = players[random_num]
    else:
       print_scoreboard()
       print ""

    # playing game
    while not game_over(game_board):
        print_board(game_board)
        move_by_column(current_player,game_board)
        print "\n    " + current_player.name + " has moved. " + current_player.next.name + " is up."
        print ""
        current_player = current_player.next

    print_board(game_board)
    
    if game_over(game_board) == "draw":
        print "There has been a draw."
    if game_over(game_board) == "winner": 
        print "\n{0} is the winner. congrats.".format(current_player.next.name)
        current_player.next.wins += 1

    again = ""            
    while again not in ["Y","N"]:
        again = raw_input("Would you like to play again? (Y/N): ").upper()
    if again == "Y":
        run(first_game=False, current_player=current_player.next)
    elif again == "N":
        print "goodbye"
        return
    else:
        print "Something has gone horribly wrong . . . "
        return


if __name__ == "__main__":
    run()