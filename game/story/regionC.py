from __future__ import annotations

import random
from typing import TYPE_CHECKING
from game.model.computer import Computer
from util.globals import COLOR_SET

if TYPE_CHECKING:
   from game.game import UnoGame
class RegionC:
   def __init__(self, game: UnoGame):
      self.game = game
      self.computers = [Computer(f"Computer{i}") for i in range(2)]

   def init(self):
      self.game.players.extend(self.computers)

   def color_change(self):
      if self.game.turn_counter % 5 == 0:
         self.game.current_color = random.choice(list(COLOR_SET.keys()))
   
