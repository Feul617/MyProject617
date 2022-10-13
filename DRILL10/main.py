from pico2d import *
import play_state
import logo_state
state = logo_state # 모듈을 변수로 취급

open_canvas()
states = [logo_state, play_state]
for state in states:
    state.enter()
# game main loop code
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        delay(0.05)
    state.exit()
# finalization code
close_canvas()
