from pico2d import *

def handle_events():
    global running
    global dirx, diry
    global sight

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                sight = 100
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
                sight = 0
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1

    pass

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


dirx = 0
diry = 0
running = True
x = 800 // 2
y = 600 // 2
frame = 0
sight = 0

while running:
    clear_canvas()
    grass.draw(400, 90)
    character.clip_draw(frame * 100, sight * 1, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if 30 <= x <= 770:
        x += dirx * 5
    elif x > 770:
        x -= 1
    elif x < 30:
        x += 1
    if 30 <= y <= 570:
        y += diry * 5
    elif y > 570:
        y -= 1
    elif y < 30:
        y += 1
    delay(0.01)

close_canvas()