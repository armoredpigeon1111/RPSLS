from player import Player
from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None


    def run_game(self):
        pass

    def welcome_message(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock game!')

    def display_rules(self):
        print('Each player choses one gesture from the list\n Rock crushes Scissors\n Scissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard\n Lizard eats Paper\n Paper disproves Spock\n Spock vaporizes Rock')

    def game_type(self):
        user_choice = input('Play a single player game or two player game? type "1" for single and "2" for multi ')
        if user_choice == 1:
            self.player_two = Ai()
        else:
            self.player_two = Human()

    def game_rounds(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.chosen_gesture()
            self.player_two.chosen_gesture()

    
