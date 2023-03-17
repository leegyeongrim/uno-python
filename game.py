from player import Player
from deck import Deck

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
        pass

    # 플레이어에게 카드를 분배
    def dealCard(self):
        pass

    # 플레이어에게 패널티 카드 1장 부여
    def penalty(self):
        pass
    
    # 다음 플레이어로 이동
    def moveNextPlayer(self):
        pass

    # 현재 플레이어 스킵
    def skipCurrentPlayer(self):
        self.moveNextPlayer()

    # 타이머 시작
    def startTimer(self):
        pass

    # 특별 카드 실행
    def runCard(self, card):
        pass

    def clickUno(self, card):
        pass