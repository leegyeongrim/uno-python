
from story_mode.regionA import regionA
from game.game import UnoGame

test=regionA()

for _ in range(1000):
    test.split_cards()
    test.computer_deal(1)
    #screenController = ScreenController()

    #screenController.run()
