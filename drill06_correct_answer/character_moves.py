import math

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)



def run_circle(): #run_circle() 빈함수
    print('circle')
    cx = 400 #800/2
    cy =300 #600/2
    r = 200 #반지름
    for deg in range (0, 360, 5): #0~360도 까지 5도(step : 단위)씩 움직인다.
        x = cx + r*math.cos(deg/360*2*math.pi) #각도(세타)를 라디안으로 바꿔 줌 / deg는 위에 각
        y = cy + r*math.sin(deg/360*2*math.pi)
        render_all(x,y)
  

def run_rectangle(): #run_rectangle() 빈함수
    print('rectangle')

    #BOTTOM LINE
    for x in range(50-1, 750, 10): #x 값을 50부터 750까지 10씩 증가
        render_all(x,90)

    #RIHGT LINE
    for y in range(80, 600, 10):
        render_all(750, y)
   

    #TOP LINE
    for x in range(750, 50-1, -10):
        render_all(x,550)

    #LEFT LINE
    for y in range(600, 80, -10):
        render_all(30, y)
        
    



while True: #무한 루트
    run_rectangle() #사각 운동
    run_circle() #원 운동
    #break
    


close_canvas()