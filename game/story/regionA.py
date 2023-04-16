from game.game import UnoGame
from game.model.deck import Deck
from util.globals import *
import random

class regionA:
   def __init__(self):
      self.game=UnoGame()
      self.game.init()
      self.game.add_computer("computer1")
      self.example=[] #TODO: computer1의 hands로 바꿔야함 -> game.py에서 deal함수 구분후에 수정필요.
      self.func_list=[] #기술카드만 모은 list
      self.num_list=[] #숫자카드만 모은 list
      

   def split_cards(self): #카드 기술,숫자로 분리
      cards=self.game.deck.cards
      for i in range(len(cards)):
         if type(cards[i].value)==int: #숫자카드 분리
            self.num_list.append(cards[i])
         else: #기술카드 분리
            self.func_list.append(cards[i])

   def computer_deal(self,n): #computer가 처음 기술카드 더 많이 갖게 deal (n장 받음)
      
      self.split_cards()

      sample=[0,0,1,1,1]
      random.shuffle(self.func_list)
      random.shuffle(self.num_list)

      for _ in range(n):
         idx=random.randint(0,len(sample)-1) #무작위 뽑기
         if sample[idx]: #기술카드 뽑는 경우
            self.example.append(self.func_list.pop())
         else:
            self.example.append(self.num_list.pop())
      
      for i in range(len(self.game.players)):
         if self.game.players[i].name=="computer1":
            self.game.players[i].init_hands(self.example)

   # func,num pop한 결과를 cards에 반영
   def set_deck(self):
      self.game.deck.cards=self.func_list+self.num_list