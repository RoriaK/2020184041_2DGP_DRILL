from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character=load_image('character.png')

x=0
while(x<770):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,90)
    x = x+2
    delay(0.01)

y=90
while(y<540):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(770,y)
    y = y+2
    delay(0.01)

x=770
y=550
while(30<x):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,y)
    x = x-2
    delay(0.01)

x=10
y=550
while(90<y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(10,y)
    y = y-2
    delay(0.01)

x=400
y=600
ceta=0
while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x=300*cos(ceta)+400
    y=300*sin(ceta)+300
    ceta+=1
    delay(0.01)


close_canvas()
