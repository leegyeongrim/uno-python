from __future__ import annotations

from util.globals import *
from typing import TYPE_CHECKING

import pygame
if TYPE_CHECKING:
    from screen.ScreenController import ScreenController


class SettingScreen:
    def __init__(self, controller: ScreenController):

        self.controller = controller
        self.setting = controller.setting

        self.title_rect = None

        self.is_setting_select_enabled = True
        self.selected_setting_idx = 0
        self.settings = [
            {'text': '해상도', 'rect': None, 'result': None, 'modes': [], 'max': 3},
            {'text': '색약모드', 'rect': None, 'result': None, 'modes': [], 'max': 2},
            {'text': '전체볼륨', 'rect': None, 'result': None, 'modes': [], 'max': 10},
            {'text': '배경볼륨', 'rect': None, 'result': None, 'modes': [], 'max': 10},
            {'text': '효과음볼륨', 'rect': None, 'result': None, 'modes': [], 'max': 10},
            {'text': '키 설정', 'rect': None, 'result': None, 'modes': [], 'max': 10},
            {'text': '돌아가기', 'rect': None, 'result': None, 'modes': [], 'max': 10},
        ]
        self.max_text_right = get_medium_font().render('효과음볼륨', True, COLOR_BLACK).get_rect().right + get_medium_margin()


    def draw(self, screen: pygame.Surface):
        screen.fill(COLOR_WHITE)
        self.draw_title(screen)
        self.draw_contents(screen)

    def draw_title(self, screen: pygame.Surface):
        title = get_large_font().render('설정', True, COLOR_BLACK)
        self.title_rect = get_rect(title, screen.get_width() // 2, get_medium_margin())
        screen.blit(title, self.title_rect)

    def draw_contents(self, screen: pygame.Surface):
        temp_right = 0
        for idx, setting in enumerate(self.settings):
            # 텍스트
            color = COLOR_BLACK if idx == self.selected_setting_idx else COLOR_GRAY
            text = get_medium_font().render(setting['text'], True, color)
            text_rect = get_rect(text, text.get_width() // 2 + get_small_margin(), screen.get_height() // 2 + text.get_height() * (idx - len(self.settings) // 2))
            setting['rect'] = text_rect
            screen.blit(text, text_rect)

            # 모드 박스
            for mode in range(setting['max']):
                box_size = 20
                pygame.draw.rect(screen, COLOR_GRAY, (self.max_text_right + box_size * mode * 1.1, text_rect.y + (text_rect.height - box_size) // 2, 20, 20))


    def run_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.run_key_events(event.key)
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

    def run_key_events(self, key):
        if self.is_setting_select_enabled:
            self.run_select_settings_event(key)

    def run_select_settings_event(self, key):
        if key == pygame.K_UP:
            self.updateSettingSelectIndex(-1)
        elif key == pygame.K_DOWN:
            self.updateSettingSelectIndex(1)
        elif key == pygame.K_RETURN:
            pass

    def updateSettingSelectIndex(self, direction):
        self.selected_setting_idx = (self.selected_setting_idx + direction) % len(self.settings)
