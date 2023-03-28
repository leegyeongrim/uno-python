from game.game import UnoGame
from util.globals import *
import random

class regionB:
   def __init__(self):
      self.game=UnoGame()
      self.game.add_computer("computer1")
      self.game.add_computer("computer2")
      self.game.add_computer("computer3")
      self.num=0 #player들에게 분배할 카드 수

   def num_decision(self): #player들에게 분배할 카드수 지정
      n=len(self.game.players)
      self.num=(len(self.game.deck.cards)-1)/n