from pico2d import *

#이벤트 정의
RD, LD, RU, LU, TIMER = range(5) # 0, 1, 2, 3, 4와 같은 효과

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
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event): # 소년이 스스로 이벤트를 처리할 수 있게
        # event는 키 이벤트 -> 이것을 내부 RD 등오로 변환이 필요
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event) # 변환된 내부 이벤트를 큐에 저장

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
        self.cur_state.do(self)

        if self.q: # q에 무언가 들어있다면
            event = self.q.pop() # 이벤트를 가죠옴
            self.cur_state.exit(self) # 현재 상태를 나감
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 계산
            self.cur_state.enter(self, event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)

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
    def enter(self, event):
        print("ENTER IDLE")
        self.dir = 0
        #타이머 설정
        self.timer = 1000
        pass

    @staticmethod
    def exit(self):
        print("EXIT IDLE")
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0: #시간이 경과하면
            #이벤트를 발생
            #self.q.insert(0, TIMER) # 객체지향 프로그래밍에 위배 -> q를 직접 엑세스하고 있어서
            self.add_event(TIMER) #객체지향적인 방법
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

class RUN:
    def enter(self, event):
        print("ENTER RUN")
        # self.dir을 결정해야 함
        if event == RD: self.dir += 1
        elif event == LD: self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LU: self.dir += 1
        pass

    def exit(self):
        print("EXIT RUN")
        # run을 나가서 IDLE로 갈때, run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800) #clamp = a ~ b 까지를 범위로 잡겠다
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class SLEEP:
    @staticmethod # 객체 생성이 아니고 그룹핑임을 알려줌
    def enter(self, event):
        print("ENTER SLEEP")
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print("EXIT SLEEP")
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592 / 2, ' ', self.x - 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, ' ', self.x + 25, self.y - 25, 100, 100)
        pass

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP},
}