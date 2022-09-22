from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

for x in range(0 , 800 + 1, 2):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    update_canvas()
    delay(0.01)
    get_events()  #중간에 윈도우가 다른 프로그램을 처리할 수 있도록 해줌

close_canvas()
