from pico2d import *

open_canvas()
bana = load_image('ninza.png')
grass = load_image('grass.png')

#1
frame=0
for y in range (600, 110, -5):
    clear_canvas()
    grass.draw(400,30)
    bana.clip_draw(frame*128, 512, 128, 128, 400, y)
    update_canvas()
    frame = (frame-1)%8
    delay(0.04)
    get_events

#2
x = 400
frame=0
for x in range (400, 0, -5):
    clear_canvas()
    grass.draw(400,30)
    bana.clip_draw(frame*128, 384, 128, 128, x, 110)
    update_canvas()
    frame = (frame-1)%8
    delay(0.03)
    get_events

#2
x = 800
frame=0
for x in range (800, 400, -5):
    clear_canvas()
    grass.draw(400,30)
    bana.clip_draw(frame*128, 384, 128, 128, x, 110)
    update_canvas()
    frame = (frame-1)%8
    delay(0.03)
    get_events

#4
x = 400
frame=0
for x in range (400, 375, -5):
    clear_canvas()
    grass.draw(400,30)
    bana.clip_draw(frame*128, 1024, 128, 128, x, 110)
    update_canvas()
    frame = (frame-1)%5
    delay(0.03)
    get_events

#5
x = 375
frame=0
for x in range (375, 325, -5):
    clear_canvas()
    grass.draw(400,30)
    bana.clip_draw(frame*128, 896, 128, 128, x, 110)
    update_canvas()
    frame = (frame-1)%5
    delay(0.08)
    get_events

#6
x = 325
frame=0
for x in range (325, 0, -5):
    clear_canvas()
    grass.draw(400,30)
    bana.clip_draw(frame*128, 256, 128, 128, x, 110)
    update_canvas()
    frame = (frame-1)%8
    delay(0.05)
    get_events

#7
x = 800
frame=0
for x in range (800, 0, -5):
    clear_canvas()
    grass.draw(400,30)
    bana.clip_draw(frame*128, 0, 128, 128, x, 110)
    update_canvas()
    frame = (frame-1)%10
    delay(0.05)
    get_events


close_canvas()



