# python grid.py
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Windows")
root.iconbitmap('images/unisa.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()
c= Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myLabel = Label(root, text=var.get()).pack()
myButon = Button(root, text="Show selection", command=show).pack()

root.mainloop()