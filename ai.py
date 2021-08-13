from player import Player
from random import Random

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.set_name()

    def set_name(self):
        self.name = 'Player 2'

    def choose_gesture(self):
        random = Random()
        # self.chosen_gesture =
        return self.gesture_list[random.randint(0,4)]

    def set_score(self):
        self.score += 1

    