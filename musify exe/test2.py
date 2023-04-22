import math
import tkinter as tk
from tkinter import ttk

def pendulum_motion(angle):
    global r
    x = r*math.sin(angle)
    y = r*math.cos(angle)
    pendulum.coords(pendulum_string, x, y, 0, 0)
    pendulum_window.after(50, pendulum_motion, angle+0.1)

pendulum_window = tk.Tk()
pendulum_window.title("Pendulum Simulation")

r = 150
angle = math.radians(45)

pendulum = tk.Canvas(pendulum_window, width=300, height=300)
pendulum.pack()
pendulum_string = pendulum.create_line(10, 10, 100, 100, width=2)

scale = ttk.Scale(pendulum_window, from_=0, to=90, orient='horizontal', command=pendulum_motion)
scale.pack()

pendulum_motion(angle)
pendulum_window.mainloop()
