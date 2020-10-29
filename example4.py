#!python3
"""
We start by importing a module, and also import all of the important
code from that module. I'm not sure why they do it this way, but 
that's the way it is.
"""
import tkinter as tk 
from tkinter import *


"""
We create an object using some of the built in functions from the
tkinter Tk class. We also use some of the object methods to set
some of the properties of the window.
"""
window = tk.Tk()
window.title("Hi!")
window.geometry("200x400")

"""
A window actually has an infinite running while loop while
it checks to see if any of the features of the window (buttons,
text entry, etc) are being mainpulated.  These features are also
called WIDGETS, and we'll see how they can be added in the next few
files.
"""
window.mainloop()