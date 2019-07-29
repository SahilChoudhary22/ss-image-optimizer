# Importing the required modules

from PIL import Image as pilimg
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path


# Initializing the Tkinter Module
root = Tk()
root.title("Super Simple Image Optimizer")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.pack()


w = Text(root, bd =8)
w.insert(INSERT, 'Super Simple Image Optimizer')
w.pack()


# Adding the browse function, the file gets optimized as soon as you browse it. 
def browsefunc():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg *.jpeg"),("png files","*.png"),("bmp files","*.bmp"),("all files","*.*")))
    pathlabel.config(text=filename)
    patho = filename
    openimg(patho)
    
def openimg(filepath):
    in_Image = pilimg.open(filepath)
    width, height = in_Image.size
    justFileName = Path(filepath).name
    justOptimize(in_Image, justFileName)

browsebutton = Button(root, text="Browse file to optimize", command=browsefunc)
browsebutton.pack()

pathlabel = Label(root)
pathlabel.pack()


# Optimization, quality currently set to 50%
def justOptimize(image, justfilename):
    finname = justfilename + "ssio.jpg"
    newImage = image.resize((width,height), pilimg.ANTIALIAS)
    newImage.save(finname , optimize = True,quality = 50)

# Runs the tkinter module window
root.mainloop()




