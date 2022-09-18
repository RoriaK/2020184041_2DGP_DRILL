import turtle
x=0 #x의 초기값
y=0 #y의 초기값
while(y<500): #사각형 1개 그리기 5번 반복, 5번 반복
    x=0
    #사각형 1개 그리기 5번 반복
    while(x<500):
        turtle.goto(x,y) #x,y로 이동한다.
        turtle.pendown() #펜을 내려놓는다.
        #사각형 1개 그리기
        count = 4 #4번 반복한다.
        while (count>0):
            turtle.forward(100) #앞으로 100간다.
            turtle.left(90) #왼쪽으로 90도 꺾는다.
            count -= 1 #1씩 count를 줄여준다.
        x +=100 #x를 100 증가시킨다.
        turtle.penup()
    y+=100
