from setting.settings import Setting
from util.globals import *
from screen.home.HomeScreen import HomeScreen
from screen.setting.SettingScreen import SettingScreen

from screen.game.lobby.LobbyScreen import LobbyScreen
from screen.game.play.PlayScreen import PlayScreen
from screen.game.story.StoryScreen import StoryScreen


from game.game import UnoGame
import pygame

class ScreenController:

    screens = {}

    def __init__(self):
        self.init_pygame()

        self.game: UnoGame = UnoGame()

        self.clock = pygame.time.Clock()
        self.fps = 30

        self.screen_type = TYPE_START
        self.running = True

        # 설정 불러오기
        self.setting = Setting()
        self.loadSetting()

        self.init_instance()


    def init_pygame(self):
        pygame.init()
        # 아이콘
        pygame.display.set_icon(pygame.image.load("./resource/icon.png"))
        #제목
        pygame.display.set_caption("Uno Game")
        # 기본 마우스
        pygame.mouse.set_visible(False)

    def init_instance(self):
        ScreenController.screens = {
            TYPE_START: HomeScreen(self),
            TYPE_SETTING: SettingScreen(self),
            TYPE_PLAY: PlayScreen(self),
            TYPE_LOBBY: LobbyScreen(self),
            TYPE_STORY: StoryScreen(self),
        }

    # 화면 설정
    def set_screen_type(self, type):
        self.screen_type = type


    # 설정 불러오기
    def loadSetting(self):
        self.screen = pygame.display.set_mode(self.setting.get_resolution())

    # 화면 시작
    def run(self):
        while self.running:
            self.dt = self.clock.tick(self.fps)

            self.display_screen()
            self.run_events()
            pygame.display.update()
        pygame.quit()

    # 화면 종료
    def stop(self):
        self.running = False

    # 현재 화면 불러옴
    def get_screen(self):
        return ScreenController.screens.get(self.screen_type)
    
    # 현재 화면 설정
    def set_screen(self, screen_type):
        self.screen_type = screen_type
    
    # 화면 선택
    def display_screen(self):
        self.get_screen().draw(self.screen)
        self.draw_cursor()

    # 마우스 커서
    def draw_cursor(self):
        cursor = pygame.image.load('./resource/cursor.svg')
        # cursor = pygame.transform.scale(cursor, (35, 40))
        cursor_rect = cursor.get_rect().topleft = pygame.mouse.get_pos()
        self.screen.blit(cursor, cursor_rect)
    
    # 이벤트 선택
    def run_events(self):
        # 이벤트 목록 
        events = pygame.event.get()

        # 공통 이벤트 처리
        for event in events:
            if event.type == pygame.QUIT: # 종료 이벤트
                self.running = False

        # 화면에 이벤트 전달
        self.get_screen().run_events(events)