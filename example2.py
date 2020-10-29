#!python3
"""
We start by importing a module, and also import all of the important
code from that module. I'm not sure why they do it this way, but 
that's the way it is.
"""
import tkinter as tk 
from tkinter import *
# the ttk command is required to get extra widgets, including the combobox
from tkinter import ttk


"""
We create an object using some of the built in functions from the
tkinter Tk class. We also use some of the object methods to set
some of the properties of the window.
"""
window = tk.Tk()
window.title("Packing Widgets example")
# Note, in this example, we removed the geometry to set the window size
# because packing the widgets tries to make the window as small as possible

"""
A window actually has an infinite running while loop while
it checks to see if any of the features of the window (buttons,
text entry, etc) are being mainpulated.  These features are also
called WIDGETS, and we'll see how they can be added in the next few
files.
"""

label1 = tk.Label(window,text="Text that does\nnothing is a label")
label1.pack()

dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto)
label2.pack()

lable3 = tk.Label(window, text="Note that an image can be in a label or a button!")
lable3.pack()

button1 = tk.Button(window,text="A button\nis clickable", padx=3, pady=2, relief=GROOVE)
button1.pack()

entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry1.pack()

combo = ttk.Combobox(window,values=["1","2","3"])
combo.config()
combo.pack()

check1 = tk.Checkbutton(window)
check1.pack()


"""
Note some of the difficulty in trying to arrange your widgets1
If you want some good control over your widgets, we need to use the
geometry manager to place them into a grid or using the coordinates
(example3.py and exampl4.py
"""

window.mainloop()