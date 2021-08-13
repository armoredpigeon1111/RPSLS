from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.set_name()
        

    def set_name(self):
        self.name = input("what's your name? ")

    def choose_gesture(self):
        validation = False
        while validation is False:
            user_choice = int(input(f'\n{self.name} Choose your gesture: Type "1" for Rock, "2" for Paper, "3" for Scissors, "4" for Lizard or "5" for Spock: ')) -1
            if user_choice == 0 or user_choice == 1 or user_choice == 2 or user_choice == 3 or user_choice == 4:
                validation = True
            else:
                print('Please choose a number between 1 - 5')

        return self.gesture_list[user_choice]

    def set_score(self):
        self.score += 1
