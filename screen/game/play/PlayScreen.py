from __future__ import annotations
from typing import TYPE_CHECKING

from game.model.player import Computer
from screen.game.play.section.escapeDialog import EscapeDialog
from screen.game.play.section.playersLayout import PlayersLayout
from util.globals import *
from screen.animate.animate import AnimateController
from screen.game.play.section.board import Board
from screen.game.play.section.cardboard import CardBoard
import time

if TYPE_CHECKING:
    from screen.ScreenController import ScreenController


class PlayScreen:

    def __init__(self, screen_controller: ScreenController):

        # 의존성 객체
        self.screen_controller = screen_controller
        self.animate_controller = AnimateController()
        self.game = screen_controller.game

        # 다이얼로그
        self.escape_dialog = EscapeDialog(self)

        # 플레이어 레이아웃
        self.players_layout = PlayersLayout(self)

        # 나의 카드 레이아웃
        self.my_cards_selected_index = 0
        self.cards_line_size = 0  # 한 줄 당 카드 개수

        self.my_cards_select_enabled = False  # 카드 선택 가능 상태

        # 게임 관련
        self.game_started = False

        self.stop_timer_enabled = False
        self.deck_select_enabled = False
        self.animate_deck_to_player_enabled = False
        self.animate_board_player_to_current_card_enabled = False
        self.animate_current_player_to_current_card_enabled = False

        # 보드 값
        self.board_width = self.screen_controller.screen.get_width() - self.players_layout.width
        self.board = Board(self)

        # 카드 레이아웃
        self.card_board = CardBoard(self)

    # 타이머 일시정지
    def pause_timer(self):
        self.stop_timer_enabled = True
        self.pause_temp_time = time.time()

    def continue_timer(self):
        self.stop_timer_enabled = False

    def start_game(self):
        self.game.is_started = True
        self.game.turn_start_time = time.time()

    # 초기화 함수
    def init(self):
        self.escape_dialog.enabled = False
        self.escape_dialog.menu_idx = 0

        if self.escape_dialog.enabled:
            self.pause_timer()
        else:
            self.continue_timer()

    # 다이얼로그 표시 상태 변경
    def toggle_escape_dialog(self):
        self.escape_dialog.enabled = not self.escape_dialog.enabled

        # 일시정지 시간 처리
        if self.escape_dialog.enabled:
            self.pause_timer()
        else:
            self.continue_timer()

    # 모든 View
    def draw(self, screen):
        screen.fill(COLOR_WHITE)
        self.my_cards_layout_height = screen.get_height() // 3

        if self.game.is_started:
            if self.game.is_game_over():
                pass
                # print("게임 종료") TODO 게임 종료
                # print(self.game.get_winner().name)

            self.resolve_error()

            self.board.draw(screen, self.game.current_card)

            self.card_board.draw(screen)

            self.players_layout.draw(screen)
            self.check_time()

        if self.animate_deck_to_player_enabled:
            if self.animate_controller.enabled:
                self.pause_timer()
                self.animate_controller.draw(screen)
            else:
                self.game.draw()  # 애니메이션 종료 후 한장 가져옴
                self.animate_deck_to_player_enabled = False

                # 일시정해 해제
                self.continue_timer()

                # 턴 전환
                self.game.next_turn()

        # 카드 제출 애니메이션
        elif self.animate_board_player_to_current_card_enabled:
            if self.animate_controller.enabled:
                self.pause_timer()
                self.animate_controller.draw(screen)

            # 애니메이션 종료 시 호출
            else:
                # 한 장 제출
                self.game.play(self.board_player_to_current_card_idx)
                self.animate_board_player_to_current_card_enabled = False
                self.continue_timer()

        elif self.animate_current_player_to_current_card_enabled:
            if self.animate_controller.enabled:
                self.pause_timer()
                self.animate_controller.draw(screen)

            # 애니메이션 종료 시 호출
            else:
                # 한 장 제출
                print('컴퓨터 제출')
                self.game.play(self.to_computer_play_idx)
                self.animate_current_player_to_current_card_enabled = False
                self.continue_timer()

        else:
            self.run_computer()

        if self.escape_dialog.enabled:
            self.escape_dialog.draw(screen)

    def check_time(self):
        if self.stop_timer_enabled:
            current_time = time.time()
            self.game.turn_start_time = self.game.turn_start_time + (current_time - self.pause_temp_time)
            self.pause_temp_time = current_time

        elif (time.time() - self.game.turn_start_time) > self.game.turn_time:
            # 시간 내 미선택 시 카드 드로우
            self.on_deck_selected()

        self.check_my_turn()

    def check_my_turn(self):
        self.my_cards_select_enabled = self.game.board_player_index == self.game.current_player_index

    # 이벤트 처리 함수
    def run_events(self, events):
        if self.game.is_started:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    self.process_key_event(event.key)

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.process_click_event(pygame.mouse.get_pos())



    # 키보드 입력 이벤트 처리
    def process_key_event(self, key):
        if self.game.is_started:
            if key == pygame.K_ESCAPE:
                self.toggle_escape_dialog()

            # 일시정지
            if self.escape_dialog.enabled:
                self.escape_dialog.run_key_event(key)

            # 카드 선택
            elif self.my_cards_select_enabled:
                self.card_board.run_my_cards_select_key_event(key)

            # 플레이어 선택
            elif self.players_layout.select_enabled:
                self.players_layout.run_select_key_event(key)

    # 클릭 이벤트
    def process_click_event(self, pos):

        if self.escape_dialog.enabled:
            self.escape_dialog.run_click_event(pos)

        elif self.my_cards_select_enabled:
            self.board.run_deck_click_event(pos)
            self.card_board.run_board_cards_select_click_event(pos)

        elif self.players_layout.select_enabled:
            self.players_layout.run_select_click_event(pos)

    # 카드 선택 분기
    def on_card_selected(self, idx):

        hands = self.game.get_board_player().hands
        card = hands[idx]
        # 유효성 확인
        if self.game.verify_new_card(card):
            self.screen_controller.play_effect()
            self.animate_board_player_to_current_card_enabled = True

            # 제출할 카드 저장
            self.board_player_to_current_card_idx = idx

            # 이동 애니메이션
            start_x, start_y = self.card_board.card_rects[idx].topleft
            end_x, end_y = self.board.current_card_rect.topleft

            surface = get_card(card, 2)
            rect = surface.get_rect()
            rect.topleft = start_x, start_y

            self.animate_controller.init_pos(surface, rect, start_x, start_y, end_x, end_y)

    # 에러 방지를 위한 함수
    def resolve_error(self):
        # 보드 카드 이전 인덱스 초과 시 처리

        if self.my_cards_selected_index >= len(self.game.get_board_player().hands):
            self.my_cards_selected_index -= 1

    # 덱 선택
    def on_deck_selected(self):
        self.screen_controller.play_effect()

        self.animate_deck_to_player_enabled = True

        self.animate_view = pygame.image.load('./resource/card_back.png')  # TODO: 카드 수정
        self.animate_view = pygame.transform.scale(self.animate_view, (
            get_card_width() * MY_BOARD_CARD_PERCENT, get_card_height() * MY_BOARD_CARD_PERCENT))

        self.animate_view_rect = get_center_rect(self.animate_view, self.board.background_rect,
                                                 -self.animate_view.get_width() // MY_BOARD_CARD_PERCENT - get_medium_margin())
        start_x, start_y = self.animate_view_rect.topleft

        # 애니메이션 목적지
        if self.game.current_player_index == self.game.board_player_index:
            self.animate_destination_x, self.animate_destination_y = self.card_board.next_card_start_x, self.card_board.next_card_start_y
            if self.card_board.next_card_start_x + (
                    get_card_width(MY_BOARD_CARD_PERCENT) // 1 + get_extra_small_margin()) + get_card_width(
                MY_BOARD_CARD_PERCENT) >= self.board.background_rect.width:
                self.animate_destination_y -= get_card_height(MY_BOARD_CARD_PERCENT) + get_extra_small_margin()
                self.animate_destination_x = get_small_margin()
            else:
                self.animate_destination_x = self.card_board.next_card_start_x + (
                        get_card_width(MY_BOARD_CARD_PERCENT) // 1 + get_extra_small_margin())

        # 내가 아닌 플레이어
        else:
            player_rect = self.players_layout.players[self.game.current_player_index - 1]
            self.animate_destination_x, self.animate_destination_y = player_rect.topleft

        # 애니메이션 정보 초기화
        self.animate_controller.init_pos(self.animate_view, self.animate_view_rect, start_x, start_y,
                                         self.animate_destination_x, self.animate_destination_y)

    def run_computer(self):
        if type(self.game.get_current_player()) is Computer:
            computer = self.game.get_current_player()

            self.to_computer_play_idx = computer.to_play(self.game)

            if self.to_computer_play_idx:
                self.screen_controller.play_effect()
                self.animate_current_player_to_current_card_enabled = True

                # 이동 애니메이션

                player_rect = self.players_layout.players[self.game.current_player_index - 1]

                start_x, start_y = player_rect.topleft
                end_x, end_y = self.board.current_card_rect.topleft

                surface = get_card_back(2)
                rect = surface.get_rect()
                rect.topleft = start_x, start_y

                self.animate_controller.init_pos(surface, rect, start_x, start_y, end_x, end_y)
            else:
                print('컴퓨터 낼 카드 없음')
                self.on_deck_selected()
