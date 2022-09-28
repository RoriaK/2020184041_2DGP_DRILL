from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 0
frame = 0
for x in range (0, 800, 5):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*100, 0, 100, 100, x, 90, 400, 400) #clip 짤라서 그리겠다.
    update_canvas()
    frame = (frame+1) %8
    # x가 800보다 작을 동안 frame을 계속 증가 시켜 간다.= frame+1 (frame은 0 부터)
    # %8= 더하기를 한 다음에 나머지 8을 해 줌 = 0, 1, 2, 3, 4, 5, 6, 7, 8%8=0 그러므로 frame=0(다시 시작)
    #frame*100 여기서 100은 잘라 내고자 하는 단위
    delay(0.01)
    get_events()

close_canvas()

