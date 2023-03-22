from util.globals import *
import time
import pygame


class CardBoard:
    def __init__(self, parent):
        self.ctr = parent

        self.game = parent.game
        self.board = parent.board


    def init(self, width, height):
        self.background_rect = pygame.Rect(0, self.board.background_rect.bottom, self.board.background_rect.right, height)
        # 나의 카드
        #self.draw_my_cards(screen, player.hands)

        self.timer = get_medium_font().render(str(int(self.ctr.turn_time + 1 - (time.time() - self.ctr.turn_start_time))), True, COLOR_RED)
        self.timer_rect = self.timer.get_rect().topleft = (self.background_rect.right - self.timer.get_width() - get_small_margin(), self.background_rect.top)


        return self
    
    def draw(self, screen):
        pygame.draw.rect(screen, COLOR_PLAYER, self.background_rect)
        
        if self.game.board_player_index == self.game.current_player_index:
            self.timer = get_medium_font().render(str(int(self.ctr.turn_time + 1 - (time.time() - self.ctr.turn_start_time))), True, COLOR_RED)
            screen.blit(self.timer, self.timer_rect)
            pygame.draw.rect(screen, COLOR_RED, self.background_rect, 2)


    # 나의 카드
    def draw_my_cards(self, screen, cards):

        # 카드 레이아웃 (충돌 감지 목적)
        self.card_list = []
        temp_card_list = []

        # 카드 시작 좌표
        start_x = get_extra_small_margin()
        self.next_card_start_y = screen.get_height() - get_card_height(1.5) - get_extra_small_margin()

        temp_idx = 0

        for idx, card in enumerate(cards):
            card_back = get_card_back(1.5)

            # 카드가 보드 넘어가는 경우 위로 쌓음
            if start_x + (card_back.get_width() + get_extra_small_margin()) * (idx - temp_idx) + card_back.get_width() >= self.board.background_rect.width:
                self.next_card_start_y -= card_back.get_height() + get_extra_small_margin()

                if temp_idx == 0:
                    self.cards_line_size = idx
                
                temp_idx = idx
        

            # 카드 시작 위치
            self.next_card_start_x = start_x + (card_back.get_width() + get_extra_small_margin()) * (idx - temp_idx)

            card_rect = card_back.get_rect().topleft = (self.next_card_start_x, self.next_card_start_y)
            card_layout = screen.blit(card_back, card_rect)
            temp_card_list.append(card_layout)

            # 선택된 카드 하이라이트
            if self.my_cards_select_enabled and not self.deck_select_enabled and idx == self.my_cards_selected_index:
                # 투명 색상 적용
                surface = pygame.Surface((card_layout.width, card_layout.height), pygame.SRCALPHA)
                surface.fill(COLOR_TRANSPARENT_WHITE)
                screen.blit(surface, (card_layout.left, card_layout.top))

        self.card_list = temp_card_list


        # 카드 개수 표시
        txt_card_cnt = get_medium_font().render(str(len(cards)), True, COLOR_BLACK)
        txt_card_cnt_rect = txt_card_cnt.get_rect().topleft = self.my_cards_layout.topleft
        screen.blit(txt_card_cnt, txt_card_cnt_rect)