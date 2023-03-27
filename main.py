from screen.ScreenController import ScreenController
from game.game import UnoGame

game = UnoGame()
screenController = ScreenController(game)

screenController.run()  