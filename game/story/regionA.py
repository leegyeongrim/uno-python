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

      self.example=[] #TODO: computer1의 hands로 바꿔야함 -> game.py에서 deal함수 구분후에 수정필요.
      self.func_list=[] #기술카드만 모은 list
      self.num_list=[] #숫자카드만 모은 list

   def init(self):
      self.computer = Computer('Computer0')
      self.game.players.append(self.computer)
      self.computer_deal(7)

   # 카드 기술,숫자로 분리
   def split_cards(self):
      cards = self.game.deck.cards
      for i in range(len(cards)):
         if type(cards[i].value)==int: #숫자카드 분리
            self.num_list.append(cards[i])
         else: #기술카드 분리
            self.func_list.append(cards[i])

   def computer_deal(self, n): #computer가 처음 기술카드 더 많이 갖게 deal (n장 받음)
      
      self.split_cards()

      sample=[0,0,1,1,1]

      random.shuffle(self.func_list)
      random.shuffle(self.num_list)

      for _ in range(n):
         idx = random.randint(0,len(sample)-1) #무작위 뽑기
         if sample[idx]: #기술카드 뽑는 경우
            self.example.append(self.func_list.pop())
         else:
            self.example.append(self.num_list.pop())

      self.computer.deal(self.example)

      self.set_deck()

      self.game.get_board_player().deal(self.game.deck.deal(7))

   # func,num pop한 결과를 cards에 반영
   def set_deck(self):
      temp = self.func_list + self.num_list
      random.shuffle(temp)
      self.game.deck.cards = temp