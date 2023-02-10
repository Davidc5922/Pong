import turtle
import threading
import time
from playsound import playsound

#AREA DE JUEGO
wn=turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Marcador
score_a=0
score_b=0

#Pala A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Pala B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#LINEA DIVISORIA
line=turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("gray")
line.shapesize(stretch_wid=30,stretch_len=0.07)
line.penup()
line.goto(0,0)

#PELOTA
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.9
ball.dy=0.9
static=True

#MARCADOR INICIAL
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-2.5,220)
pen.write("0         0",align="center",font=("Fixedsys",60,"bold"))

#MENSAJE "ENTER"
pen2=turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,120)
pen2.write("PRESS ENTER TO START",align="center",font=("Fixedsys",24,"bold"))

#MOVER PALA "A" HACIA ARRIBA
def paddle_a_up():
    y=paddle_a.ycor()
    if y <=240:
        y+=20
        paddle_a.sety(y)
#MOVER PALA "A" HACIA ABAJO
def paddle_a_down():
    y=paddle_a.ycor()
    if y >=-220:
        y-=20
        paddle_a.sety(y)
#MOVER PALA "B" HACIA ARRIBA
def paddle_b_up():
    y=paddle_b.ycor()
    if y <=240:
        y+=20
        paddle_b.sety(y)
#MOVER PALA "B" HACIA ABAJO
def paddle_b_down():
    y=paddle_b.ycor()
    if y >=-220:
        y-=20
        paddle_b.sety(y)

#REPRODUCCION DE SONIDO
def play_sound():
    playsound("pong.mp3")   

#INICIAR TAREA EN SEGUNDO PLANO
def ini_playsoun():
    t=threading.Thread(target=play_sound)
    t.start()         
#REPRODUCCION DE SONIDO
def play_sound2():
    playsound("point.mp3")   

#INICIAR TAREA EN SEGUNDO PLANO
def ini_playsoun2():
    t=threading.Thread(target=play_sound2)
    t.start()         

#INICIAR JUEGO  
def init_game():   
    global static
    static = False
    pen2.clear()

#RESTAURAR PANTALLA DE INICIO
def reset_screen():
    ball.goto(0,0)
    ball.dx *=-1  
    pen2.write("PRESS ENTER TO START",align="center",font=("Fixedsys",24,"bold"))
    paddle_a.goto(-350,0)
    paddle_b.goto(350,0)
#ACTUALIZA MARCADOR
def update_score():
    pen.clear()
    pen.write("{}         {}".format(score_a,score_b),align="center",font=("Fixedsys",60,"bold"))    


#REGISTRAR EVENTOS DE TECLADO
wn.listen()
wn.onkeypress(paddle_a_up,"w")   
wn.onkeypress(paddle_a_down,"s")   
wn.onkeypress(paddle_b_up,"Up")   
wn.onkeypress(paddle_b_down,"Down")   
wn.onkeypress(init_game,"Return")   

#DESARROLO DEL JUEGO
while True:
    try:
        wn.update()
        #MOVER PELOTA
        if static == False:
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
        #REBOTE EN EL MARGEN SUPERIOR    
        if ball.ycor() >290:
            ball.sety(290)
            ball.dy *=-1
            ini_playsoun()
        #REBOTE EN EL MARGEN INFERIOR    
        if ball.ycor() <-290:
            ball.sety(-290)
            ball.dy *=-1
            ini_playsoun()
        #PELOTA SOBREPAS LA PALA B
        if ball.xcor()>390:
            score_a +=1
            update_score()
            static=True
            time.sleep(1)
            ini_playsoun2()
            reset_screen()
        #PELOTA SOBREPAS LA PALA A
        if ball.xcor()<-390:
            score_b +=1
            update_score()
            static=True
            time.sleep(1)
            ini_playsoun2()
            reset_screen()
        #REBOTE EN LA PALA B
        if (ball.xcor()>340 and ball.xcor()<350)and(ball.ycor()<paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
            ball.setx(340)
            ball.dx *= -1
            ini_playsoun()    
        #REBOTE EN LA PALA A
        if (ball.xcor()<-340 and ball.xcor()>-350)and(ball.ycor()<paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
            ball.setx(-340)
            ball.dx *= -1
            ini_playsoun()    
    except:
        break        