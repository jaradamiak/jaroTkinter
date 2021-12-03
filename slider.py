# python grid.py
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Windows")
root.iconbitmap('images/unisa.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide(var):
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x" + str(vertical.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()

ny_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()