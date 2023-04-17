from game.model.player import *
from game.model.deck import Deck
from game.model.card import *
from util.globals import *
import random
import time


class UnoGame:

    def __init__(self):
        self.is_started = False

        self.play_type = None
        self.players: list[Player] = []

        self.reverse_direction = False
        self.current_player_index = 0
        self.board_player_index = 0
        self.previous_player_index = 0
        self.turn_counter = None

        self.deck = None
        self.current_card = None
        self.turn_time = 10

        self.turn_start_time = None
        self.is_turn_start = False

        self.uno_enabled = False
        self.uno_clicked = False

    def start_game(self, play_type, players):

        self.is_started = True
        self.play_type = play_type
        self.players = players

        self.reverse_direction = False
        self.current_player_index = 0
        self.board_player_index = 0
        self.previous_player_index = None
        self.turn_counter = 1
        self.is_turn_start = False

        self.deck = Deck()
        self.deck.shuffle()
        if self.play_type == TYPE_SINGLE:
            self.deal()
        self.current_card = self.deck.draw()

        self.turn_start_time = time.time()
        self.uno_clicked = False

    def finish_game(self):
        self.players: list[Player] = []

    # 다음 턴
    def next_turn(self, turn=1):
        self.is_turn_start = True
        # 이전 플레이어 저장
        self.previous_player_index = self.current_player_index

        direction = -turn if self.reverse_direction else turn
        self.current_player_index = (self.current_player_index + direction) % len(self.players)
        self.turn_counter += 1
        self.reset_turn_start_time()

    # 현재 플레이어 반환
    def get_current_player(self):
        return self.players[self.current_player_index]
    
    def get_board_player(self):
        return self.players[self.board_player_index]

    def get_previous_player(self):
        return self.players[self.previous_player_index]
    
    def draw(self):
        self.get_current_player().draw(self.deck.draw())

    def play(self, idx=None):
        self.set_current_card(self.get_current_player().play(self, idx))
        self.next_turn()
        self.reset_turn_start_time()
    
    def reset_turn_start_time(self):
        self.turn_start_time = time.time()

    # 다음 턴 스킵 : 
    def skip_turn(self, skip=1):
        self.next_turn(skip + 1)

    # 턴 이동 방향 변경
    def toggle_turn_direction(self):
        self.reverse_direction = not self.reverse_direction

    # 카드 분배 #수정부분: idx 받아서 특정 player에게만 deal 해주기
    def deal(self, idx=None, n=7):
        for player in self.players:
            player.deal(self.deck.deal(7))

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

    def update_uno_enabled(self):
        self.uno_enabled = len(self.get_current_player().hands) == 2


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

    def get_winner(self):
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
        if self.reverse_direction: #역방향
            self.current_player_index=(self.current_player_index+1)%len(self.players) #미리 index 증가시켜놓고, next_turn 수행시 다시 자기 차례로 돌아오게함 
        else: #정방향이면
            self.current_player_index=(self.current_player_index-1)%len(self.players) #미리 index 감소시켜놓고, next_turn 수행시 다시 자기 차례로 돌아오게함
    # SKILL_runPLUS_4 수행
    def runPLUS_4(self):
        if self.reverse_direction:
            self.penalty(self.current_player_index+1,4)
        else:
            self.penalty(self.current_player_index-1,4)
    # SKILL_COLOR 수행
    def runCOLOR(self, idx):
        self.current_card.color=CARD_COLOR_SET[idx]