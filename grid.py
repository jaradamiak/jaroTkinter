# python grid.py
from tkinter import *

root = Tk()
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is")
myLabel3 = Label(root, text="Welcome to TKinter")
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=3, column=2)

root.mainloop()