from __future__ import annotations
from typing import TYPE_CHECKING
from util.globals import *


if TYPE_CHECKING:
    from screen.game.GameController import GameController
    

class StoryScreen:
    def __init__(self, screen_controller):
        self.init(screen_controller)

    # 초기화 함수
    def init(self, screen_controller):

        # 상위 의존성 초기화
        self.screen_controller = screen_controller
        self.game = screen_controller.game


        # 스토리모드 활성화 변수
        self.enabled = True

    def disable_screen(self):
        self.enabled = False
    
    def enable_screen(self):
        self.enabled = True

    def draw(self, screen: pygame.Surface):
        screen.fill(COLOR_WHITE)

    def run_events(self, events):
        pass
