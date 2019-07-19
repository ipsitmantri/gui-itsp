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

'''
resource = url.urlopen("")
output = open('file1.jpg','wb')
output.write(resource.read())
output.close()'''
#filename = askopenfilename()
root = Tk()
root.geometry("650x700")
root.title('Run Query')
v = IntVar()
def openchecklist():
    button1.pack_forget()
    radiobutton1.pack(anchor = S)
    radiobutton2.pack(anchor = S)
    button2.pack(anchor = S)

def takeinput():
    x = v.get()
    button2.pack_forget()
    if x == 1:
        radiobutton2.pack_forget()
        #global filename
        filename = askopenfilename()
        radiobutton1.pack_forget()
        label = Label(root,text = 'File: ' + filename)
        label.pack(anchor = NW)
        global img
        img = Image.open(filename)
        photo = ImageTk.PhotoImage(img)
        label1 = Label(image = photo)
        label1.image = photo
        label1.pack(anchor = S)
        button3.pack()

    if x == 2:
        radiobutton1.pack_forget()
        global entry1
        entry1 = Entry(root)
        entry1.bind('<Return>',sendinput)
        entry1.pack()

def sendinput(event):
    entry1.pack_forget()
    resource = url.urlopen(entry1.get())
    output = open('fileio.jpg','wb')
    output.write(resource.read())
    output.close()
    global img
    img = Image.open('fileio.jpg')
    photo = ImageTk.PhotoImage(img)
    label3 = Label(image = photo)
    label3.image = photo
    label3.pack()
    button3.pack()

def statusbar():
    status = Label(root,text = 'Running your query...',bd = 1,relief = SUNKEN, anchor = W)
    status.pack(side = BOTTOM, fill = X)
    time.sleep(2)
    status.pack_forget()

def run():
    button3.pack_forget()
    t = threading.Thread(target = statusbar,args = ())
    t.start()
    while t.is_alive():
        import mainprgm
        results = mainprgm.main(np.array(img))
        break

button1 = Button(root,text = 'Select Input Type',command = openchecklist)
button1.pack()
button2 = Button(root,text = 'Next',command = takeinput)
radiobutton1 = Radiobutton(root,text = 'File',variable = v,value = 1)
radiobutton2 = Radiobutton(root,text = 'URL',variable = v,value = 2)
button3 = Button(root,text = 'Run',command = run)

































root.mainloop()
