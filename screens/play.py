from util.globals import *

class PlayScreen:

    def __init__(self, controller):
        self.ctr = controller

        self.player_width = 200

        self.init_escape_dialog()


    def init_escape_dialog(self):
        self.escape_dialog_enabled = False

        self.escape_dialog_width = 500
        self.escape_dialog_height = 300

        self.escape_menu_index = 0 
        self.esacpe_menus = [
            {'text': '설정', 'view': None, 'rect': None, 'action': lambda: self.ctr.set_screen(TYPE_SETTING) }, 
            {'text': '종료', 'view': None, 'rect': None, 'action': lambda: (
                    self.init(),
                    self.ctr.set_screen(TYPE_START) 
                )
            }
        ]

    # 초기화 함수
    def init(self):
        self.escape_dialog_enabled = False
        self.escape_menu_index = 0

    def draw(self, screen):
        screen.fill(COLOR_WHITE)

        self.draw_players(screen)

        if self.escape_dialog_enabled:
            self.draw_escpe_dialog(screen)

    def process_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.process_key_event(event.key)

    # 키보드 입력 이벤트 처리
    def process_key_event(self, key):
        if key == pygame.K_ESCAPE:
            self.toggle_escape_dialog()

        if self.escape_dialog_enabled:
            self.run_esacpe_key_event(key)

    # ESC 키보드 입력 이벤트 처리
    def run_esacpe_key_event(self, key):
        if key == pygame.K_UP:
            self.escape_menu_index = (self.escape_menu_index - 1) % len(self.esacpe_menus)
        elif key == pygame.K_DOWN:
            self.escape_menu_index = (self.escape_menu_index + 1) % len(self.esacpe_menus)
        elif key == pygame.K_RETURN:
            self.esacpe_menus[self.escape_menu_index]['action']()

    def toggle_escape_dialog(self):
        self.escape_dialog_enabled = not self.escape_dialog_enabled

    def draw_escpe_dialog(self, screen):
        # background solid
        self.escape_box = pygame.draw.rect(screen, COLOR_WHITE, ((screen.get_width() - self.escape_dialog_width) // 2, (screen.get_height() - self.escape_dialog_height) // 2, self.escape_dialog_width, self.escape_dialog_height))
        # background outline
        pygame.draw.rect(screen, COLOR_BLACK, ((screen.get_width() - self.escape_dialog_width) // 2, (screen.get_height() - self.escape_dialog_height) // 2, self.escape_dialog_width, self.escape_dialog_height), 1)

        title = get_large_font().render("일시정지", True, COLOR_BLACK)
        title_rect = get_rect(title, screen.get_width() // 2, self.escape_box.y + get_margin())
        screen.blit(title, title_rect)

        self.draw_esacpe_menu(screen)
        

    def draw_esacpe_menu(self, screen):
        for index, menu in enumerate(self.esacpe_menus):
            text = get_medium_font().render(menu['text'], True, COLOR_GRAY if  index != self.escape_menu_index else COLOR_BLACK)
            rect = get_rect(text, screen.get_width() // 2, screen.get_height() // 2 + text.get_height() * index)
            menu.update({'view': text, 'rect': rect})
            screen.blit(text, rect)

    def draw_players(self, screen):
        pygame.draw.rect(screen, COLOR_GRAY, (screen.get_width() - self.player_width, 0, self.player_width, screen.get_height()))