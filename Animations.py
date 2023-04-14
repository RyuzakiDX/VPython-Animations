from time import *
from tkinter import *

from vpython import *

root = Tk()
root.geometry("550x250")

def animation():
    heightOFroom = 10
    lenghtOFroom = 10
    breathOFroom = 10

    cieling =  box(pos = vector(0,5,0),size = vec(10,.1,10),color=color.white)
    floor =  box(pos = vector(0,-5,0), width = 10, height = .1, length=10 , color=color.white)
    leftwall =  box(pos = vector(-5,0,0),size = vec(.1,10,10) , color = color.white )
    #rightwall =  box(pos = vector(5,0,0), width = 10, height = 10, length=.1, color = color.yellow)
    #backwall =  box(pos = vector(0,0,-5), width = .1, height = 10, length=10 , color = color.yellow)
    ball = sphere(pos= vec(0,0,0),color=color.red)

    deltaX = .1
    xPos = 0 
    yPos = 0
    deltaY = .1
    x1Pos = -5
    deltaX1 = .1
    while True:
       rate(10)
       xPos = xPos + deltaX
       if xPos > 5:
          yPos = yPos + deltaY
          if yPos > 4:
            deltaY = 0
            deltaX = -0.1
       elif xPos < -5:
          yPos = yPos + deltaY
          if yPos > 4:
             deltaY = 0
             deltaX = 0.1
       ball.pos = vec(xPos,yPos,0)

def animation2():
    floor = box(pos = vector(0,-5,0),color=color.black, length = 10, width = 10,height = .1 )
    sleep(1)
    floor = box(pos = vector(0,-5,0),color=color.purple, length = 10, width = 10,height = .1 )
    sleep(1)
    chaat = box(pos = vector(0,5,0),color=color.purple, length = 10, width = 10,height = .1 )
    sleep(1)
    diwaar = box(pos = vector(-5,0,0),color=color.purple, length = .1, width = 10,height = 10 )
    sleep(1)
    uranium = sphere(pos = vec(0,0,0),)
    sleep(2)

    uranium.color = color.blue
    sleep(1) 
    floor.color = color.cyan
    sleep(1)
    diwaar.color = color.yellow
    sleep(1)
    chaat.color = color.green
    sleep(1) 

    
l = Label(
    root,
    text = "Howdyy, click on the button to see the animation :))",
    font = "lucida 20 bold",
)
l.place(x=20,y=10)

btn1 = Button(
    root,
    text = "ball animation",
    font = "lucida 35 bold",
    command=animation

)
btn1.place(x=200,y=100)


btn2 = Button(
    root,
    text = "color animation",
    font = "lucida 35 bold",
    command=animation2

)
btn2.place(x=200,y=150)





root.mainloop()