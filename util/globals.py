import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_BLACK = (0, 0, 0)

TYPE_START = "start"
TYPE_SETTING = "setting"
TYPE_PLAY = "play"

DIMEN_LARGE = 50
DIMEN_MEDIUM = 30

def get_rect(view, x, y):
    return view.get_rect(center = (x, y))

def get_large_font(percent = 1):
    return pygame.font.SysFont('malgungothic', DIMEN_LARGE * percent)

def get_medium_font(percent = 1):
    return pygame.font.SysFont('malgungothic', DIMEN_MEDIUM * percent)