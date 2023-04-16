class AnimateController:
    def __init__(self):
        self.enabled = False

        self.speed = 40

        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

    def init_pos(self, view, rect, start_x, start_y, end_x, end_y):
        self.enabled = True

        self.view = view
        self.rect = rect

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

        distance_x = self.end_x - start_x
        distance_y = self.end_y - start_y
        distance = ((distance_x ** 2) + (distance_y ** 2)) ** 0.5

        self.direction_x = distance_x / distance
        self.direction_y = distance_y / distance      

    def draw(self, screen):
        distance_remain_x = self.end_x - self.rect.x
        distance_remain_y = self.end_y - self.rect.y
        distance_remain = ((distance_remain_x ** 2) + (distance_remain_y ** 2)) ** 0.5

        # 종료 조건
        if distance_remain <= 2 * (self.speed ** 2) ** 0.5:
            self.rect.x = self.end_x
            self.rect.y = self.end_y
            
            self.enabled = False
        else:
            self.rect.x += self.speed * self.direction_x
            self.rect.y += self.speed * self.direction_y

        screen.blit(self.view, self.rect)