from pico2d import *

import math
math.sin(270 / 360*2*math.pi)

open_canvas()

grass = load_image('grass.png')
character=load_image('character.png')

x=0
while(x<800):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,90)
    x = x+2
    delay(0.01)

y=90
while(y<550):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(770,y)
    y = y+2
    delay(0.01)

x=770
y=550
while(100<x):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,y)
    x = x-2
    delay(0.01)

x=10
y=550
while(10<y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(10,y)
    y = y-2
    delay(0.01)

close_canvas()