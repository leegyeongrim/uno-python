from __future__ import annotations

import random
from typing import TYPE_CHECKING
from game.model.computer import Computer
from util.globals import COLOR_SET

if TYPE_CHECKING:
   from game.game import UnoGame
class RegionA:
   def __init__(self, game: UnoGame):
      self.game = game

      self.example=[]


   def init(self):
      self.example=[]
      self.computer = Computer('Computer0')
      print(len(self.computer.hands))
      self.game.players.append(self.computer)
      self.computer_deal(7)
      print(len(self.computer.hands))

   def computer_deal(self, n):
      print('딜')
      for _ in range(n):
         card = self.roulette_wheel_selection(self.game.deck.cards)
         self.game.deck.cards.remove(card)
         self.example.append(card)

      self.computer.deal(self.example)
      self.game.get_board_player().deal(self.game.deck.deal(7))

   def roulette_wheel_selection(self, cards):
      non_int_values = [card for card in cards if not isinstance(card.value, int)]
      int_values = [card for card in cards if isinstance(card.value, int)]

      sample=[0,0,1,1,1]
      idx = random.randint(0, len(sample) - 1)


      if sample[idx]:
         return random.choice(non_int_values)
      else:
         return random.choice(int_values)