from card import Card
import random

class Deck:
    def __init__(self, cards): #cards; card의 리스트
        self.cards = cards
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop()

color = [None,'red','yellow','green','blue']
value = [i for i in range(1,10)] + ["jump", "back", "+2", "-1", "omt", "+4"] #omt; 1번더
cards=[Card(color[0],value[-1])]
for c in color[1:]:
    for v in value[:14]:
        cards.append(Card(c,v))

