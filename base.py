# python grid.py
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Windows")
root.iconbitmap('images/unisa.ico')

def open():
    global my_img
    top=Toplevel()
    top.title("Second Window")
    top.iconbitmap('images/headphone.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/AAHtU6t.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()

root.mainloop()