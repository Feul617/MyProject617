from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def rander_all(x, y):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def run_circle():
    print('circle')

    cx, cy, r = 800 / 2, 300, 200
    for deg in range(0, 360):
        x = cx + r * math.cos(deg/360 * 2 * math.pi)
        y = cy + r * math.sin(deg/360 * 2 * math.pi)
        rander_all(x, y)

def run_rectangle():
    print('rectangle')

    #bottom line
    for x in range(50,750+1, 10):
        rander_all(x, 90)

     #right line
    for y in range(90, 550 + 1, 10):
        rander_all(750, y)

    #top line
    for x in range(750, 50 - 1, -10):
        rander_all(x, 550)

    #left line
    for y in range(550, 90 - 1, -10):
         rander_all(50, y)
    
while True:
    run_circle()
    run_rectangle()
    
close_canvas()
