from game.model.card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []

        self.init_deck()

    def init_deck(self):
        self.create_cards()
        self.shuffle()

    def create_cards(self):
        color = ["None",'red','yellow','green','blue']
        value = [i for i in range(1,10)] + ["jump", "back", "+2", "-1", "omt", "+4"] #omt; 1번더
        cards=[Card(color[0],value[-1])]
        for c in color[1:]:
            for v in value[:14]:
                cards.append(Card(c,v))
        self.cards=cards
        
    def shuffle(self):
        random.shuffle(self.cards)

    # 카드 분해 TODO: 범위 체크
    def deal(self, n = 1):
        return [self.draw() for _ in range(n)]

    # 카드 드로우
    def draw(self):
        if len(self.cards) == 0:
            self.init_deck()

        return self.cards.pop()