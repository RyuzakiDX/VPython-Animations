
import sys
from tkinter import *

sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/to/pygame')
import pygame

pygame.mixer.init()
root = Tk()

root.geometry("1980x800")
root.title("MUSIFY")

img1 = PhotoImage(file="musify exe/Screenshot 2022-09-18 at 10.05.33 AM.png")
Supremeimg = PhotoImage(file="musify exe/like supreme img.png")
cjrapimg = PhotoImage(file="musify exe/cji mg 2.png")
exitbtnimg = PhotoImage(file="musify exe/Exit btn 2.png")
neverfadeawayimg = PhotoImage(file="musify exe/Screenshot 2022-09-24 at 2.07.38 PM.png")
brokendreams = PhotoImage(file="musify exe/Screenshot 2022-09-24 at 2.03.11 PM.png")
viwallimg = PhotoImage(file="musify exe/View all.png")
viwallimg2gui = PhotoImage(file="musify exe/All music 2 gui.png")
viewallimg3gui = PhotoImage(file="musify exe/Screenshot 2022-10-17 at 9.51.51 PM.png")
viewall4gui = PhotoImage(file="musify exe/viewall gui 4.png")
img2  = PhotoImage(file="musify exe/Screenshot 2022-09-24 at 2.13.05 PM.png")
imghome = PhotoImage(file="musify exe/Screenshot 2022-09-24 at 9.23.12 AM.png")
backimg = PhotoImage(file="musify exe/Screenshot 2022-09-24 at 10.00.08 AM.png")
pauseimg = PhotoImage(file="musify exe/Pause img.png")
chippinimg = PhotoImage(file="musify exe/chippin2.png")
supremepg2 = PhotoImage(file="musify exe/supreme pag2.png")

scr1 = Label(
    image=img1
)
scr1.place(x=0,y=0)
    

def Home():
    global Home
    
    homebtn.destroy()
    scr1.destroy()
    newscreen()

    
def back():
    global back
    scr2 .destroy()
    backbtn.destroy()
    

    scrback = Label(
        image=img1
    )
    scrback.place(x=0,y=0)
    
    def hover1(e):
      homebtn1["highlightbackground"]="blue"

    def hoverleave1(e):
     homebtn1["highlightbackground"]="black"
    
    homebtn1 = Button(
    root,
    image= imghome,
    command=Home
    )
    homebtn1.place(x=150,y=165)
    homebtn1.bind("<Enter>",hover1)
    homebtn1.bind("<Leave>",hoverleave1)

    exitbtn = Button(
    root,
    image= exitbtnimg,
    command= Exit
    )
    exitbtn.place(x = 690,y=690)

    pygame.mixer.music.stop()


def viewall():
    global viewall
    scr2.destroy()
    nerverbtn.destroy()
    exitbtn.destroy()
    dreambtn.destroy()
    viewallbtn.destroy()
    backbtn.destroy()
    viewallscrn()

def cjrap():
    def nextsupreme():
        viewallscrn()
        Alikesupreme()
        nextmusic.destroy()
        stopcj.destroy()
        cj1.destroy()

    def cjstop():
      global stop
      pygame.mixer.music.stop()
      stopcj.destroy()  
      nextmusic.destroy()
      cj.destroy()
      viewallscrn()
       
    global stopcj
    global cjrap
    pygame.mixer.music.load("musify exe/GTA San Andreas CJ rap.mp3")
    pygame.mixer.music.play(loops=0)
    stopcj = Button(
        root,
        image=pauseimg,
        command=cjstop
    )
    stopcj.place(x=1055,y=250)
    nextmusic = Button(
        root,
        text="next",
        font="lucida 20 bold",
        command=nextsupreme
    ) 
    nextmusic.place(x=1050,y=350)
    cj1 = Button(
        root,
        image=cjrapimg,
        command=cjrap,
        highlightbackground="blue"
    )
    cj1.place(x= 400,y=110)
    
def Alikesupreme():
    global Alikesupreme
    pygame.mixer.music.load("musify exe/A like supreme.mp3")
    pygame.mixer.music.play(loops=0)
    supreme.destroy()

    def nextdream():
        viewallscrn()
        mydream()
        nextdreambtn.destroy()
        stopsupremebtn.destroy()
        supreme1.destroy()
        
        

    def stopsupreme():
        pygame.mixer.music.stop()
        stopsupremebtn.destroy()
        nextdreambtn.destroy()
        viewallscrn()
        
  
    stopsupremebtn = Button(
        root,
        image=pauseimg,
        command=stopsupreme
    )
    stopsupremebtn.place(x=1055,y=250)

    nextdreambtn = Button(
        root,
        text="Next",
        font = "lucida 20 bold",
        command=nextdream
    )
    nextdreambtn.place(x=1050,y=350)
    supreme1 = Button(
        root,
        image = Supremeimg,
        command=Alikesupreme,
        highlightbackground="blue"

    )
    supreme1.place(x=700,y=100)

def mydream():
    global mydream
    pygame.mixer.music.load("musify exe/Drew_McIntyre_Custom_Titantron__Broken_Dreams_RE_UPLOADMP3_128K.mp3")
    pygame.mixer.music.play(loops=0)
    dreambtn.destroy()

    def mydreamstop():
        pygame.mixer.music.stop()
        stopdrambtn.destroy()
        viewallscrn()

    stopdrambtn = Button(
        root,
        image=pauseimg,
        command=mydreamstop
    )    
    stopdrambtn.place(x=1055,y=250)
    dreambtn1 = Button(
        root,
        image=brokendreams,
        command=mydream,
        highlightbackground="blue"
    )
    dreambtn1.place(x=100,y=300)
        
def viewallscrn():
    global viewallscrn
    global viwallimg
    global backbtn2
    global scr3
    global nfd
    global supreme
    global cj


    scr3 = Label(
        image=viewall4gui
    )
    scr3.place(x=0,y=0)

    nfd = Button(
        root,
        image = neverfadeawayimg,
        command=nfy
    )
    nfd.place(x=100,y=100)

    def cjhover(e):
        cj["highlightbackground"]="green"        
    def notcjhover(e):
        cj["highlightbackground"]="black"
    cj = Button(
        root,
        image=cjrapimg,
        command=cjrap,
    )
    cj.place(x= 400,y=110)
    cj.bind("<Enter>",cjhover)
    cj.bind("<Leave>",notcjhover)
    
    def supremehover(e):
        supreme["highlightbackground"]="purple"
    def notsupremehover(e):
        supreme["highlightbackground"]="black"

    supreme = Button(
        root,
        image = Supremeimg,
        command=Alikesupreme

    )
    supreme.place(x=700,y=100)
    supreme.bind("<Enter>",supremehover)
    supreme.bind("<Leave>",notsupremehover)
    
    def upu(e):
        dreambtn["highlightbackground"]="cyan"
    def upuleave(e):
        dreambtn["highlightbackground"]="black"    

    dreambtn = Button(
        root,
        image=brokendreams,
        command=mydream,
    )
    dreambtn.place(x=100,y=300)
    dreambtn.bind("<Enter>",upu)
    dreambtn.bind("<Leave>",upuleave)

    chippinbtn = Button(
        root,
        image=chippinimg,
    )
    chippinbtn.place(x=400,y=300)

    backbtn2 = Button(
        root,
        image=backimg,
        command=back,
    )
    backbtn2.place(x=6,y=8)


def nfy():
    global stopnfy
    global nfy
    nfd.destroy()
    def nfystop():
      global stop
      pygame.mixer.music.stop()
      stopnfy.destroy()    
      viewallscrn()

      
    pygame.mixer.music.load("musify exe/Never fade away.mp3")
    pygame.mixer.music.play(loops=0)
    stopnfy = Button(
        root,
        image=pauseimg,
        command=nfystop
    )
    stopnfy.place(x=1055,y=250) 
    nfd1 = Button(
        root,
        image = neverfadeawayimg,
        command=nfy,
        highlightbackground="blue"
    )
    nfd1.place(x=100,y=100)

def aboutdev():
    scr2.destroy()
    nerverbtn.destroy()
    mebtn.destroy()
    dreambtn.destroy()    
    exitbtn.destroy()
    supreme2.destroy()
    viewallbtn.destroy()

    mylabel = Label(root,text="0100101100000000000000000000000000000000000000000000010110010101010101010001100101001010110010101010101010100101\n0100101100000000000000000000000000000000000000000000010110010101010101010001100101001010110010101010101010100101\n010101001010101010101001010101010101010011001010101\n01101010010101011010101010101010101010101\n1001101000101010101010101001010101010101010101010\n010110010101010101010101010101010010101010\n10101010010101010101010100101010101010101010101010\n011010010101010101010010101010101010101010101010101010\n010101001011010010101010101010101011\n0101010101010101010101010100101001010010010101010101010101010101010101010101010101010101010100101010101010101010101010101010101010010110011001\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110\n101001010101100101100101010101010101010101010101010101010101010101010010101010101010101010010101010110010101010101010110101001010101010110",font="lucida 15 bold",fg="green")
    mylabel.pack()    

def newscreen():
    global newscreen
    global scr2
    global backbtn
    global nerverbtn
    global dreambtn
    global viewallbtn
    global mebtn
    global supreme2


    scr2 = Label(
        image=img2
    )
    scr2.place(x=0,y=0)

    backbtn = Button(
        root, 
        image = backimg,
        command= back

    )
    backbtn.place(x=6,y=8)
    
    nerverbtn = Button(
        root,
        image=neverfadeawayimg,
        command=nfy

    )
    nerverbtn.place(x=400,y=500)

    dreambtn = Button(
        root,
        image=brokendreams,
        command=mydream
    )
    dreambtn.place(x=800,y=500)

    viewallbtn = Button(
        root,
        text = "View All",
        font = "lucida 35 bold",
        command= viewall,
        highlightbackground="yellow"
    )
    viewallbtn.place(x=100,y=380)
    
    mebtn = Button(
        root,
        text="About Dev.",
        font="lucida 35 bold ",
        command=aboutdev,
    )
    mebtn.place(x=100,y=580)
    def suprme2():
     pygame.mixer.music.load("musify exe/A like supreme.mp3")
     pygame.mixer.music.play(loops=0)


    supreme2 = Button(
        root,
        image=supremepg2,
        command=suprme2,
        background="black",
        highlightbackground="black"
    )
    supreme2.place(x=100,y=210)
    

def hover(e):
    homebtn["highlightbackground"]="blue"

def hoverleave(e):
    homebtn["highlightbackground"]="black"

homebtn = Button(
    root,
    image= imghome,
    command=Home,
    
            
)
homebtn.place(x=150,y=165)

homebtn.bind("<Enter>",hover)
homebtn.bind("<Leave>",hoverleave)


def Exit():
    global Exit
    root.destroy()

exitbtn = Button(
    root,
    image= exitbtnimg,
    command= Exit,
    highlightbackground="red"

)
exitbtn.place(x = 690,y=690)

root.mainloop()