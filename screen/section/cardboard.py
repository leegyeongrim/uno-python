from __future__ import annotations
from typing import TYPE_CHECKING

from util.globals import *
import time
import pygame

if TYPE_CHECKING:
    from game.game import UnoGame

class CardBoard:
    def __init__(self, parent):
        self.ctr = parent

        self.game: UnoGame = parent.game
        self.board = parent.board


    def init(self, width, height):
        self.card_width = get_card_width(1.5)
        self.card_height = get_card_height(1.5)

        self.background_rect = pygame.Rect(0, self.board.background_rect.bottom, self.board.background_rect.right, height)

        self.card_highlight = pygame.Surface((self.card_width, self.card_height), pygame.SRCALPHA)
        self.card_highlight.fill(COLOR_TRANSPARENT_WHITE)



        return self
    
    def draw(self, screen):
        pygame.draw.rect(screen, COLOR_PLAYER, self.background_rect)
        
        if self.game.board_player_index == self.game.current_player_index:
            self.timer = get_medium_font().render(str(int(self.ctr.turn_time + 1 - (time.time() - self.ctr.turn_start_time))), True, COLOR_RED)
            self.timer_rect = (self.background_rect.right - self.timer.get_width() - get_small_margin(), self.background_rect.top)
            screen.blit(self.timer, self.timer_rect)
            pygame.draw.rect(screen, COLOR_RED, self.background_rect, 2)

        self.draw_my_cards(screen, self.game.get_board_player().hands)
        for idx, rect in enumerate(self.card_rects):
            screen.blit(get_card_back(1.5), rect)

            # 하이라이트
            if self.ctr.my_cards_select_enabled and not self.ctr.deck_select_enabled and idx == self.ctr.my_cards_selected_index:
                screen.blit(self.card_highlight, rect)

        txt_card_cnt = get_medium_font().render(str(len(self.card_rects)), True, COLOR_BLACK)
        screen.blit(txt_card_cnt, self.background_rect)



    # 나의 카드
    def draw_my_cards(self, screen: pygame.Surface, cards):

        # 카드 레이아웃 (충돌 감지 목적)
        self.card_rects = []
        temp_card_rects = []


        # 카드 시작 좌표
        start_x = get_extra_small_margin()
        self.next_card_start_y = screen.get_height() - self.card_height - get_extra_small_margin()

        temp_idx = 0

        for idx, card in enumerate(cards):

            # 카드가 보드 넘어가는 경우 위로 쌓음
            if start_x + (self.card_width + get_extra_small_margin()) * (idx - temp_idx) + self.card_width >= self.board.background_rect.width:
                self.next_card_start_y -= self.card_height + get_extra_small_margin()

                if temp_idx == 0:
                    self.cards_line_size = idx
                
                temp_idx = idx
        

            # 카드 시작 위치
            self.next_card_start_x = start_x + (self.card_width + get_extra_small_margin()) * (idx - temp_idx)

            card_rect = pygame.Rect(self.next_card_start_x, self.next_card_start_y, self.card_width, self.card_height)
            temp_card_rects.append(card_rect)

        self.card_rects = temp_card_rects


        # 카드 개수 표시
