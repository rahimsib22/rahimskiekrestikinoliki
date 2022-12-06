from tkinter import *
from tkinter import messagebox
import time
import random


tk = Tk()
app_running = True

def on_clothing():
    global app_running
    if messagebox.askokcancel("Quit", "do you wont to quit?"):
        app_running = False
        tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_clothing)
tk.title("Крестики нолики от Рахима(пожалуста можно не летник")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=768, height=768, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

while 1:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)