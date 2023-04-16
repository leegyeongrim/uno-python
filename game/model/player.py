import random

from game.game import UnoGame
from game.model.deck import Deck
from util.globals import *

class Player:
    def __init__(self, name):
        self.name = name
        self.hands = []
    
    def deal(self, cards):
        self.hands = cards

    # 카드를 가져옴
    def draw(self, card):
        self.hands.append(card)

    # 카드를 냄
    def play(self, game, idx):
        return self.hands.pop(idx)
    
    def press_uno(self):
        pass


class Computer(Player):

    def __init__(self, name):
        super().__init__(name)

    def to_play(self, game):
        temp = [card for card in self.hands if game.verify_new_card(card)]
        if len(temp) > 0:
            card = random.choice(temp)
        else:
            return None
        return self.hands.index(card)
