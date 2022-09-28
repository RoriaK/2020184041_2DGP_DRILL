from pico2d import *

open_canvas()
girl = load_image('girl.png')

x = 0
frame = 0
for x in range (0, 800, 5):
    clear_canvas()
    girl.clip_draw(frame*208, 0, 208, 208, x, 110)
    update_canvas()
    frame = (frame+1) % 6
    delay(0.03)
    get_events()

close_canvas()

