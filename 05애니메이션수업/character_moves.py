from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0 #x의 값 초기화
for x in range(0, 800+1, 2): #0부터  800+1까지 2씩 움직여라
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    update_canvas()
    delay(0.001)
    get_events()

close_canvas()

