from screen.ScreenController import ScreenController
from story_mode.regionA import regionA
from game.game import UnoGame

#TODO main에서는 돌아가는데 testcode.py에서는 안돌아감

test=regionA()
func_li=[]
num_li=[]
        
for i in range(1000):
    test.split_cards()
    test.computer_deal(1)
    if type(test.example[i].value)==int:
        num_li.append(test.example)
    else:
        func_li.append(test.example)
    
print("기술카드:"+str(len(func_li))+", 숫자카드:"+str(len(num_li)))