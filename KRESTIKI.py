from tkinter import *
from tkinter import messagebox
import time
import random


tk = Tk()
app_running = True

size_canvas_x = 768
size_canvas_y = 768

def on_clothing():
    global app_running
    if messagebox.askokcancel("Выйти?", "пж не уходите"):
        app_running = False
        tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_clothing)
tk.title("Крестики нолики от Рахима(пожалуста можно не летник")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0,0, size_canvas_x, size_canvas_y, fill = "white")
canvas.pack()
tk.update()

s_x = 3
s_y = 3
step_x = size_canvas_x // s_x
step_y = size_canvas_y // s_y
def draw_table():
    for i in range(0, s_x+1):
        canvas.create_line(0,i*step_y,size_canvas_x,i*step_y)
    for i in range(0, s_y+1):
        canvas.create_line(i*step_y,0,i*step_y,size_canvas_y,)

points = []
draw_table()

class Point:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

def draw_point(x, y, type):
    size = 25
    color = "black"
    id = 0
    if type == 0:
        color = "red"
        id = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_x, fill=color)
        id = canvas.create_oval(x * step_x+size, y * step_y+size, x * step_x + step_x-size, y * step_y + step_x-size, fill='white')
    if type == 1:
        color = "blue"
    #id = canvas.create_oval(x*step_x, y*step_y, x*step_x+step_x, y*step_y+step_x, fill=color)




def add_to_points(event):
    print(event.num, event.x, event.y)
    type = 0
    if event.num == 3:
        type = 1
    points.append(Point(event.x // step_x, event.y // step_y, type))
    draw_point(event.x // step_x, event.y // step_y, type)
    print(" ", join(map(str, points)))

canvas.bind_all("<Button-1>", add_to_points) #ЛKM
canvas.bind_all("<Button-3>", add_to_points) #ПKM




while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)