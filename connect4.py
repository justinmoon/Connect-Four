from random import random
from math import floor

""" 
add an option to abort at any time by entering draw, making both players agree

have the program keep track of games won in a match

have a match class, which could have a tournament subclass
the match class could take in player names and store the games-won tally

 """


class Player:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.wins = 0
        self.next = None
        # we just need to define self.next

        # if len(players) == 1:
        #     self.next = players[0]
        #     players[0].next = self
        # else:
        #     self.next = None    
        # players.append(self)

class RowError(Exception):
    def __init__(self, value):
        self.value = value



initial_state = [[" " for x in xrange(7)] for x in xrange(6)]


class Game:

    def __init__(self, first_game=True, current_player=None):
        self.first_game = first_game
        self.players = []
        self.available_marks = ["X","O"]
        self.state = initial_state
        # fix . . . 
        self.current_player = current_player
        
        # I choose the board to be a property of the game because 

        self.board = Board()

        # self.board.game_board = self.generate_game_board(self.state)
        # self.board.divider = self.generate_divider()
        # self.board.column_numbers = self.generate_column_numbers

    def collect_players_function(self):
        """ This is a function to  """

        new_player_name = raw_input("Player " + str(len(self.players) + 1) + ", please enter your name: ").capitalize()
        print ""
        if len(self.players) == 0:
            # TRYYYYYYY!!!!!
            new_player_mark = raw_input(new_player_name + ", would you like to be X's or O's? ").upper()
            while new_player_mark not in self.available_marks:
                print ""
                new_player_mark = raw_input(new_player_name + ", enter X or O: ").upper()
            self.available_marks.remove(new_player_mark)
        else:
            new_player_mark = self.available_marks[0]
        
        new_player = Player(new_player_name,new_player_mark)
        return new_player

    def collect_players_phase(self):
        """  """
        if self.first_game == True and self.current_player == None:
            self.available_marks = ["X","O"]
            self.players.append(self.collect_players_function())
            print ""
            self.players.append(self.collect_players_function())
            print ""
                # set this equal to "player"
                # self.player.append(player)
            print "{0} will control the {1}'s and {2} will control the {3}'s\n".format(
                        self.players[0].name, self.players[0].mark, self.players[1].name, self.players[1].mark)
        else:
           self.board.print_scoreboard()
           print ""
        return

    def set_current_player(self):
        """ Generate 0 or 1 with equal probability, then assign the player at that index to go """
        # if len(self.players) == 1:


        random_num = int(floor(random() + 0.5))
        self.current_player = self.players[random_num]
        return

    def get_input(self, message):
        """ IS THIS NECESSARY. ALMOST SEEMS STUPID... """ 
        return raw_input(self.current_player.name + message)

    def loop_until_valid_input(self):
        """ JOE -- HELP!!! """
        raw_column_input = self.get_input(", Select a column to drop your piece: ")
        x = True
        while x:
            try:
                if raw_column_input in range(1,8,1): 
                    x = False
            except (IndexError, ValueError):
                raw_column_input = raw_input(self.current_player.name + ", Please enter a number between 1 and 7: ")
            except RowError:
                raw_column_input = raw_input(self.current_player.name + ", That column is full. Please enter another: ")
        # converting from 1-7 'diaplayed' indices to 0-6 'list' indices 
        return int(raw_column_input) - 1

    def place_pieces_by_column(self, column):
        """  """
        for i in range(5,-1,-1):
            if self.state[i][column] == " ":
                self.state[i][column] = self.current_player.mark
                break

    def move_by_column(self):
        """ Player chooses a column. Piece is dropped into place. """
        column = self.loop_until_valid_input()
        self.place_pieces_by_column(column)
        return
        
    def play_game(self):
        """ this function executes the gameplay of phase of this script. """
        while not self.game_over():
            self.board.print_board()
            self.move_by_column()
            print "\n    " + self.current_player.name + " has moved. " + self.current_player.next.name + " is up."
            print ""
            self.current_player = self.current_player.next

        self.board.game_board.print_board()
        return


    def horizontal_winner(self):
        """ Checks for horizontal winners. 





        These all Return winning player or false/none ??? 






        """
        for row in range(6):
            for col in range(4):
                condition_one = self.state[row][col] != " "
                condition_two = len(set(self.state[row][col:col+4])) == 1
                if (condition_one) and (condition_two):
                    return True
        return False

    def vertical_winner(self):
        """ Checks for vertical winners. """

        for col in range(7):
            for row in range(3):
                list = []
                for i in range(4):
                    list.append(self.state[row+i][col])
                
                condition_one = self.state[row][col] != " "
                condition_two = len(set(list)) == 1
                
                if (condition_one) and (condition_two):
                    return True

        return False

    # remake these with 1 base function and pass in East or West which are 
    # passed into a dictionary and converted into +/- and passed into base function

    def NE_diagonal_winner(self):
        """ Checks for winners moving from bottom left to top right: 
        to North East Direction """
        row_range = range(5,-1,-1)
        col_range = range(7)
        for row in row_range:
            for col in col_range:
                if (row-3 in row_range) and (col+3 in col_range):
                    list = []
                    for i in range(4):
                        list.append(self.state[row-i][col+i])
                    if (self.state[row][col] != " ") and (len(set(list)) == 1):
                        return True
        return False

    def NW_diagonal_winner(self):
        """ Checks for winners moving from bottom left to top right: 
        to North West Direction """
        row_range = range(5,-1,-1)
        col_range = range(7)
        for row in row_range:
            for col in col_range:
                if (row-3 in row_range) and (col-3 in col_range):
                    list = []
                    for i in range(4):
                        list.append(self.state[row-i][col-i])
                    if (self.state[row][col] != " ") and (len(set(list)) == 1):
                        return True
        return False

    def game_over(self):
        """ This method will declare a winner. """
        top_row = self.state[0][:]
        if " " not in top_row:
            return "draw"
        elif self.horizontal_winner() or self.vertical_winner() \
                        or self.NE_diagonal_winner() or self.NE_diagonal_winner():
            return "winner"
        else: 
            return False

    def over_or_not(self):
        """  """
        if self.game_over() == "draw":
            print "There has been a draw."
        if self.game_over() == "winner": 
            print "\n{0} is the winner. congrats.".format(self.current_player.next.name)
            self.current_player.next.wins += 1



    def wrapup(self):
        """ Check if players wish to continue:
            restarts the game if 'yes'
            quits the game if 'no' """
        again = ""            
        while again not in ["Y","N"]:
            again = raw_input("Would you like to play again? (Y/N): ").upper()
        if again == "Y":
            self.run(first_game = False, current_player = self.current_player.next)
        else:
            print "goodbye"
        return

    def run(self, first_game=True, current_player=None):

        print "\n   Welcome to 'Connect 4 by Moen'\n"

        self.collect_players_phase()

        # for player in self.players:
        #     print player.name

        self.set_current_player()



        self.play_game()

        # make this display_results at the end
        self.board.print_board()

        self.wrapup()
        return


class Board:
    """ This class handles the display & printing of the board. """
    
    def __init__(self, state=initial_state):
        self.game_board = self.generate_game_board(state)
        self.divider = self.generate_divider()
        self.column_numbers = self.generate_column_numbers

    def generate_game_board(self, game_state):
        """ generates a string representing the 'gameplay board' where 'pieces' are 'dropped'.
        It converts the Game.state array into a printable string """
        body = ""
        for row in game_state:
            this_row = "   |"
            for entry in row:
                this_row += "| " + entry + " |"
            body += this_row + "|\n"
        return body 


    def generate_divider(self):
        """ this generates a line of dashes separating the 'gameplay board' from the 'column labels'. """
        return "   " + "-"*37

    def generate_column_numbers(self):
        """ this generates a the 'column labels' (ranging from 1 to 7) at the bottom. """
        column_numbers = "   |"
        for x in xrange(7):
            column_numbers += "| " + str(x+1) + " |"
        return column_numbers + "|"

    def print_board(self):
        """ prints all 3 parts of board: the 'game board', 'divider', 'column labels' """
        print self.game_board
        print self.divider
        print self.column_numbers
        return

    def print_scoreboard(self):
        """ prints a scoreboard tabulating wins and losses """
        win0, win1 = " win", " win"   
        if self.players[0].wins > 1:
            win0 = " wins"
        if self.players[1].wins > 1:
            win1 = " wins"
        print " "*15 + "Scoreboard:"    
        print " "*15 + self.players[0].name + ": " + str(self.players[0].wins) + win0
        print " "*15 + self.players[1].name + ": " + str(self.players[1].wins) + win1
        return

    

if __name__ == "__main__":
    game = Game()
    game.run()
