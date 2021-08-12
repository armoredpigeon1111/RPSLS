from player import Player
from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None


    def run_game(self):
        self.welcome_message()
        self.display_rules()
        self.game_type()
        self.game_rounds()
        
        

    def welcome_message(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock game!')

    def display_rules(self):
        print('Each player choses one gesture from the list\n Rock crushes Scissors\n Scissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard\n Lizard eats Paper\n Paper disproves Spock\n Spock vaporizes Rock')

    def game_type(self):
        user_choice = int(input('Play a single player game or two player game? type "1" for single and "2" for multi '))
        if user_choice == 1:
            self.player_two = Ai()
        else:
            self.player_two = Human()

    def game_rounds(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            p1_gesture = self.player_one.chosen_gesture()
            p2_gesture = self.player_two.chosen_gesture()

            self.choose_round_winner(p1_gesture, p2_gesture)
            

    def choose_round_winner(self, p1_gesture, p2_gesture):
        if p1_gesture == "Rock":
            if(p2_gesture == "Rock"):
                print("tie")
            elif(p2_gesture == "Paper"):
                self.player_two.set_score()
                print("Player 2 wins round")
            elif(p2_gesture == "Scissors"):
                self.player_one.set_score()
                print("Player 1 wins round")
            elif(p2_gesture == "Lizard"):
                self.player_one.set_score()
                print("Player 1 wins round")
            elif(p2_gesture == "Spock"):
                self.player_two.set_score()
                print("Player 2 wins round")
        elif p1_gesture == "Paper":
            if(p2_gesture == "Rock"):
                self.player_one.set_score()
                print("Player 1 wins round")
            elif(p2_gesture == "Paper"):
                print("tie")
            elif(p2_gesture == "Scissors"):
                self.player_two.set_score()
                print("Player 2 wins round")
            elif(p2_gesture == "Lizard"):
                self.player_two.set_score()
                print("Player 2 wins round")
            elif(p2_gesture == "Spock"):
                self.player_one.set_score
                print("Player 1 wins round")
        elif p1_gesture == "Scissors":
            if(p2_gesture == "Paper"):
                self.player_one.set_score
                print("Player 1 wins round")
            elif(p2_gesture == "Rock"):
                self.player_two.set_score()
                print("Player 2 wins")
            elif(p2_gesture == "Scissors"):
                print("tie")
            elif(p2_gesture == "Lizard"):
                self.player_one.set_score()
                print("Player 1 wins round")
            elif(p2_gesture == "Spock"):
                self.player_two.set_score()
                print("Player 2 wins round")
        elif p1_gesture == "Lizard":
            if(p2_gesture == "Rock"):
                self.player_two.set_score()
                print("Player 2 wins round")
            elif(p2_gesture == "Paper"):
                self.player_one.set_score()
                print("Player 1 wins round")
            elif(p2_gesture == "Scissors"):
                self.player_two.set_score()
                print("Player 2 wins round")
            elif(p2_gesture == "Lizard"):
                print("tie")
            elif(p2_gesture == "Spock"):
                self.player_one.set_score()
                print("Player 1 wins round") 
        elif p1_gesture == "Spock":
            if(p2_gesture == "Rock"):
                self.player_one.set_score()
                print("Player 1 wins round")
            elif(p2_gesture == "Paper"):
                self.player_two.set_score()
                print("Player 2 wins round")
            elif(p2_gesture == "Scissors"):
                self.player_one.set_score()
                print("Player 1 wins round")
            elif(p2_gesture == "Lizard"):
                self.player_two.set_score()
                print("Player 2 wins round")
            elif(p2_gesture == "Spock"):
                print("tie")

    
