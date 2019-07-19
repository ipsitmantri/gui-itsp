from tkinter import *
#import cv2
import os
import pickle
import urllib.request as url
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
import numpy as np
import time
import threading
import webbrowser


root = Tk()
v = IntVar()
new = 1
url1= "https://github.com/fathimazarin/star42"
url2="https://docs.google.com/document/d/1DEzzMaNtRvxnJgG-Jnkvsit0Y96FQ4fjLhor5J2GeB8/edit"
def openweb1():
	webbrowser.open(url1,new = new)

def openweb2():
	webbrowser.open(url2,new = new)

def hello():  
    print("hello!")

def takeinput1():
	#filename= 'C:/Users/Meeta Malviya/AppData/Local/Programs/Python/Python37-32/geminitemp.png'
	#define file loation on comp
	filename= 
	global img 
	img = Image.open(filename)
	photo = ImageTk.PhotoImage(img)
	label1 = Label(image = photo)
	label1.image = photo
	label1.pack(anchor = S)

def takeinput2():
	#filename= 'C:/Users/Meeta Malviya/AppData/Local/Programs/Python/Python37-32/geminitemp.png'
	#define file location on comp
	filename =
	global img 
	img = Image.open(filename)
	photo = ImageTk.PhotoImage(img)
	label1 = Label(image = photo)
	label1.image = photo
	label1.pack(anchor = S)

def takeinput3():
	#filename= 'C:/Users/Meeta Malviya/AppData/Local/Programs/Python/Python37-32/geminitemp.png'
	#define file location on comp
	filename =
	global img 
	img = Image.open(filename)
	photo = ImageTk.PhotoImage(img)
	label1 = Label(image = photo)
	label1.image = photo
	label1.pack(anchor = S)

def takeinput4():
	#filename= 'C:/Users/Meeta Malviya/AppData/Local/Programs/Python/Python37-32/geminitemp.png'
	#define file location on comp
	filename =
	global img 
	img = Image.open(filename)
	photo = ImageTk.PhotoImage(img)
	label1 = Label(image = photo)
	label1.image = photo
	label1.pack(anchor = S)

def run1():
    t = threading.Thread(target = statusbar,args = ())
    t.start()
    while t.is_alive():
        import mainprgm
        results = mainprgm.main(np.array(img))
        break


menu = Menu(root)
root.config(menu = menu)
imgcon = Menu(menu)
subpre = Menu(menu)
menu.add_command(label='Home',command=hello)

menu.add_cascade(label='Images',menu=imgcon)
imgcon.add_command(label='Gemini',command =takeinput1)

imgcon.add_command(label='Cassiopia',command = takeinput2)
imgcon.add_command(label='Orion',command = takeinput3)
imgcon.add_command(label='Ursa Major',command = takeinput4)

menu.add_command(label='Run',command = run1)
menu.add_command(label='Code',command = openweb1)
menu.add_command(label='Documentation',command = openweb2)

menu.add_cascade(label='Presentation',menu =subpre)
subpre.add_command(label='ppt',command=hello)
subpre.add_command(label='vedio',command=hello)



root.mainloop()
