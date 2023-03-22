import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)

COLOR_TRANSPARENT_WHITE = (255, 255, 255, 128)

COLOR_BOARD = (8, 64, 21)
COLOR_PLAYER = (40, 120, 58)

TYPE_START = "start"
TYPE_SETTING = "setting"
TYPE_PLAY = "play"

DIMEN_EXTRA_LARGE = 50
DIMEN_LARGE = 40
DIMEN_MEDIUM = 30
DIMEN_SMALL = 20
DIMEN_EXTRA_SMALL = 10

DIMEN_MARGIN_MEDIUM = 20
DIMEN_MARGIN_SMALL = 10
DIMEN_MARGIN_EXTRA_SMALL = 5

CARD_WIDTH = 30
CARD_HEIGHT = 45

DECK_PERCENT = 2
MY_BOARD_CARD_PERCENT = 1.5

UNO_WIDTH = 50
UNO_HEIGHT = 50

def get_rect(view, x, y):
    return view.get_rect(center = (x, y + view.get_height() // 2))

def get_center_rect(view, parent, x = 0, y = 0):
    if type(parent) is pygame.Rect:
        return view.get_rect(center = (parent.left + parent.width // 2 + x, parent.top + parent.height // 2 + y))
    else:
        return None

def get_large_font(percent = 1):
    return pygame.font.Font('./font/pretendard_regular.otf', DIMEN_LARGE * percent)

def get_medium_font(percent = 1):
    return pygame.font.Font('./font/pretendard_regular.otf', DIMEN_MEDIUM * percent)

def get_small_font(percent = 1):
    return pygame.font.Font('./font/pretendard_regular.otf', DIMEN_SMALL * percent)

def get_extra_small_font(percent = 1):
    return pygame.font.Font('./font/pretendard_regular.otf', DIMEN_EXTRA_SMALL * percent)


def get_medium_margin(percent = 1):
    return DIMEN_MARGIN_MEDIUM * percent

def get_small_margin(percent = 1):
    return DIMEN_MARGIN_SMALL * percent

def get_extra_small_margin(percent = 1):
    return DIMEN_MARGIN_EXTRA_SMALL * percent


def get_card_width(percent = 1):
    return CARD_WIDTH * percent

def get_card_height(percent = 1):
    return CARD_HEIGHT * percent

def get_uno_width(percent = 1):
    return UNO_WIDTH * percent

def get_uno_height(percent = 1):
    return UNO_HEIGHT * percent

def get_card_back(scale = 1):
    card_back = pygame.image.load('./resource/card_back.png') # TODO: 카드 수정
    card_back = pygame.transform.scale(card_back, (get_card_width(scale), get_card_height(scale)))
    return card_back
