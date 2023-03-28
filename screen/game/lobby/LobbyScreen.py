from __future__ import annotations
from typing import TYPE_CHECKING

import pygame.draw

from util.globals import *

if TYPE_CHECKING:
    from screen.game.GameController import GameController


class LobbyScreen:
    def __init__(self, screen_controller):
        # 메뉴 초기화
        self.menu_index = 0
        self.menus = [
            {'text': '플레이', 'view': None, 'rect': None, 'action': self.toggle_input_name_dialog },
            {'text': '돌아가기', 'view': None, 'rect': None, 'action': lambda: (
                self.screen_controller.set_screen_type(TYPE_START)
            )},
        ]

        self.input_name_dialog_enabled = False

        self.input_name_enabled = False
        self.input_name_text = ''

        # 상위 의존성 초기화
        self.screen_controller = screen_controller
        self.game = screen_controller.game

    def toggle_input_name_dialog(self):
        self.input_name_dialog_enabled = not self.input_name_dialog_enabled
    # 화면 그리기
    def draw(self, screen: pygame.Surface):

        # 선택 메뉴 그리기
        def draw_menu():
            for idx, item in enumerate(self.menus):
                # 플레이 텍스트
                text_play = get_medium_font().render(item['text'], True,
                                                     COLOR_BLACK if idx == self.menu_index else COLOR_GRAY)
                text_play_rect = get_left_center_rect(text_play, screen.get_rect(), y=text_play.get_height() * idx,
                                                      x=get_medium_margin())

                # 기존 객체에 추가
                self.menus[idx]['view'] = text_play
                self.menus[idx]['rect'] = text_play_rect

                screen.blit(text_play, text_play_rect)

        # 본인 이름 입력
        def draw_input_name():
            text_name = get_small_font().render('이름', True, COLOR_BLACK)
            text_name_rect = get_center_rect(text_name, screen.get_rect())

            self.input_name = get_small_font().render(self.input_name_text, True, COLOR_BLACK)
            input_name_rect = pygame.Rect(text_name_rect.bottomleft, self.input_name.get_size())

            # 제목
            screen.blit(text_name, text_name_rect)

            # 배경
            pygame.draw.rect(screen, COLOR_LIGHT_GRAY, input_name_rect)

            # 글자
            screen.blit(self.input_name, input_name_rect)

            if self.input_name_enabled:
                pygame.draw.rect(screen, COLOR_BLACK, input_name_rect, 2)

        # 함수 호출
        screen.fill(COLOR_WHITE)
        draw_menu()

        if self.input_name_dialog_enabled:
            self.draw_input_name_dialog(screen)

    def draw_input_name_dialog(self, screen: pygame.Surface):
        width, height = 500, 300
        
        # 배경    
        background = pygame.Surface(size=(width, height))
        background.fill(COLOR_WHITE)
        background_rect = get_center_rect(background, screen.get_rect())
        
        # 제목
        title = get_medium_font().render("이름 입력", True, COLOR_BLACK)

        # 확인
        submit = get_medium_font().render("확인", True, COLOR_BLACK)
        self.submit_rect = get_bottom_center_rect(submit, background_rect, -submit.get_width() // 2, -(submit.get_height() + get_small_margin()))

        # 입력 박스
        input_name = get_small_font().render('이름', True, COLOR_BLACK)
        input_background = pygame.Surface(size = (background_rect.width - 4 * get_medium_margin(), input_name.get_height() + get_small_margin()))
        input_background.fill(COLOR_LIGHT_GRAY)

        screen.blit(background, background_rect)
        pygame.draw.rect(screen, COLOR_BLACK, background_rect, 2)

        screen.blit(title, get_top_center_rect(title, background_rect, x = -title.get_width() // 2, y = get_medium_margin()))
        screen.blit(submit, self.submit_rect)
        screen.blit(input_background, get_center_rect(input_background, background_rect))

    # 이벤트 처리
    def run_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.run_key_event(event, event.key)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.run_click_event(event, pygame.mouse.get_pos())

    # 키입력 이벤트 처리
    def run_key_event(self, event, key):

        # 메뉴 키입력 이벤트 처리
        def run_menu_key_event(key):
            if key == pygame.K_UP:
                self.menu_index = (self.menu_index - 1) % len(self.menus)
            elif key == pygame.K_DOWN:
                self.menu_index = (self.menu_index + 1) % len(self.menus)
            elif key == pygame.K_RETURN:
                self.menus[self.menu_index]['action']()

            elif key == pygame.K_RIGHT:
                self.menu_enabled = False
                self.input_name_enabled = True

        if self.input_name_dialog_enabled:
            return self.run_input_name_dialog_key_event(key)

        # 함수 호출
        run_menu_key_event(key)

    def run_input_name_dialog_key_event(self, key):
        if key == pygame.K_ESCAPE:
            return self.toggle_input_name_dialog()

        if key == pygame.K_RETURN:
            # 이름 설정

            # 플레이어 설정 적용

            # 화면 이동
            self.screen_controller.set_screen_type(TYPE_PLAY)


    # 클릭 이벤트 처리
    def run_click_event(self, event, pos):
        pass
