from tkinter import Y
from pico2d import *

winWidth = 1287
winHeight = 725

def handle_events():
    global running
    global dirx, diry
    global odd_y, even_y
    global odd_dir, even_dir

    if odd_y < 180:
        odd_dir = 1
    elif odd_y > 520:
        odd_dir = -1

    odd_y += odd_dir*10


    if even_y < 180:
        even_dir = 1
    elif even_y > 520:
        even_dir =-1

    even_y += even_dir*10


    events = get_events()
    
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx = 1
            elif event.key == SDLK_LEFT:
                dirx = -1
            elif event.key == SDLK_UP:
                diry = 1
            elif event.key == SDLK_DOWN:
                diry = -1
            elif event.key == SDLK_ESCAPE:
                running = False


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_ESCAPE:
                running = False
            else:
                dirx = diry = 0

open_canvas(winWidth, winHeight)

ima = load_image('ima.png')
character = load_image('monster.png')
black = load_image('black.png')


running = True
x = 150
y = 375
dirx = 0
diry = 0

odd_y = 350
even_y = 350
odd_dir = 1
even_dir = -1

while running:
    clear_canvas()
    ima.draw(winWidth//2, winHeight//2)

    for i in range(6):
        black.clip_draw(0, 0, 1200, 1200, 250+150*i, odd_y if i%2 == 0 else even_y, 50, 50)

    character.clip_draw(0 , 0, 1200, 1200, x, y,100,100)

    update_canvas()

    handle_events()

    if y >= 350 and y <= 400:
        if (x >= 90 or dirx == 1) and (x <= 1200 or dirx == -1):
            x += dirx * 5
    elif y >= 170 and y <= 550:
        if (x >= 250 or dirx == 1) and (x <= 1040 or dirx == -1):
            x += dirx * 5
    
    if x >= 250 and x <= 1040:
        if (y >= 170 or diry == 1) and (y <= 550 or diry == -1):
            y += diry * 5
    elif x >= 90 and x <= 1200:
        if (y >= 350 or diry == 1) and (y <= 400 or diry == -1):
            y += diry * 5

    delay(0.01)

close_canvas()