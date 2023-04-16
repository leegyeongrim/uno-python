import json
import os


class Setting:
    file_path = 'uno_setting.json'

    MODE_SCREEN = "mode_screen"
    MODE_BLIND = "mode_blind"
    MODE_MASTER_VOLUME = "mode_master_volume"
    MODE_BACKGROUND_VOLUME = "mode_background_volume"
    MODE_EFFECT_VOLUME = "mode_effect_volume"

    MAX_VOLUME = 10

    def __init__(self):

        self.data = None

        self.load()

        # 화면
        self.screen_resolution = [(600, 400), (720, 480), (960, 640)]

    def init(self):
        self.data = {
            Setting.MODE_SCREEN: 1,
            Setting.MODE_BLIND: False,
            Setting.MODE_MASTER_VOLUME: 5,
            Setting.MODE_BACKGROUND_VOLUME: 5,
            Setting.MODE_EFFECT_VOLUME: 5,
        }

    def clear(self):
        self.init()
        self.save()

    def get_resolution(self):
        return self.screen_resolution[self.get(Setting.MODE_SCREEN)]

    def get_background_volume(self):
        return self.get(Setting.MODE_BACKGROUND_VOLUME) * self.get(Setting.MODE_MASTER_VOLUME) / 100

    def get_effect_volume(self):
        return self.get(Setting.MODE_EFFECT_VOLUME) * self.get(Setting.MODE_MASTER_VOLUME) / 100

    # 파일 저장 관련 코드
    def get(self, key):
        self.load()
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def load(self):
        try:
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.clear()


if __name__ == '__main__':
    setting = Setting()
    print(setting.get_resolution())
    print(setting.get_effect_volume())
    print(setting.get(Setting.MODE_MASTER_VOLUME))
