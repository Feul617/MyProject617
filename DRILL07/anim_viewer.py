from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('hollownight.png')

cannes = 7
d_time = 0.1

def move(depth):
    x = 0
    frame = 0
    while x < 800:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 80, 1024 - (80 * depth), 85, 85, x, 90)
        update_canvas()
        frame = (frame + 1) % cannes
        x += 5
        delay(d_time)
        get_events()

def jumpmove(depth, fast):
    j_count = 7
    y = 90
    x = 0
    frame = 0
    while x < 800:
        clear_canvas()
        grass.draw(400, 30)
        if j_count >= 4:
            y += 30

        elif j_count < 4:
            y -= 40

        j_count -= 1

        character.clip_draw(frame * 80, 1024 - (80 * depth), 85, 85, x, y)
        update_canvas()
        frame = (frame + 1) % cannes
        x += fast
        if j_count == 0:
            j_count = 7
            y = 90
        delay(d_time)
        get_events()

def step():
    global  cannes, d_time
    fast = 10
    for depth in range(1, 6):
        if depth == 1:
            #walk
            cannes = 9
            d_time = 0.05

        elif depth == 2:
            #crawl
            cannes = 12
            d_time = 0.05

        elif depth == 3:
            #flutter
            cannes = 7
            d_time = 0.05

        elif depth == 4:
            #surprise
            cannes = 8
            d_time = 0.05

        elif depth == 5:
            #attack
            cannes = 6
            d_time = 0.05

        move(depth)

    for depth in range(9, 11):
        if depth == 9:
            #jump
            cannes = 7
            d_time = 0.1
            fast = 10

        elif depth == 10:
            #run and jump
            cannes = 12
            d_time = 0.05
            fast = 20

        jumpmove(depth, fast)

step()


close_canvas()