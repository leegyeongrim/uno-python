class Setting:
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 600
        self.blind_mode = False

    def getResoulition(self):
        return (self.screen_width, self.screen_height)
    
    def setResolution(self, width, height):
        self.screen_width, self.screen_height = width, height
    
    def toggleBlindMode(self):
        self.blind_mode = not self.blind_mode

    def isBlindModeEnabled(self):
        return self.blind_mode

    # 설정 저장
    def save(self):
        pass

    # 설정 불러오기
    def load(self):
        pass

    # 설정 초기화
    def clear(self):
        pass