from pico2d import *
import random

import game_framework
import game_world

#1 : 이벤트 정의
RD, LD, RU, LU, TIMER, SPACE = range(6)
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8

#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 1
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        self.x = clamp(0, self.x, 1600)
        if self.x == 1600 or self.x == 0:
            self.dir *= -1

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 180, 0, 180, 200, 0, ' ', self.x, self.y, 180, 200)
        else:
            self.image.clip_composite_draw(int(self.frame) * 180, 0, 180, 200, 0, ' ', self.x, self.y, 180, 200)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        # self.frame = (self.frame + 1) % 8
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        self.x = clamp(0, self.x, 1600)

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*100, 0, 100, 100, 0, ' ', self.x, self.y, 100, 100)
        elif self.dir == 1:
            self.image.clip_composite_draw(int(self.frame)*100, 0, 100, 100, 0, 'v', self.x, self.y, 100, 100)



class SLEEP:

    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 100, 200, 100, 100,
                                          -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100,
                                          3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)


#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN, TIMER: SLEEP, SPACE: IDLE},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SPACE: IDLE}
}

PIXEL_PER_METER = (18.0 / 5.0)
RUN_SPEED_KMPH = 80.0 # km/h 마라토너의 평속
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

class Bird:

    def __init__(self):
        self.x, self.y = random.randint(0, 1600), random.randint(50, 200)
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')
        self.frame_high = 0


        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        self.frame_high = (int(self.frame) / 5) + 1

        if self.x == 1599 or self.x == 1:
            self.dir *= -1
            self.face_dir *= -1

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f}', (255, 255, 0))

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass
