#!/usr/bin/env python
# coding: utf-8

# ==================================================================================================================

# #                                         <center>|| Super Simple Image Optimizer || </center>

#  _<center> | By https://github.com/SahilChoudhary22 |</center>_
# 

# ==================================================================================================================

# ## Importing the required modules

# In[101]:


from PIL import Image as pilimg
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path


# ## Initializing the Tkinter Module

# In[102]:


root = Tk()
root.title("Super Simple Image Optimizer")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.pack()


# In[103]:


w = Text(root, bd =8)
w.insert(INSERT, 'Super Simple Image Optimizer')
w.pack()


# ## Adding the browse function, the file gets optimized as soon as you browse it. 

# In[104]:


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


# ## Optimization, quality currently set to 50%

# In[105]:


def justOptimize(image, justfilename):
    finname = justfilename + "ssio.jpg"
    newImage = image.resize((width,height), pilimg.ANTIALIAS)
    newImage.save(finname , optimize = True,quality = 50)


# In[106]:


root.mainloop()


# ---------------------

# TODO :
# 
# 1) Add slider to set quality [ ]
# 
# 2) Add a button to optimize instead of direct optimization on browsing [ ]
# 
# 3) Beautify the interface [ ]
# 
# 4) Add resizing and other functionalities [ ]

# In[ ]:




