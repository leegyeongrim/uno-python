from __future__ import annotations
from typing import TYPE_CHECKING
from util.globals import *


if TYPE_CHECKING:
    from screen.game.GameController import GameController
    

class LobbyScreen:
    def __init__(self, screen_controller):
        self.init(screen_controller)

    # 초기화 함수
    def init(self, screen_controller):

        # 메뉴 초기화
        def init_menu():
            self.menu_index = 0
            self.menus = [
                {'text': '플레이', 'view': None, 'rect': None, 'action': lambda: (
                    self.screen_controller.set_screen_type(TYPE_PLAY)
                )},
                {'text': '스토리모드', 'view': None, 'rect': None, 'action': lambda: (
                    self.screen_controller.set_screen_type(TYPE_STORY)
                )},
                {'text': '돌아가기', 'view': None, 'rect': None, 'action': lambda: (
                    self.screen_controller.set_screen_type(TYPE_START)
                )},
            ]

        # 상위 의존성 초기화
        self.screen_controller = screen_controller
        self.game = screen_controller.game

        init_menu()

    # 화면 그리기    
    def draw(self, screen: pygame.Surface):

        # 선택 메뉴 그리기
        def draw_menu(screen: pygame.Surface):
            for idx, item in enumerate(self.menus):
                # 플레이 텍스트
                text_play = get_medium_font().render(item['text'], True, COLOR_GRAY if  idx != self.menu_index else COLOR_BLACK)
                text_play_rect = get_leftcenter_rect(text_play, screen.get_rect(), y = text_play.get_height() * idx, x = get_medium_margin())
                
                # 기존 객체에 추가
                self.menus[idx]['view'] = text_play
                self.menus[idx]['rect'] = text_play_rect

                screen.blit(text_play, text_play_rect)

        # 함수 호출
        screen.fill(COLOR_WHITE)
        draw_menu(screen)

    # 이벤트 처리
    def run_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.run_key_event(event.key)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.run_click_event(pygame.mouse.get_pos())

    # 키입력 이벤트 처리
    def run_key_event(self, key):

        # 메뉴 키입력 이벤트 처리
        def run_menu_key_event(key):
            if key == pygame.K_UP:
                self.menu_index = (self.menu_index - 1) % len(self.menus)
            elif key == pygame.K_DOWN:
                self.menu_index = (self.menu_index + 1) % len(self.menus)
            elif key == pygame.K_RETURN:
                self.menus[self.menu_index]['action']()
        
        # 함수 호출
        run_menu_key_event(key)

    # 클릭 이벤트 처리
    def run_click_event(self, pos):
        pass