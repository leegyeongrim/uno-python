from __future__ import annotations
from typing import TYPE_CHECKING

from util.globals import *
import time
import pygame

if TYPE_CHECKING:
    from game.game import UnoGame
    from screen.ScreenController import ScreenController

class Board:
    def __init__(self, play_screen):
        self.play_screen = play_screen

    def draw(self, screen: pygame.Surface, current_card: Card):

        self.background_rect = pygame.Rect((0, 0, screen.get_width() - self.play_screen.players_layout.width, screen.get_height() - screen.get_height() // 3))
        self.color_circle = (self.background_rect.center, self.background_rect.width // 4, 20)

        self.deck = get_card_back(2)
        self.deck_rect = get_center_rect(self.deck, self.background_rect, -self.deck.get_width() // 2 - get_medium_margin())
        self.deck_highlight = pygame.Surface((get_card_width(2), get_card_height(2)), pygame.SRCALPHA)
        self.deck_highlight.fill(COLOR_TRANSPARENT_WHITE)

        # TODO: 삭제
        self.current_card = get_card_back(2)
        self.current_card_rect = get_center_rect(self.current_card, self.background_rect, self.current_card.get_width() // 2 + get_medium_margin())

        self.uno = pygame.image.load('./resource/uno_btn.png')
        self.uno = pygame.transform.scale(self.uno, (get_uno_width(), get_uno_height()))
        self.uno_rect = get_center_rect(self.uno, self.background_rect, y = self.background_rect.width // 4 - 10)

        pygame.draw.rect(screen, COLOR_BOARD, self.background_rect)
        pygame.draw.circle(screen, CARD_COLOR_SET[current_card.color], *self.color_circle)
        screen.blit(self.deck, self.deck_rect)

        if self.play_screen.my_cards_select_enabled and self.play_screen.deck_select_enabled:
            screen.blit(self.deck_highlight, self.deck_rect)

        screen.blit(get_card(current_card, 2), self.current_card_rect)

        screen.blit(self.uno, self.uno_rect)

    def run_deck_click_event(self, pos):
        if self.deck_rect.collidepoint(pos):
            self.play_screen.on_deck_selected()