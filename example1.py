#!python3

import tkinter as tk 
from tkinter import *



def getEntry():
    myEntry = entry.get()
    print(myEntry)
    labeldata.set(myEntry)
    return myEntry

window = tk.Tk()
window.title("Hi!")
window.geometry("200x400")

labeldata = StringVar()
labeldata.set("hahahaha")

label1 = tk.Label(textvariable = labeldata)
label1.grid(row=1,column=1)

button = tk.Button(text="testing", command=getEntry)
button.grid(row=2,column = 1)

entry = tk.Entry()
entry.grid(row=3,column = 2)

window.mainloop()