import json
file_path='/Users/leegyeongrim/setting_data.json'

class Setting:
    def __init__(self):
        self.screen_width=720
        self.screen_height=600
        self.screen_mode = 1
        self.blind_mode = False

    def get_resolution(self):
        return (self.screen_width, self.screen_height)
    
    def get_screen_mode(self):
        return self.screen_mode
    
    def isBlindModeEnabled(self):
        return self.blind_mode
    
    def setResolution(self):
        width = [360,720,1080]
        height = [300,600,900]
        if(self.screen_mode==0):
            self.screen_width, self.screen_height=width[0], height[0]
        elif(self.screen_mode==1):
            self.screen_width, self.screen_height=width[1], height[1]
        elif(self.screen_mode==2):
            self.screen_width, self.screen_height=width[2], height[2]
    
    def toggleBlindMode(self):
        self.blind_mode = not self.blind_mode
        

    # 설정 저장
    def save(self):
        with open(file_path,'w') as file:
            json.dump(self.setting_data(), file)
        pass

    # 설정 불러오기
    def load(self):
        with open(file_path,'r') as file:
            data=json.load(file)
        self.screen_mode=data['screen_mode']
        self.blind_mode=data['blind_mode']
        pass
    
    def load2(self):
        with open(file_path,'r') as file:
            data=json.load(file)
        print(data)

    # 설정 초기화
    def clear(self):
        self.screen_width=720
        self.screen_height=600
        self.screen_mode = 1
        self.blind_mode = False
        pass