# python grid.py
from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


e.pack()
e.insert(0, "Enter your name")

def myClick():
    hello = "Hello @ " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter name", command=myClick, fg="blue", bg="yellow")
myButton.pack()

root.mainloop()