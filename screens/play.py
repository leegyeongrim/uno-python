from util.globals import *

class PlayScreen:
    def __init__(self, controller):
        self.controller = controller

    def draw(self, screen):
        screen.fill(COLOR_WHITE)

    def process_events(self, events):
        pass