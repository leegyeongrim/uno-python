import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)

TYPE_START = "start"
TYPE_SETTING = "setting"
TYPE_PLAY = "play"

DIMEN_EXTRA_LARGE = 50
DIMEN_LARGE = 40
DIMEN_MEDIUM = 30
DIMEN_SMALL = 20

DIMEN_MARGIN = 20

def get_rect(view, x, y):
    return view.get_rect(center = (x, y + view.get_height() // 2))

def get_large_font(percent = 1):
    return pygame.font.Font('./font/pretendard_regular.otf', DIMEN_LARGE * percent)

def get_medium_font(percent = 1):
    return pygame.font.Font('./font/pretendard_regular.otf', DIMEN_MEDIUM * percent)

def get_small_font(percent = 1):
    return pygame.font.Font('./font/pretendard_regular.otf', DIMEN_SMALL * percent)

def get_margin(percent = 1):
    return DIMEN_MARGIN * 1