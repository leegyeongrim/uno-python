from settings import Setting
from util.globals import *
from screens.start import StartScreen
from screens.setting import SettingsScreen
from screens.play import PlayScreen
import pygame

class ScreenController:

    screens = {}

    def __init__(self):
        pygame.init()
        pygame.display.set_icon(pygame.image.load("./icon.png"))
        pygame.display.set_caption("Uno Game")

        self.screen_type = TYPE_START
        self.running = True

        # 설정 불러오기
        self.setting = Setting()
        self.loadSetting()

        self.init_instance()

    def init_instance(self):
        ScreenController.screens = {
            TYPE_START: StartScreen(self),
            TYPE_PLAY: PlayScreen(self),
            TYPE_SETTING: SettingsScreen(self),
        }


    # 설정 불러오기
    def loadSetting(self):
        self.screen = pygame.display.set_mode(self.setting.get_resolution())

    # 화면 시작
    def run(self):
        while self.running:
            self.display_screen()
            self.process_events()
            pygame.display.update()
        pygame.quit()

    # 화면 종료
    def stop(self):
        self.running = False

    # 현재 화면 불러옴
    def get_screen(self):

        return ScreenController.screens.get(self.screen_type)
    
    def set_screen(self, screen_type):
        self.screen_type = screen_type
    
    # 화면 선택
    def display_screen(self):
        self.get_screen().draw(self.screen)
    
    # 이벤트 선택
    def process_events(self):
        # 이벤트 목록 
        events = pygame.event.get()

        # 공통 이벤트 처리
        for event in events:
            if event.type == pygame.QUIT: # 종료 이벤트
                self.running = False

        self.get_screen().process_events(events)

# 테스트 코드
if __name__ == '__main__':
    ScreenController().run()