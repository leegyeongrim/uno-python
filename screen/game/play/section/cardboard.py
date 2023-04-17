from __future__ import annotations
from typing import TYPE_CHECKING

from util.globals import *
import time
import pygame

if TYPE_CHECKING:
    from game.game import UnoGame

class CardBoard:
    def __init__(self, play_screen):
        self.play_screen = play_screen

        self.game: UnoGame = play_screen.game
        self.board = play_screen.board

        self.next_card_start_x = get_extra_small_margin()
    
    def draw(self, screen):
        background_height = screen.get_height() // 3

        self.card_width = get_card_width(1.5)
        self.card_height = get_card_height(1.5)
        self.background_rect = pygame.Rect(0, screen.get_height() - background_height, self.board.background_rect.right, background_height)


        pygame.draw.rect(screen, COLOR_PLAYER, self.background_rect)

        name = get_small_font().render(self.game.get_board_player().name, True, COLOR_BLACK)
        name_rect = get_top_center_rect(name, self.background_rect, x=-name.get_width() // 2)
        screen.blit(name, name_rect)
        
        if self.game.board_player_index == self.game.current_player_index:
            self.timer = get_medium_font().render(str(int(self.game.turn_time + 1 - (time.time() - self.game.turn_start_time))), True, COLOR_RED)
            self.timer_rect = (self.background_rect.right - self.timer.get_width() - get_small_margin(), self.background_rect.top)
            screen.blit(self.timer, self.timer_rect)
            pygame.draw.rect(screen, COLOR_RED, self.background_rect, 2)

        self.draw_my_cards(screen, self.game.get_board_player().hands)
        for idx, rect in enumerate(self.card_rects):
            screen.blit(get_card(self.cards[idx], 1.5), rect)

            # 하이라이트
            if self.play_screen.card_select_enabled and not self.play_screen.deck_select_enabled and idx == self.play_screen.my_cards_selected_index:
                pygame.draw.rect(screen, COLOR_BLACK, rect, 5)

        txt_card_cnt = get_medium_font().render(str(len(self.card_rects)), True, COLOR_BLACK)
        screen.blit(txt_card_cnt, self.background_rect)



    # 나의 카드
    def draw_my_cards(self, screen: pygame.Surface, cards):

        # 카드 레이아웃 (충돌 감지 목적)
        self.cards = cards
        self.card_rects: list[pygame.Rect] = []
        temp_card_rects = []


        # 카드 시작 좌표
        start_x = get_extra_small_margin()
        self.next_card_start_y = screen.get_height() - self.card_height - get_extra_small_margin()

        temp_idx = 0
        self.cards_line_size = 0
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

    # 카드 선택 키 이벤트
    def run_my_cards_select_key_event(self, key):
        if key == pygame.K_LEFT:
            if not self.play_screen.deck_select_enabled:
                self.play_screen.my_cards_selected_index = (self.play_screen.my_cards_selected_index - 1) % len(self.game.get_board_player().hands)
        elif key == pygame.K_RIGHT:
            if not self.play_screen.deck_select_enabled:
                self.play_screen.my_cards_selected_index = (self.play_screen.my_cards_selected_index + 1) % len(self.game.get_board_player().hands)
        elif key == pygame.K_UP:
            if self.cards_line_size != 0 and self.play_screen.my_cards_selected_index + self.cards_line_size < len(self.game.get_board_player().hands):
                self.play_screen.my_cards_selected_index = self.play_screen.my_cards_selected_index + self.cards_line_size
            else: # 덱 선택
                self.play_screen.deck_select_enabled = True
        elif key == pygame.K_DOWN:
            # 다시 카드 선택으로 돌아옴
            if self.play_screen.deck_select_enabled:
                self.play_screen.deck_select_enabled = False
            
            elif self.cards_line_size != 0 and self.play_screen.my_cards_selected_index - self.cards_line_size >= 0:
                self.play_screen.my_cards_selected_index = self.play_screen.my_cards_selected_index - self.cards_line_size
        elif key == pygame.K_RETURN:
            if self.play_screen.deck_select_enabled:
                self.play_screen.on_deck_selected()
            else:
                self.play_screen.on_card_selected(self.play_screen.my_cards_selected_index)

    def run_board_cards_select_click_event(self, pos):
        for idx, rect in enumerate(self.card_rects):
            if rect.collidepoint(pos):
                self.play_screen.on_card_selected(idx)