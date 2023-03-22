import pygame
from util.globals import *

class Board:
    def __init__(self, parent):
        self.parent = parent

    def init(self, width, height):
        self.background_rect = pygame.Rect((0, 0, width, height))
        self.color_circle = (self.background_rect.center, self.background_rect.width // 4, 20)

        self.deck = get_card_back(2)
        self.deck_rect = get_center_rect(self.deck, self.background_rect, -self.deck.get_width() // 2 - get_medium_margin())
        self.deck_highlight = pygame.Surface((get_card_width(2), get_card_height(2)), pygame.SRCALPHA)
        self.deck_highlight.fill(COLOR_TRANSPARENT_WHITE)

        self.current_card = get_card_back(2)
        self.current_card_rect = get_center_rect(self.current_card, self.background_rect, self.current_card.get_width() // 2 + get_medium_margin())

        self.uno = pygame.image.load('./resource/uno_btn.png')
        self.uno = pygame.transform.scale(self.uno, (get_uno_width(), get_uno_height()))
        self.uno_rect = get_center_rect(self.uno, self.background_rect, y = self.background_rect.width // 4 - 10)

        return self

    def draw(self, screen, current_card = COLOR_RED):
        pygame.draw.rect(screen, COLOR_BOARD, self.background_rect)
        pygame.draw.circle(screen, current_card, *self.color_circle)
        screen.blit(self.deck, self.deck_rect)

        if self.parent.my_cards_select_enabled and self.parent.deck_select_enabled:
            screen.blit(self.deck_highlight, self.deck_rect)

        screen.blit(self.current_card, self.current_card_rect)

        screen.blit(self.uno, self.uno_rect)
