# python grid.py
from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title("Simple Calculator")
root.iconbitmap('images/unisa.ico')

my_img = ImageTk.PhotoImage(Image.open('images/AAHuaVF.jpg'))
myLabel = Label(image=my_img)
myLabel.pack()

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()