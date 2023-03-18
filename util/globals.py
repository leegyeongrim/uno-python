import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)

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

def get_rect(view, x, y):
    return view.get_rect(center = (x, y + view.get_height() // 2))

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