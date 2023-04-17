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

    DELAY = 3  # 컴퓨터 선택 딜레이
    UNO_DELAY = 2  # 플레이어가 2초 이내 우노 미클릭시 우노 버튼 클릭

    def __init__(self, name):
        super().__init__(name)

    def to_play(self, game):
        temp = [card for card in self.hands if game.verify_new_card(card)]
        if len(temp) > 0:
            card = random.choice(temp)
        else:
            return None
        return self.hands.index(card)
