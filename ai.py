from player import Player
from random import Random

class Ai:
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = 'Player 2'

    def chosen_gesture(self):
        self.chosen_gesture = Random.randint(0, 4)

    def set_score(self):
        self.score += 1

    