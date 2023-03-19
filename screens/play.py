from util.globals import *
from player import Player
class PlayScreen:

    def __init__(self, controller):
        self.ctr = controller

        self.init_my_cards_layout(self.ctr.screen)
        self.init_board_layout(self.ctr.screen)
        self.init_players_layout(self.ctr.screen)
        self.init_escape_dialog(self.ctr.screen)

    # 나의 카드 레이아웃 초기화
    def init_my_cards_layout(self, screen):
        self.my_cards_layout_height = screen.get_height() // 3

    # 보드 레이아웃 초기화
    def init_board_layout(self, screen):
        self.board_layout_height = screen.get_height() - self.my_cards_layout_height

    # 플레이어 레이아웃 초기화
    def init_players_layout(self, screen):

        self.players = [Player([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18]), Player([1, 2, 3]), Player([1, 2, 3, 2, 3, 2, 3]), Player([1]), Player([1, 2, 3, 2, 3, 2, 3])]
        self.my_player_index = 0 # TODO: 나의 플레이어 인덱스

        self.current_player_index = 0 # TODO: 게임에서 받아와야 함
        self.players_selected_index = 0
        self.players_select_enabled = True

        self.players_layout_width = 200
        self.player_layout_height = (screen.get_height() - get_small_margin() * 6) // 5

    # 일시정지 다이얼로그 초기화
    def init_escape_dialog(self, screen):
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

    # 초기화 함수 (게임 종료 후 다시 들어왔을 때 호출)
    def init(self):
        self.escape_dialog_enabled = False
        self.escape_menu_index = 0

    # 다이얼로그 표시 상태 변경
    def toggle_escape_dialog(self):
        self.escape_dialog_enabled = not self.escape_dialog_enabled

    # 플레이어 선택 상태 변경
    def toggle_players_select(self):
        self.players_select_enabled = not self.players_select_enabled

    # 모든 View
    def draw(self, screen):
        screen.fill(COLOR_WHITE)

        self.draw_board_layout(screen)
        self.draw_my_cards_layout(screen, self.players[self.my_player_index])

        self.draw_players_layout(screen, self.players)

        if self.escape_dialog_enabled:
            self.draw_escpe_dialog_layout(screen)

    # 일시정지 다이얼로그 레이아웃
    def draw_escpe_dialog_layout(self, screen):
        # background solid
        self.escape_box = pygame.draw.rect(screen, COLOR_WHITE, ((screen.get_width() - self.escape_dialog_width) // 2, (screen.get_height() - self.escape_dialog_height) // 2, self.escape_dialog_width, self.escape_dialog_height))
        # background outline
        pygame.draw.rect(screen, COLOR_BLACK, ((screen.get_width() - self.escape_dialog_width) // 2, (screen.get_height() - self.escape_dialog_height) // 2, self.escape_dialog_width, self.escape_dialog_height), 1)

        title = get_large_font().render("일시정지", True, COLOR_BLACK)
        title_rect = get_rect(title, screen.get_width() // 2, self.escape_box.y + get_medium_margin())
        screen.blit(title, title_rect)

        self.draw_esacpe_menu(screen)
    
    # 일시정지 메뉴
    def draw_esacpe_menu(self, screen):
        for index, menu in enumerate(self.esacpe_menus):
            text = get_medium_font().render(menu['text'], True, COLOR_GRAY if  index != self.escape_menu_index else COLOR_BLACK)
            rect = get_rect(text, screen.get_width() // 2, screen.get_height() // 2 + text.get_height() * index)
            menu.update({'view': text, 'rect': rect})
            screen.blit(text, rect)

    # 보드 레이아웃
    def draw_board_layout(self, screen):
        self.board_layout = pygame.draw.rect(screen, COLOR_BOARD, (0, 0, screen.get_width() - self.players_layout_width, self.board_layout_height))
        self.draw_current_color(screen)
        self.draw_deck(screen)
        self.draw_current_card(screen)
        self.draw_uno_btn(screen)

    # 현재 색상 표시
    def draw_current_color(self, screen):
        # TODO: 색상 동적으로 변경
        ratio = 4
        # rect = (self.board_layout.width // ratio, self.board_layout.height // ratio, self.board_layout.width - self.board_layout.width // ratio * 2, self.board_layout.height - self.board_layout.height // ratio * 2)
        pygame.draw.circle(screen, COLOR_RED, self.board_layout.center, self.board_layout.width // ratio, 20)

    # 덱 레이아웃
    def draw_deck(self, screen):
        deck_layout = pygame.image.load('./resource/card_back.png') # TODO: 카드 수정
        deck_layout = pygame.transform.scale(deck_layout, (get_card_width() * 2, get_card_height() * 2))
        deck_layout_rect = get_center_rect(deck_layout, self.board_layout, -deck_layout.get_width() // 2 - get_medium_margin())
        self.deck_layout = screen.blit(deck_layout, deck_layout_rect)

    # 현재 카드 레이아웃
    def draw_current_card(self, screen):
        current_card_layout = pygame.image.load('./resource/card_back.png')
        current_card_layout = pygame.transform.scale(current_card_layout, (get_card_width() * 2, get_card_height() * 2))
        current_card_layout_rect = get_center_rect(current_card_layout, self.board_layout, current_card_layout.get_width() // 2 + get_medium_margin())
        self.current_card_layout = screen.blit(current_card_layout, current_card_layout_rect)

    # 우노 버튼
    def draw_uno_btn(self, screen):
        uno_btn = pygame.image.load('./resource/uno_btn.png')
        uno_btn = pygame.transform.scale(uno_btn, (get_uno_width(), get_uno_height()))
        uno_btn_rect = get_center_rect(uno_btn, self.board_layout, y = self.board_layout.width // 4 - 10)
        self.uno_btn = screen.blit(uno_btn, uno_btn_rect)

    # 나의 카드 레이아웃
    def draw_my_cards_layout(self, screen, player):
        # 배경
        self.my_cards_layout = pygame.draw.rect(screen, COLOR_PLAYER, (0, self.board_layout.bottom, self.board_layout.right, self.my_cards_layout_height))

        # 나의 차례 스트로크
        if self.my_player_index == self.current_player_index:
            pygame.draw.rect(screen, COLOR_RED, (0, self.board_layout.bottom, self.board_layout.right, self.my_cards_layout_height), 2)

        # 나의 카드
        self.draw_my_cards(screen, player.cards)

    # 나의 카드
    def draw_my_cards(self, screen, cards):
        card_percent = 1.5

        # 카드 시작 좌표
        start_x, start_y = get_extra_small_margin(), screen.get_height() - get_card_height() * card_percent - get_extra_small_margin()
        temp_idx = 0

        for idx, card in enumerate(cards):
            card_layout = pygame.image.load('./resource/card_back.png')
            card_layout = pygame.transform.scale(card_layout, (get_card_width() * card_percent, get_card_height() * card_percent))

            # 카드가 보드 넘어가는 경우 위로 쌓음
            if start_x + (card_layout.get_width() // card_percent) * (idx - temp_idx) + card_layout.get_width() >= self.board_layout.width:
                start_y -= card_layout.get_height() + get_extra_small_margin()
                temp_idx = idx

            # 카드 시작 위치
            card_start = start_x + (card_layout.get_width() // card_percent) * (idx - temp_idx)

            card_rect = card_layout.get_rect().topleft = (card_start, start_y)
            temp = screen.blit(card_layout, card_rect)

        # 카드 개수 표시
        txt_card_cnt = get_medium_font().render(str(len(cards)), True, COLOR_BLACK)
        txt_card_cnt_rect = txt_card_cnt.get_rect().topleft = self.my_cards_layout.topleft
        screen.blit(txt_card_cnt, txt_card_cnt_rect)

    # 플레이어 목록 레이아웃
    def draw_players_layout(self, screen, players):
        self.players_layout = pygame.draw.rect(screen, COLOR_GRAY, (screen.get_width() - self.players_layout_width, 0, self.players_layout_width, screen.get_height()))
        self.draw_player(screen, players)

    # 플레이어
    def draw_player(self, screen, players):

        self.player_list = []
        temp_player_list = []

        for idx, player in enumerate(players):
            # 배경
            player_layout = pygame.draw.rect(screen, COLOR_PLAYER, (self.players_layout.left + get_small_margin(), get_small_margin() + (self.player_layout_height + get_small_margin()) * idx, self.players_layout.width - get_small_margin() * 2, self.player_layout_height))
            temp_player_list.append(player_layout)

            # 선택된 플레이어 스트로크
            if self.players_select_enabled and idx == self.players_selected_index:
                # 투명 색상 적용
                surface = pygame.Surface((self.players_layout.width - get_small_margin() * 2, self.player_layout_height), pygame.SRCALPHA)
                surface.fill(COLOR_TRANSPARENT_WHITE)
                screen.blit(surface, (self.players_layout.left + get_small_margin(), get_small_margin() + (self.player_layout_height + get_small_margin()) * idx))

            # 현재 플레이어 스트로크
            if idx == self.current_player_index:
                pygame.draw.rect(screen, COLOR_RED, (self.players_layout.left + get_small_margin(), get_small_margin() + (self.player_layout_height + get_small_margin()) * idx, self.players_layout.width - get_small_margin() * 2, self.player_layout_height), 2)

            # 카드
            self.draw_cards(screen, player_layout, player.cards)

        self.player_list = temp_player_list
            
    # 카드
    def draw_cards(self, screen, player_layout, cards):
        for idx, card in enumerate(cards):
            card_layout = pygame.image.load('./resource/card_back.png')
            card_layout = pygame.transform.scale(card_layout, (get_card_width(), get_card_height()))
            card_rect = card_layout.get_rect().topleft = (player_layout.left  + get_extra_small_margin() + (card_layout.get_width() // 2) * idx, player_layout.bottom - card_layout.get_height() - get_extra_small_margin())
            temp = screen.blit(card_layout, card_rect)

        # 카드 개수 표시 (45 변수로 설정해야 함)
        txt_card_cnt = get_small_font().render(str(len(cards)), True, COLOR_BLACK)
        txt_card_cnt_rect = txt_card_cnt.get_rect().topleft = (player_layout.left + get_extra_small_margin(), player_layout.bottom - get_card_height() - txt_card_cnt.get_height() - get_extra_small_margin())
        screen.blit(txt_card_cnt, txt_card_cnt_rect)

    # 이벤트 처리 함수
    def process_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.process_key_event(event.key)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.process_click_event(pygame.mouse.get_pos())

    # 키보드 입력 이벤트 처리
    def process_key_event(self, key):
        if key == pygame.K_ESCAPE:
            self.toggle_escape_dialog()

        if self.escape_dialog_enabled:
            self.run_esacpe_key_event(key)

        elif self.players_select_enabled:
            self.run_players_select_key_event(key)

    # 일시정지 메뉴 키 이벤트
    def run_esacpe_key_event(self, key):
        if key == pygame.K_UP:
            self.escape_menu_index = (self.escape_menu_index - 1) % len(self.esacpe_menus)
        elif key == pygame.K_DOWN:
            self.escape_menu_index = (self.escape_menu_index + 1) % len(self.esacpe_menus)
        elif key == pygame.K_RETURN:
            self.esacpe_menus[self.escape_menu_index]['action']()

    # 플레이어 선택 키 이벤트
    def run_players_select_key_event(self, key):
        if key == pygame.K_UP:
            self.players_selected_index = (self.players_selected_index - 1) % len(self.players)
        elif key == pygame.K_DOWN:
            self.players_selected_index = (self.players_selected_index + 1) % len(self.players)
        elif key == pygame.K_RETURN:
            self.on_player_selected(self.players_selected_index)

    # 클릭 이벤트
    def process_click_event(self, pos):
        if self.escape_dialog_enabled:
            self.run_esacpe_click_event(pos)
        
        elif self.players_select_enabled:
            self.run_players_select_click_evnet(pos)

    # 일시정지 메뉴 클릭 이벤트
    def run_esacpe_click_event(self, pos):
        for menu in self.esacpe_menus:
            if menu['rect'] and menu['rect'].collidepoint(pos):
                menu['action']()

    # 플레이어 선택 클릭 이벤트
    def run_players_select_click_evnet(self, pos):
        for idx, player in enumerate(self.player_list):
            if player.collidepoint(pos):
                self.on_player_selected(idx)

    # 플레이어 선택 종류 분기
    def on_player_selected(self, idx):
        print(f"{idx}번 플레이어 선택")