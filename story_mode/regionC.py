from game.game import UnoGame
from util.globals import *
import random

class regionC:
   def __init__(self):
      self.game=UnoGame()
      self.game.add_computer("computer1")
      self.game.add_computer("computer2")

   def color_change(self): #5턴 마다 낼 수 있는 카드 색상 변화
      idx=random.randint(0,len(CARD_COLOR_SET)-1)
      if self.game.turn_counter%5==0 and self.game.turn_counter!=0:
         self.game.current_card.color=CARD_COLOR_SET[idx]
   
