# python grid.py
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Radio")
root.iconbitmap('images/unisa.ico')

def popup():
    response = messagebox.askyesno("This is my popup", "Hello world")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="yes clicked").pack()
    else:
        Label(root, text="no clicked").pack()
        

Button(root, text="popup", command=popup).pack()

root.mainloop()