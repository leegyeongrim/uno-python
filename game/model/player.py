from game.model.deck import Deck

class Player:
    def __init__(self, hands = []):
        self.hands = hands

    # 덱에서 분배시, 카드를 받음 
    def init_hands(self, hands):
        self.hands= hands

    # 덱에서 카드를 가져옴
    def draw(self, card):
        self.hands.append(card)

    # 카드를 냄
    def play(self, idx):
        return self.hands.pop(idx)