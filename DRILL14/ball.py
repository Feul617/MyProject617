import random
from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600), 70, 0

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.fall_speed

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        print('ball disappears')
        if group == 'boy:ball':
            game_world.remove_object(self)
        pass

class BigBall(Ball):
    MIN_FALL_SPEED = 1 # 50pps = 1.5 meter per sec
    MAX_FALL_SOEED = 3 # 200pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SOEED)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed

    def handle_collision(self, other, group):
        if group == 'grass:big_ball':
            for i in range(10):

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
