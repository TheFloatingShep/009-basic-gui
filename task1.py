#!python3
"""
Create the interface shown in the file task1.png
You will need to add a function called "multiply"
When the "=" button is clicked, multiply will read 
the contents of the first 2 entry boxes. It will
find the product and display the answer in the
3rd entry box
"""
import tkinter as tk

def do():
    x = entry1.get()
    y = entry2.get()
    entry3["text"] = int(x) * int(y)

main = tk.Tk()

entry1 = tk.Entry(width = 25)
label1 = tk.Label(text = "x")
entry2 = tk.Entry(width = 25)
button1 = tk.Button(text = "=", command = do)
entry3 = tk.Label(width = 40)

entry1.pack(side = "left")
label1.pack(side = "left")
entry2.pack(side = "left")
button1.pack(side = "left")
entry3.pack(side = "left")

main.mainloop()