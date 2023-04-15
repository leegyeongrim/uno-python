from screen.ScreenController import ScreenController
from story_mode.regionD import regionD
from game.game import UnoGame

if __name__ == '__main__':
    test=regionD()

    for p in range(len(test.game.players)):
        test.game.deal(p)
    
    for _ in range(10):
        print(test.game.get_current_player().name)
        test.next_turn()

