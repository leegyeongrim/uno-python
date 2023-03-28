from screen.ScreenController import ScreenController
from game.game import UnoGame

if __name__ == '__main__':
    game = UnoGame()
    screenController = ScreenController(game)

    screenController.run()