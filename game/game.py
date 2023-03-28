from game.model.player import *
from game.model.deck import Deck
from game.model.card import *
from util.globals import *
import random
import time

class UnoGame:
    def __init__(self):
        self.init()

        self.turn_time = 10 # 턴 시간 (초단위)
        self.turn_start_time = time.time()

    # 게임 시작
    def init(self):
        self.reverse_direction = True
        self.current_player_index = 0
        self.board_player_index = 0
        self.turn_counter=0         #지금까지 지난 게임 턴수를 셈
        self.players: list[Player] = []
        self.add_player("YOU")
        self.deck = Deck()

        self.deal()

        self.current_card: Card = self.deck.draw()

    def add_player(self, name):
        self.players.append(Player(name))

    def add_computer(self, name): #computer 추가
      self.players.append(Computer(name))

    # 다음 턴
    def next_turn(self, turn = 1):
        direction = -turn if self.reverse_direction else turn
        print(direction)
        self.current_player_index = (self.current_player_index + direction) % len(self.players)
        self.reset_turn_start_time()
        self.turn_counter+=1 #턴수를 세기 위함

    # 현재 플레이어 반환
    def get_current_player(self):
        return self.players[self.current_player_index]
    
    def get_board_player(self):
        return self.players[self.board_player_index]
    
    def draw(self):
        self.get_current_player().draw(self.deck.draw())

    def play(self, idx):
        self.set_current_card(self.get_current_player().play(idx))
        self.next_turn()
        self.reset_turn_start_time()
    
    def reset_turn_start_time(self):
        self.turn_start_time = time.time()

    # 다음 턴 스킵 : 
    def skip_turn(self, skip = 1):
        self.next_turn(skip + 1)

    # 턴 이동 방향 변경
    def toggle_turn_direction(self):
        self.reverse_direction = not self.reverse_direction

    # 카드 분배
    def deal(self, n = 7):
        for player in self.players:
            player.deal(self.deck.deal(n))

    # 플레이어에게 패널티 카드 n장 부여
    def penalty(self, player_index, n):
        for _ in range(n):
            self.players[player_index].draw(self.deck.draw())

    # 현재 카드 변경
    def set_current_card(self, card):
        self.current_card = card

    # 카드 검증
    def verify_new_card(self, new_card: Card) -> bool:
        # TODO: 색상 카드 선택 시 다음 플레이어는 바뀐 색의 카드나 또 다른 색 변경 카드만 낼 수 있음
        if self.current_card.value == SKILL_COLOR:
            if new_card.color == CARD_COLOR_NONE:
                return new_card.value == SKILL_COLOR
            
        # 이전 카드가 미색상 기술 카드이면서 새로운 카드가 미색상 카드가 아닌 경우 
        return self.current_card.color == CARD_COLOR_NONE or \
            new_card.color == CARD_COLOR_NONE or \
            self.current_card.color == new_card.color or \
            self.current_card.value == new_card.value

        

    # TODO: 우노 버튼 클릭
    def click_uno(self, idx):
        pass
    
    # TODO: 게임이 끝났는지 확인
    def is_game_over(self) -> bool:
        for idx, player_hands in enumerate([player.hands for player in self.players]):
            if len(player_hands) == 0:
                self.set_winner(self.players[idx])
                return True
        return False
    
    def set_winner(self, player):
        self.winner = player
    
    # TODO: 승자 확인
    def get_winner(self) -> Player:
        return self.winner

    # TODO: 특별 카드 실행
    # SKILL_JUMP 수행
    def runJUMP(self):
        self.skip_turn() #다음차례 턴이 skip
    # SKILL_REVERSE 수행
    def runREVERSE(self):    
        self.toggle_turn_direction()
    # SKILL_runPLUS_2 수행
    def runPLUS_2(self):    
        if self.reverse_direction:
            self.penalty(self.current_player_index+1,2) 
        else:
            self.penalty(self.current_player_index-1,2)
    # SKILL_MINUS_1 수행
    def runMINUS_1(self):
        card_idx=random.randint(0,len(self.players[self.current_player_index].hands)-1)
        self.players[self.current_player_index].hands.pop(card_idx)
    # SKILL_OMIT 수행
    def runOMIT(self):
        if self.reverse_direction: #정방향이면
            self.current_player_index-=1 #미리 index 감소시켜놓고, next_turn 수행시 다시 자기 차례로 돌아오게함 
        else: #역방향이면
            self.current_player_index-=1 #미리 index 증가시켜놓고, next_turn 수행시 다시 자기 차례로 돌아오게함
    # SKILL_runPLUS_4 수행
    def runPLUS_4(self):
        if self.reverse_direction:
            self.penalty(self.current_player_index+1,4)
        else:
            self.penalty(self.current_player_index-1,4)
    # SKILL_COLOR 수행
    def runCOLOR(self, idx):
        self.current_card.color=CARD_COLOR_SET[idx]
        
    
game = UnoGame()
game.init()


