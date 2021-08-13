from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.set_name()
        

    def set_name(self):
        self.name = input("what's your name? ")

    def choose_gesture(self):
        user_choice = int(input('\n Choose your gesture: Type "1" for Rock, "2" for Paper, "3" for Scissors, "4" for Lizard or "5" for Spock ')) -1
        return self.gesture_list[user_choice]

    def set_score(self):
        self.score += 1
