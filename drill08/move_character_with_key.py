from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600

def handle_events():
    global running
    global dirx
    global diry
    global state
    global isrun

    events = get_events()
    
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        ###KEY DOWN
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                state = 1
                dirx +=1
            elif event.key == SDLK_LEFT:
                state = 0
                dirx -=1
            elif event.key == SDLK_UP:
                if state==2:
                    state = 0
                if state==3:
                    state = 1
                diry +=1
            elif event.key == SDLK_DOWN:
                if state == 2:
                    state = 0
                if state == 3:
                    state = 1
                diry -=1
            elif event.key == SDLK_ESCAPE:
                running = False

            isrun = True

        #### Key UP
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                state = 3
                dirx =0
            elif event.key == SDLK_LEFT:
                state = 2
                dirx =0
            elif event.key == SDLK_UP:
                if state == 1:
                    state = 3
                else:
                    state = 2
                diry =0
            elif event.key == SDLK_DOWN:
                if state == 1:
                    state = 3
                else:
                    state = 2
                diry =0
            elif event.key == SDLK_ESCAPE:
                running = False

            isrun = False

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

isrun = False

running = True
x = 800 // 2
y = 600 //2
frame = 0
state = 2
dirx = 0
diry = 0

while running:
    clear_canvas()
    grass.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    character.clip_draw(frame * 100, state * 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    if isrun:
        frame = (frame + 1) % 8
    x+=dirx*5
    y+=diry*5
    delay(0.01)

close_canvas()