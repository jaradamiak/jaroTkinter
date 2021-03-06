# python grid.py
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Windows")
root.iconbitmap('images/unisa.ico')

# root.filename = filedialog.askopenfilename(initialdir="images", title="Select a file", 
#                                            filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), 
#                                                       ("all files", "*.*")))
# my_label = Label(root, text=root.filename).pack()
# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# my_image_label = Label(image=my_image).pack()

def open():
    global my_image 
    root.filename = filedialog.askopenfilename(initialdir="images", title="Select a file", 
                                           filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), 
                                                      ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open file", command=open).pack()

root.mainloop()