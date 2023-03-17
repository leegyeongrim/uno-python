from player import Player
from deck import Deck
from card import Card
import time
import random

class UnoGame:
    def __init__(self, deck, players):
        self.timer = 5000
        self.isTurnEnd = False

        self.reverseDirection = False
        self.skipTurnCnt = 0

        self.players = players
        self.currentPlayer = players[0]

        self.deck = deck
        self.currentCard = None

    # 게임 시작
    def startGame(self):
        self.deck.shuffle()
        self.currentCard=self.deck.draw() #player들에게 나눠준 후 현재카드 deck에서 1장 놓기
        print("current card : ",end='')
        print(self.currentCard.color, self.currentCard.value)
        self.dealCard()
        #current palyer turn
        #self.startTimer()
        while True:
            print()
            for idx in range(len(self.currentPlayer.hands)):                        #current card가 색깔이 없을때     #player가 내는 카드가 색깔이 없을때
                if self.currentCard.color == self.currentPlayer.hands[idx].color or self.currentCard.color=="None" or self.currentPlayer.hands[idx].color=="None": #색깔 같은 카드 먼저 냄 (idx빠른거부터)
                    self.currentCard=self.currentPlayer.play(idx)
                    print("current card :",self.currentCard.color, self.currentCard.value, end=" ")
                    print()

                    print("player", self.players.index(self.currentPlayer), "hands :", end=" ")
                    for idx in range(len(self.currentPlayer.hands)):
                        print(self.currentPlayer.hands[idx].color, self.currentPlayer.hands[idx].value, end=' / ')
                    print()
                    if len(self.currentPlayer.hands)==0:
                        print("게임 종료!")
                        return 0
                    self.runCard(self.currentCard)
                    break
                elif self.currentCard.value == self.currentPlayer.hands[idx].value: #값 같은 카드 먼저 냄 (idx빠른거부터)
                    self.currentCard=self.currentPlayer.play(idx) #현재 플레이어가 카드를 냄
                    print("current card :",self.currentCard.color, self.currentCard.value, end=" ")
                    print()

                    print("player", self.players.index(self.currentPlayer), "hands :", end=" ")
                    for idx in range(len(self.currentPlayer.hands)):
                        print(self.currentPlayer.hands[idx].color, self.currentPlayer.hands[idx].value, end=' / ')
                    print()
                    if len(self.currentPlayer.hands)==0:
                        print("게임 종료!")
                        return 0
                    self.runCard(self.currentCard)
                    break
            else:                                          #낼 카드가 없을때
                if len(self.currentPlayer.hands)==0:
                    print("게임 종료!")
                    return 0
                self.penalty(1)
                print("current card와 일치하는 카드가 없으므로 1장 draw!!")
                print("player", self.players.index(self.currentPlayer), "hands :", end=" ")
                for idx in range(len(self.currentPlayer.hands)):
                    print(self.currentPlayer.hands[idx].color, self.currentPlayer.hands[idx].value, end=' / ')
                print()
                self.moveNextPlayer()
                
    # 플레이어에게 카드를 분배
    def dealCard(self):
            for p in self.players:
                print("player", self.players.index(p), "hands :", end=" ")
                hands=[]
                for _ in range(7):
                    hands.append(self.deck.cards.pop()) 
                p.init_hands(hands)
                for idx in range(len(self.currentPlayer.hands)):
                    print(p.hands[idx].color, p.hands[idx].value, end=' / ')
                print()

    # 플레이어에게 패널티 카드 n장 부여
    def penalty(self, n):
        for _ in range(n):
            self.currentPlayer.draw(self.deck.draw())
        #print(self.currentPlayer.hands)
    
    # 다음 플레이어로 이동
    def moveNextPlayer(self):
        player_idx=players.index(self.currentPlayer)
        if self.reverseDirection==False:
            if player_idx<len(self.players)-1:
                player_idx+=1
            else:                  #player 수 n명이라 가정하면, player_idx: n-1일때 다음 차례는 처음(player_idx=0)으로 돌아감
                player_idx=0
        else:
            if player_idx>0:
                player_idx-=1
            else:                  
                player_idx=len(self.players)-1
        self.currentPlayer=players[player_idx]
        #print(player_idx)
            
    # 현재 플레이어 스킵
    def skipCurrentPlayer(self):
        self.moveNextPlayer()

    # 타이머 시작 
    def startTimer(self):
        self.timer = 5000
        while (self.timer !=0):
            self.timer-=1
            time.sleep(1)
            print(self.timer)

    # 특별 카드 실행
    def runCard(self, card): #기능 확인은 못해봄
        if card.value=="jump":
            self.moveNextPlayer()
            self.skipCurrentPlayer() #다음차례 턴이 skip
        elif card.value=="back":
            if self.reverseDirection==False:
                self.reverseDirection=True
            else:
                self.reverseDirection=False
            self.moveNextPlayer()
        elif card.value=="+2":
            self.moveNextPlayer()
            self.penalty(2)
            self.skipCurrentPlayer()
        elif card.value=="-1": # hands 중 1장 무작위로 버림
            if len(self.currentPlayer.hands)==1: #마지막 남은 2장 중 -1 카드가 남았을때, 카드 버리는거 수행안하고 게임 종료시킴
                self.currentPlayer.hands.pop(card_idx)
                return
            card_idx=random.randint(0,len(self.currentPlayer.hands)-1)
            self.currentPlayer.hands.pop(card_idx)
            self.moveNextPlayer()
        elif card.value=="omt": # moveNextPlayer를 실행하지 않음
            pass
        elif card.value=="+4":
            self.moveNextPlayer()
            self.penalty(4)
            self.skipCurrentPlayer()
        else: #기술카드가 아닐때
            self.moveNextPlayer()

    def clickUno(self, idx): #idx는 우노버튼을 누른사람의 idx
        if self.currentPlayer==players[idx]:
            pass
        else:
            self.penalty(1)
        self.moveNextPlayer()

p1 = Player()
p2 = Player()
color = ["None",'red','yellow','green','blue']
value = [i for i in range(1,10)] + ["jump", "back", "+2", "-1", "omt", "+4"] #omt; 1번더
cards=[Card(color[0],value[-1])]
for c in color[1:]:
    for v in value[:14]:
        cards.append(Card(c,v))

deck=Deck(cards)
players=[p1,p2]
game=UnoGame(deck,players)

game.startGame()