import game_framework
import game_world
from pico2d import *
import server
import random

class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(150, 1700)
        self.y = random.randint(200, 900)
        self.timer = 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        pass

    def draw(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(self.sx, self.sy, 30, 30)
        #draw_rectangle(self.sx-10, self.sy-10, self.sx+10, self.sy+10)

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)
        pass
