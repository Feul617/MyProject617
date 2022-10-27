from pico2d import *

#이벤트 정의
RD, LD, RU, LU = range(4) # 0, 1, 2, 3과 같은 효과

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter()

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event): # 소년이 스스로 이벤트를 처리할 수 있게
        # event는 키 이벤트 -> 이것을 내부 RD 등오로 변환이 필요
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event) # 변환된 내부 이벤트를 큐에 저장

        if self.q: # q에 무언가 들어있다면
            event = self.q.pop() # 이벤트를 가죠옴
            self.cur_state.exit() # 현재 상태를 나감
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 계산
            self.cur_state.enter()

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1
        pass

    def update(self):
        self.cur_state.do()

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw()

        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

# 클래스를 이용해서 상태를 만듦
class IDLE:
    @staticmethod # 객체 생성이 아니고 그룹핑임을 알려줌
    def enter():
        print("ENTER IDLE")
        pass

    @staticmethod
    def exit():
        print("EXIT IDLE")
        pass

    @staticmethod
    def do():
        print("DO IDLE")
        pass

    @staticmethod
    def draw():
        print("DRAW IDLE")
        pass

class RUN:
    def enter():
        print("ENTER RUN")
        pass

    def exit():
        print("EXIT RNU")
        pass

    def do():
        print("DO RUN")
        pass

    def draw():
        print("DRAW RUN")
        pass

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}