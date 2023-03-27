from util.globals import *
import pygame

class SettingScreen:
    def __init__(self, controller):
        self.controller = controller # ScreenController 객체

    # 반복적으로 실행되며 화면 그려지는 함수
    def draw(self, screen):
        screen.fill(COLOR_WHITE)

    # 반복적으로 실행되며 이벤트 처리하는 함수
    def process_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN: # 키보드 입력 처리
                if event.key == pygame.K_UP: # 위 방향키
                    pass
                elif event.key == pygame.K_DOWN: # 아래 방향키
                    pass
                elif event.key == pygame.K_RETURN: # 엔터
                    pass
            elif event.type == pygame.MOUSEBUTTONUP: # 마우스 클릭 처리
                pos = pygame.mouse.get_pos() # 마우스 좌표