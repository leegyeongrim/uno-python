from game.model.card import Card
import random

class Deck:
    def __init__(self, cards): #cards; card의 리스트
        self.cards = cards
        
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    # def __str__(self):
    #     return f"{self.cards}"
    
    # def __repr__(self):
    #     return self.cards

