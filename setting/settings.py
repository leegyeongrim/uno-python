import json
import os

#os.mkdir("/Users/leegyeongrim/uno-python2")
file_path='/Users/leegyeongrim/uno-python2/setting_data.json'

class Setting:
    def __init__(self):
        # 화면
        self.screen_resolution=[(360,300),(720,600),(1080,900)]
        
        self.screen_mode = 1 # index 0,1,2
        
        self.screen_width = 720
        self.screen_height = 600
        
        self.blind_mode = False
        
        # 음향
        self.volumes=[0,1,2,3,4,5,6,7,8,9]
        
        self.sounds_mode=5 # index 0~9
        self.bgm_mode=5 # index 0~9
        self.sound_effect_mode=5 # index 0~9
        
        self.sounds_volume=self.volumes[self.sounds_mode]
        self.bgm_volume=self.volumes[self.bgm_mode]
        self.sound_effect_volume=self.volumes[self.sound_effect_mode]

    def get_resolution(self):
        return self.screen_resolution[self.screen_mode]
    
    def get_screen_mode(self):
        return self.screen_mode
    
    # 화면 모드 set
    def set_screen_mode(self, screen_mode):
        self.screen_mode=screen_mode
    
    # 화면 해상도 set (화면 모드 설정 후)
    def set_resolution(self):   
        (self.screen_width, self.screen_height)=self.screen_resolution[self.screen_mode]
            
    def isBlindModeEnabled(self):
        return self.blind_mode
    
    def toggleBlindMode(self):
        self.blind_mode = not self.blind_mode
    
    # 음향 모드 get
    def get_sounds_mode(self):
        return self.sounds_mode
    
    def get_bgm_mode(self):
        return self.bgm_mode
        
    def get_sound_effect_mode(self):
        return self.sound_effect_mode
    
    # 음향 볼륨 get
    def get_sounds_volume(self):
        return self.sounds_volume

    def get_bgm_volume(self):
        return self.bgm_volume
    
    def get_sound_effect_volume(self):
        return self.sound_effect_volume
    
    # 음향 모드 set
    def set_sounds_mode(self, sounds_mode):
        self.sounds_mode=sounds_mode
        
    def set_bgm_mode(self, bgm_mode):
        self.bgm_mode=bgm_mode
        
    def set_sound_effect_mode(self, sound_effect_mode):
        self.sound_effect_mode=sound_effect_mode
        
    # 음향 볼륨 set (모드 setting 후!)
    def set_sounds_volume(self):
        self.sounds_volume=self.volumes[self.sounds_mode]
        
    def set_bgm_volume(self):
        self.bgm_volume=self.volumes[self.bgm_mode]
        
    def set_sound_effect_volume(self):
        self.sound_effect_volume=self.volumes[self.sound_effect_mode]
        
    # 설정 파일 내용   
    def setting_data(self):
        setting_data={
        'screen_mode':self.screen_mode,
        'blind_mode':self.blind_mode,
        'sounds_mode':self.sounds_mode,
        'bgm_mode':self.bgm_mode,
        'sound_effect_mode':self.sound_effect_mode
        }
        return setting_data
    
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