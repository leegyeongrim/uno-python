from __future__ import annotations
from typing import TYPE_CHECKING
from game.model.computer import Computer
if TYPE_CHECKING:
   from game.game import UnoGame



class RegionB:
   def __init__(self, game: UnoGame):
      self.game = game
      self.computers = [Computer(f"Computer{i}") for i in range(3)]


   def init(self):
      self.game.players.extend(self.computers)

      cnt = len(self.game.deck.cards) // len(self.game.players)
      self.game.deal(cnt)