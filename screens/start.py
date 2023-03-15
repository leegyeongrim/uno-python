from util.globals import *
import pygame

class StartScreen:
    def __init__(self, controller):
        self.controller = controller

        # 초기 설정
        self.selected_menu_index = 0
        self.menu_dict = [
            {'text': '싱글플레이', 'action': lambda: controller.set_screen(TYPE_PLAY), 'view': None, 'rect': None }, 
            {'text': '설정', 'action': lambda: controller.set_screen(TYPE_SETTING), 'view': None, 'rect': None }, 
            {'text': '종료', 'action': lambda: controller.stop(), 'view': None, 'rect': None }, 
        ]

        self.draw_title(controller.screen)
        self.draw_menu(controller.screen, self.menu_dict)


    # 시작 화면
    def draw(self, screen):
        screen.fill(COLOR_WHITE)

        self.draw_title(screen)
        self.draw_menu(screen, self.menu_dict)
        

    # 시작 화면 이벤트 처리
    def process_events(self, events):
        for event in events:
            # 마우스 좌표 (x, y)
            pos = pygame.mouse.get_pos() 

            if event.type == pygame.KEYDOWN: # 키보드 입력 처리
                if event.key == pygame.K_UP:
                    self.selected_menu_index = (self.selected_menu_index - 1) % len(self.menu_dict)
                elif event.key == pygame.K_DOWN:
                    self.selected_menu_index = (self.selected_menu_index + 1) % len(self.menu_dict)
                elif event.key == pygame.K_RETURN:
                    self.menu_dict[self.selected_menu_index]['action']()

            elif event.type == pygame.MOUSEBUTTONUP: # 마우스 클릭 처리
                for menu in self.menu_dict:
                    if menu['rect']:
                        if menu['rect'].collidepoint(pos):
                            menu['action']()




            if self.title_rect.collidepoint(pos):
                print("충돌")

    def draw_title(self, screen):
        self.title = get_large_font().render("Uno Game", True, COLOR_BLACK)
        self.title_rect = get_rect(self.title, self.get_width() // 2, self.get_height() // 3)
        screen.blit(self.title, self.title_rect)

    def draw_menu(self, screen, menus):
        for index, menu in enumerate(menus):
            text = get_medium_font().render(menu['text'], True, COLOR_GRAY if  index != self.selected_menu_index else COLOR_BLACK)
            rect = get_rect(text, self.get_width() // 2, self.get_height() // 2 + text.get_height() * index)
            self.menu_dict[index].update({'view': text, 'rect': rect})
            screen.blit(text, rect)

    def get_width(self):
        return self.controller.screen.get_width()
    
    def get_height(self):
        return self.controller.screen.get_height()