from random import random
from math import floor

class Player:
    """ This class represents the players. """

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.wins = 0
        self.next = None

class RowError(Exception):
    pass

class Game:
    """ This class represents the game, and includes both an instance of the
    board object, and a list of player objects called players. """
    def __init__(self, players):
        self.first_game = True
        self.players = players        
        self.initialize_state()
        self.set_player_positions()
        self.board = Board(self.state)
        self.compliments = ["are perhaps the greatest ever to play this game",
                            "are a Hercules of thought",
                            "conquered the eternal fount of Glory", 
                            "strike fear in the heart of the enemy", 
                            "are peerless in cunning, strategy and tactics"]

    def initialize_state(self):
        """ Sets Game.state in the Games's __init()__ and resets the game's 
        state in the wrapup() function that is called after a winner is
        determined in each round of gameplay. 
        " " will represent an unoccupied space on the game board. 
        "X" will represent a space occupied by the player controlling X's.
        "O" will represent a space occupied by the player controlling O's. 
        """
        self.state = [[" " for x in xrange(7)] for x in xrange(6)]

    def set_player_positions(self):
        """ Generates 0 or 1 with equal probability, then assigns the player 
        at that index as the current_player. """
        random_num = int(floor(random() + 0.5))
        self.current_player = self.players[random_num]

    def get_input(self, message):
        """ Convenience method for taking input. """ 
        return raw_input(self.current_player.name + message)

    def place_piece(self, column):
        """ Places a piece based on user input collected in the move_by_column
        function. This will of course raise IndexErrors, ValueErrors,
        and TypeErrors when incorrect indices are entered, but it will also 
        raise a RowError if all entries in the chosen column are occupied. """
        for i in range(5,-1,-1):
            if self.state[i][column] == " ":
                self.state[i][column] = self.current_player.mark
                return
        raise RowError("This column is full.")

    def move_by_column(self):
        """ The player selects a column to drop a piece, and is forced to 
        re-enter column selections until a valid selection is made. """
        col_input = self.get_input(", Select a column to drop your piece: ")
        invalid_input = True
        while invalid_input:
            try:
                col_index = int(col_input) - 1
                self.place_piece(col_index)
                invalid_input = False
            except (IndexError, ValueError, TypeError):
                col_input = self.get_input(
                        ", Please enter a number between 1 and 7: ")
            except RowError:
                col_input = self.get_input(
                        ", That column is full. Please enter another: ")
        
    def play_game(self):
        """ This function executes the gameplay phase of this script. """
        while not self.game_over():
            self.board.print_board(self.state)
            print ""
            self.move_by_column()
            if not self.game_over():
                print "\n    " + self.current_player.name + " has moved. " + \
                        self.current_player.next.name + " is up."
                print ""
                self.current_player = self.current_player.next
            else: 
                print ""
        

    def horizontal_winner(self):
        """ Checks for horizontal winning combinations. Iterates over all 
        spaces in the first 4 left-hand columns, and returns True if that 
        entry is equal to the 3 entries to its right, and unequal to ' ' 
        which represents unoccupied spaces on the board. """
        for row in range(6):
            for col in range(4):
                not_empty = self.state[row][col] != " "
                # I separate this condition for performance considerations:
                # we don't need to build the list below if it contains an 
                # empty space -- as it often will
                if not_empty:
                    four_equivalent_pieces = len(set(
                            self.state[row][col:col+4])) == 1
                    if four_equivalent_pieces:
                        return True

        return False

    def vertical_winner(self):
        """ Checks for vertical winning combinations. Works the same as 
        horizontal_winner, but iterates over the bottom 3 columns and checks
        for runs of 4. """
        for col in range(7):
            for row in range(3):
                not_empty = self.state[row][col] != " "
                if not_empty:
                    list = []
                    for i in range(4):
                        list.append(self.state[row+i][col])
                    four_equivalent_pieces = len(set(list)) == 1
                    if four_equivalent_pieces:
                        return True
        return False

    def diagonal_winner(self):
        """ Checks for left-to-right and right-to-left diagonal winning 
        combinations. This iterates over all spaces on the board, first 
        checks whether diagonals starting from that space 'fit' on the board, 
        then build a list of the entries on that diagonal, and returns True 
        if all entries of the list are equal to eachother and unequal to " " 
        which represents an unoccupied space on the board. """
        row_range = range(5,-1,-1)
        col_range = range(7)
        for row in row_range:
            for col in col_range:
                empty = self.state[row][col] == " "
                if empty:
                    pass
                # Checks diagonals from lower right to upper left
                elif (row-3 in row_range) and (col+3 in col_range):
                    list = []
                    for i in range(4):
                        list.append(self.state[row-i][col+i])
                    if (len(set(list)) == 1):
                        return True
                # Checks diagonals from lower left to upper right
                elif (row-3 in row_range) and (col-3 in col_range):
                    list = []
                    for i in range(4):
                        list.append(self.state[row-i][col-i])
                    if (len(set(list)) == 1):
                        return True
        return False

    def game_over(self):
        """ This method will declare whether the game is over. """
        top_row = self.state[0][:]
        if self.horizontal_winner() or self.vertical_winner() \
                        or self.diagonal_winner():
            return "winner"
        elif " " not in top_row:
            return "draw"
        else: 
            return False

    def ending_messages(self):
        """ This function prints the messages after the game is over. It is
        called in the wrapup function. """
        if self.game_over() == "draw":
            return "\nThere has been a draw."
        if self.game_over() == "winner": 
            self.current_player.wins += 1
            random_num = int(floor(random()*5))
            return "\nCongrats {0}, you ".format(self.current_player.name) + \
                    self.compliments[random_num] + "!"

    def wrapup(self):
        """ Prints ending_messages and checks if players wish to play again:
            if 'yes' it restarts the game with the losing player moving first 
            if 'no' it quits the game. """
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
        else:
            print "\nGoodbye!\n"

    def run(self):
        """ Runs the game in two phases
        play_game is when the players move pieces
        wrapup is after the game is over. """
        self.play_game()
        self.board.print_board(self.state)
        self.wrapup()


class Board:
    """ This class handles the display & printing of the board. """
    
    def __init__(self, state):
        self.game_board = self.generate_game_board(state)
        self.divider = self.generate_divider()
        self.column_numbers = self.generate_column_numbers()

    def generate_game_board(self, game_state):
        """ Generates a string representing the 'game board' where 'pieces'
        are 'dropped' by converting the game_state array into a printable 
        string. """
        body = ""
        for row in game_state:
            this_row = "   |"
            for entry in row:
                this_row += "| " + entry + " |"
            body += this_row + "|\n"
        return body[:-1] 


    def generate_divider(self):
        """ this generates a line of dashes separating the 'gameplay board' 
        from the 'column labels'. """
        return "   " + "-"*37

    def generate_column_numbers(self):
        """ this generates a the 'column labels' (ranging from 1 to 7) at 
        the bottom. """
        column_numbers = "   |"
        for x in xrange(7):
            column_numbers += "| " + str(x+1) + " |"
        return column_numbers + "|"

    def print_board(self, state):
        """ prints all 3 parts of board: the 'game board', 'divider', and 
        'column labels' """
        print self.generate_game_board(state)
        print self.divider
        print self.column_numbers

    def print_scoreboard(self, players):
        """ prints a scoreboard tabulating wins and losses for both player """
        win0, win1 = " win", " win"   
        if players[0].wins != 1:
            win0 = " wins"
        if players[1].wins != 1:
            win1 = " wins"
        print " "*15 + "Scoreboard:"    
        print " "*15 + players[0].name + ": " + str(players[0].wins) + win0
        print " "*15 + players[1].name + ": " + str(players[1].wins) + win1

def collect_players():
    """ This is the first function called by the main method. 
    It collects the players and returns a list of player objects. """


    marks = ["X","O"]
    players = []

    player_1_name = raw_input("Player " + str(1) + 
                ", please enter your name: ").capitalize()
    print ""
    player_1_mark = raw_input(player_1_name + 
                ", would you like to be X's or O's? ").upper()
    while player_1_mark not in marks:
        print ""
        player_1_mark = raw_input(player_1_name + ", enter X or O: ").upper()
    print ""
    player_1 = Player(player_1_name,player_1_mark)
    

    player_2_name = raw_input("Player " + str(2) + 
                ", please enter your name: ").capitalize()
    print ""

    player_2_mark = marks[(marks.index(player_1_mark) + 1) % 2]
    player_2 = Player(player_2_name, player_2_mark)

    player_1.next = player_2
    player_2.next = player_1

    players.append(player_1)
    players.append(player_2)

    return players


if __name__ == "__main__":
    print "\nWelcome to 'Connect 4 by Moen'\n"
    players = collect_players()
    game = Game(players)
    print "{0} will control the {1}'s and {2} will control the {3}'s\n".format(
                game.players[0].name, game.players[0].mark, 
                game.players[1].name, game.players[1].mark)
    game.run()
