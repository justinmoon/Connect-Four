from random import random
from math import floor

class Player:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.wins = 0
        self.next = None

class RowError(Exception):
    pass

def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
class Game:

    def __init__(self, players):
        self.first_game = True
        self.players = players        
        self.initialize_state()
        self.set_player_positions()
        # I choose the board to be a property of the game because ...
        self.board = Board(self.state)
        self.compliments = ["are perhaps the greatest ever to play this game","are a Hercules of thought",
                    "conquered the eternal fount of Glory", "strike fear in the heart of the enemy", 
                    "are peerless in cunning, strategy and tactics"]

    # Methods to help initialize the game
    def initialize_state(self):
        self.state = [[" " for x in xrange(7)] for x in xrange(6)]

    def set_player_positions(self):
        """ Generate 0 or 1 with equal probability, then assign the player 
        at that index to go """
        random_num = int(floor(random() + 0.5))
        self.current_player = self.players[random_num]

    def get_input(self, message):
        """ Convenience method for taking input. Also allows player to quit. 
        """ 
        input = raw_input(self.current_player.name + message)
        if input.upper() == 'Q':
            print "\nGoodbye!\n"
            exit()
        else:
            return input

    def place_piece(self, column):
        """ places a piece. This will of course raise IndexErrors, ValueErrors,
        and TypeErrors when incorrect indices are entered, but it will also 
        raise a RowError if all entries in chose column are full. """
        for i in range(5,-1,-1):
            if self.state[i][column] == " ":
                self.state[i][column] = self.current_player.mark
                return
        raise RowError("This column is full.")

    def move_by_column(self):
        """ JOE -- HELP!!! """
        col_input = self.get_input(", Select a column to drop your piece: ")
        x = True
        while x:
            try:
                col_index = int(col_input) - 1
                self.place_piece(col_index)
                x = False
            except (IndexError, ValueError, TypeError):
                col_input = self.get_input(
                        ", Please enter a number between 1 and 7: ")
            except RowError:
                col_input = self.get_input(
                        ", That column is full. Please enter another: ")
        
    def play_game(self):
        """ this function executes the gameplay of phase of this script. """
        while not self.game_over():
            self.board.print_board(self.state)
            print ""
            self.move_by_column()
            if not self.game_over():
                print "\n    " + self.current_player.name + " has moved. " + \
                        self.current_player.next.name + " is up."
                print ""
                self.current_player = self.current_player.next
        self.board.print_board(self.state)

    def horizontal_winner(self):
        """ Checks for horizontal winning combinations. """
        for row in range(6):
            for col in range(4):
                condition_one = self.state[row][col] != " "
                condition_two = len(set(self.state[row][col:col+4])) == 1
                if (condition_one) and (condition_two):
                    return True
        return False

    def vertical_winner(self):
        """ Checks for vertical winning combinations. """
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

    def diagonal_winner(self):
        """ Checks for diagonal winning combinations. """
        row_range = range(5,-1,-1)
        col_range = range(7)
        for row in row_range:
            for col in col_range:
                # Checks diagonals from lower right to upper left
                if (row-3 in row_range) and (col+3 in col_range):
                    list = []
                    for i in range(4):
                        list.append(self.state[row-i][col+i])
                    if (self.state[row][col] != " ") and (len(set(list)) == 1):
                        return True
                # Checks diagonals from lower left to upper right
                if (row-3 in row_range) and (col-3 in col_range):
                    list = []
                    for i in range(4):
                        list.append(self.state[row-i][col-i])
                    if (self.state[row][col] != " ") and (len(set(list)) == 1):
                        return True
        return False

    # def NW_diagonal_winner(self):
    #     """ Checks for winners moving from bottom left to top right: 
    #     to North West Direction """
    #     row_range = range(5,-1,-1)
    #     col_range = range(7)
    #     for row in row_range:
    #         for col in col_range:
    #             if (row-3 in row_range) and (col-3 in col_range):
    #                 list = []
    #                 for i in range(4):
    #                     list.append(self.state[row-i][col-i])
    #                 if (self.state[row][col] != " ") and (len(set(list)) == 1):
    #                     return True
    #     return False

    def game_over(self):
        """ This method will declare a winner. """
        top_row = self.state[0][:]
        if " " not in top_row:
            return "draw"
        elif self.horizontal_winner() or self.vertical_winner() \
                        or self.diagonal_winner():
            return "winner"
        else: 
            return False

    def ending_messages(self):
        """ this function seems unnecessary . . . """
        if self.game_over() == "draw":
            return "There has been a draw."
        if self.game_over() == "winner": 
            # UGLY
            self.current_player.wins += 1
            random_num = int(floor(random()*5))
            return "\nCongrats {0}, you ".format(self.current_player.name) + \
                    self.compliments[random_num] + "!"

    def wrapup(self):
        """ Check if players wish to continue:
            restarts the game if 'yes'
            quits the game if 'no' """
        print self.ending_messages()
        print ""
        self.board.print_scoreboard(players)
        again = ""            
        while again not in ["Y","N"]:
            print ""
            again = raw_input("Would you like to play again? (Y/N): ").upper()
        if again == "Y":
            self.first_game = False
            self.current_player = self.current_player.next
            self.initialize_state()
            print ""
            self.run()
            # self.run(first_game = False, current_player = self.current_player.next)
        else:
            print "\nGoodbye!\n"

    def run(self):
        """ Runs the game """
        self.play_game()
        self.wrapup()


class Board:
    """ This class handles the display & printing of the board. """
    
    def __init__(self, state):
        self.game_board = self.generate_game_board(state)
        self.divider = self.generate_divider()
        self.column_numbers = self.generate_column_numbers()

    def generate_game_board(self, game_state):
        """ generates a string representing the 'gameplay board' where 'pieces' are 'dropped'.
        It converts the Game.state array into a printable string """
        body = ""
        for row in game_state:
            this_row = "   |"
            for entry in row:
                this_row += "| " + entry + " |"
            body += this_row + "|\n"
        return body[:-1] 


    def generate_divider(self):
        """ this generates a line of dashes separating the 'gameplay board' from the 'column labels'. """
        return "   " + "-"*37

    def generate_column_numbers(self):
        """ this generates a the 'column labels' (ranging from 1 to 7) at the bottom. """
        column_numbers = "   |"
        for x in xrange(7):
            column_numbers += "| " + str(x+1) + " |"
        return column_numbers + "|"

    def print_board(self, state):
        """ prints all 3 parts of board: the 'game board', 'divider', 'column labels' """
        print self.generate_game_board(state)
        print self.divider
        print self.column_numbers

    def print_scoreboard(self, players):
        """ prints a scoreboard tabulating wins and losses """
        win0, win1 = " win", " win"   
        if players[0].wins != 1:
            win0 = " wins"
        if players[1].wins != 1:
            win1 = " wins"
        print " "*15 + "Scoreboard:"    
        print " "*15 + players[0].name + ": " + str(players[0].wins) + win0
        print " "*15 + players[1].name + ": " + str(players[1].wins) + win1

def collect_players():
    """ This is a function to """

    print "\nWelcome to 'Connect 4 by Moen'\n"
    print "Enter Q at any time to exit the game.\n"
    marks = ["X","O"]
    players = []

    player_1_name = raw_input("Player " + str(len(players) + 1) + ", please enter your name: ").capitalize()
    print ""
    player_1_mark = raw_input(player_1_name + ", would you like to be X's or O's? ").upper()
    while player_1_mark not in marks:
        print ""
        player_1_mark = raw_input(player_1_name + ", enter X or O: ").upper()
    print ""
    player_1 = Player(player_1_name,player_1_mark)
    

    player_2_name = raw_input("Player " + str(len(players) + 1) + ", please enter your name: ").capitalize()
    print ""

    player_2_mark = marks[(marks.index(player_1_mark) + 1) % 2]
    player_2 = Player(player_2_name, player_2_mark)

    player_1.next = player_2
    player_2.next = player_1

    players.append(player_1)
    players.append(player_2)

    return players


if __name__ == "__main__":
    
    players = collect_players()
    game = Game(players)
    print "{0} will control the {1}'s and {2} will control the {3}'s\n".format(
            game.players[0].name, game.players[0].mark, game.players[1].name, game.players[1].mark)
    game.run()
