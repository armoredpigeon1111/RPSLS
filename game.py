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
        self.get_game_winner()
        
        

    def welcome_message(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock game!')

    def display_rules(self):
        print('\nEach player choses one gesture from the list\n Rock crushes Scissors\n Scissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard\n Lizard eats Paper\n Paper disproves Spock\n Spock vaporizes Rock')

    def game_type(self):
        validation = False
        while validation is False:
            user_choice = int(input('\nPlay a single player game or two player game? type "1" for single and "2" for multi: '))
            if user_choice == 1 or user_choice == 2:
                validation = True
            else:
                print('Please choose either "1" or "2"')
        if user_choice == 1:
            self.player_two = Ai()
        else:
            self.player_two = Human()

    def game_rounds(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            p1_gesture = self.player_one.choose_gesture()
            p2_gesture = self.player_two.choose_gesture()
            print(f'{self.player_one.name} chose {p1_gesture}.')
            print(f'{self.player_two.name} chose {p2_gesture}.')

            self.choose_round_winner(p1_gesture, p2_gesture)
            

    def choose_round_winner(self, p1_gesture, p2_gesture):
        if p1_gesture == "Rock":
            if(p2_gesture == "Rock"):
                print("tie")
            elif(p2_gesture == "Paper" or p2_gesture == "Spock"):
                self.player_two.set_score()
                print(self.player_two.name + " wins round")
            elif(p2_gesture == "Scissors" or p2_gesture == "Lizard"):
                self.player_one.set_score()
                print(self.player_one.name + " wins round")
        elif p1_gesture == "Paper":
            if(p2_gesture == "Rock" or p2_gesture == "Spock"):
                self.player_one.set_score()
                print(self.player_one.name + " wins round")
            elif(p2_gesture == "Paper"):
                print("tie")
            elif(p2_gesture == "Scissors" or p2_gesture == "Lizard"):
                self.player_two.set_score()
                print(self.player_two.name + " wins round")
        elif p1_gesture == "Scissors":
            if(p2_gesture == "Paper" or p2_gesture == "Lizard"):
                self.player_one.set_score
                print(self.player_one.name + " wins round")
            elif(p2_gesture == "Rock" or p2_gesture == "Spock"):
                self.player_two.set_score()
                print(self.player_two.name +" wins")
            elif(p2_gesture == "Scissors"):
                print("tie")
        elif p1_gesture == "Lizard":
            if(p2_gesture == "Rock" or p2_gesture == "Scissors"):
                self.player_two.set_score()
                print(self.player_two.name +" wins round")
            elif(p2_gesture == "Paper" or p2_gesture == "Spock"):
                self.player_one.set_score()
                print(self.player_one.name + " wins round")
            elif(p2_gesture == "Lizard"):
                print("tie")
        elif p1_gesture == "Spock":
            if(p2_gesture == "Rock" or p2_gesture == "Scissors"):
                self.player_one.set_score()
                print(self.player_one.name + " wins round")
            elif(p2_gesture == "Paper" or p2_gesture == "Lizard"):
                self.player_two.set_score()
                print(self.player_two.name + " wins round")
            elif(p2_gesture == "Spock"):
                print("tie")

    
    def get_game_winner(self):
        if(self.player_one.score == 2):
            print(self.player_one.name + " Wins!")
        else:
            print(self.player_two.name + " Wins!")