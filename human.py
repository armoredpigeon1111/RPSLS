from player import Player

class Human:
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = input("what's your name? ")

    def chosen_gesture(self):
        user_choice = int(input('Choose your gesture: Type "1" for Rock, "2" for Paper, "3" for Scissors, "4" for Lizard or "5" for Spock ')) -1
        self.chosen_gesture(self.gesture_list[user_choice])

    def set_score(self):
        self.score += 1
