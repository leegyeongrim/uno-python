
from game.model.computer import Computer
from util.globals import *
import random

class RegionD:
   def __init__(self, game):
      self.game = game
      self.turn_cnt = 0
      self.computers = [Computer(f"Computer{i}") for i in range(5)]

   def init(self):
      self.game.players.extend(self.computers)
