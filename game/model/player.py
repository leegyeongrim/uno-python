from game.model.deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hands = None
    
    def deal(self, cards):
        self.hands = cards

    # 카드를 가져옴
    def draw(self, card):
        self.hands.append(card)

    # 카드를 냄
    def play(self, idx):
        # TODO: 개수 체크
        return self.hands.pop(idx)
    
    def press_uno(self):
        pass
    
class Computer(Player):
    def init_hands(self, hands):
        self.hands= hands

    # 덱에서 카드를 가져옴
    def draw(self, card):
        self.hands.append(card)

    # 카드를 냄
    def play(self, idx):
        return self.hands.pop(idx)
    
    # TODO: 우노 버튼을 누름
    def press_uno(self):
        pass