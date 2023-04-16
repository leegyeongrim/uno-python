from game.game import UnoGame
from util.globals import *
import random

class regionD:
   def __init__(self):
      self.game=UnoGame()
      self.game.init()
      self.game.add_computer("computer1")
      self.tmp = 1 #컴퓨터 턴일때 한 번만 omit을 위한 변수

   def whoseturn(self):
      if self.game.players[self.game.current_player_index].isComputer:
         if self.tmp:
            self.game.runOMIT()
            self.tmp = 0
         else:
            self.tmp = 1
      else:
         pass

   def next_turn(self, turn = 1):
      self.whoseturn()
      direction = -turn if self.game.reverse_direction else turn
      #print(direction)
      self.game.current_player_index = (self.game.current_player_index + direction) % len(self.game.players)
      self.game.turn_counter+=1 #턴수를 세기 위함
      self.game.reset_turn_start_time()
