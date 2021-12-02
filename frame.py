# python grid.py
from tkinter import *

root = Tk()
root.title("Frames")
root.iconbitmap('images/unisa.ico')

frame = LabelFrame(root, text="my frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="here is the frame")
b2 = Button(frame, text="another button")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()