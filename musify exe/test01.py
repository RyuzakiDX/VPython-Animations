from tkinter import*
import webbrowser

def callback(url):
    webbrowser.open_new(url)


root = Tk()
root.geometry("600x500")

mylabel = Label(
    root,
    text= "Youtube",
    font="lucida 20 bold"
)
mylabel.pack()
mylabel.bind("<Button-1>",lambda e: callback("https://www.youtube.com/"))

def hover(e):
    homebtn["highlightbackground"]="blue"

def hoverleave(e):
    homebtn["highlightbackground"]="black"

homebtn = Button(
    root,
    text="PW"            
)
homebtn.place(x=150,y=165)

homebtn.bind("<Button-1>",lambda e: callback("https://www.youtube.com/"))
homebtn.bind("<Enter>",hover)
homebtn.bind("<Leave>",hoverleave)

root.mainloop()