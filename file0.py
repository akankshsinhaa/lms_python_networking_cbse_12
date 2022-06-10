import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

root = tk.Tk()

root.minsize(750,500)
root.title("Welcome")

def onClick():
    root.destroy()
    import file

def sel():
   onClick()

def sel2():
    root.destroy()
    import file00

l1 = tk.Label(root, text = "Welcome").place(x=325,y=240)

#b1 = tk.Button(root, text = "Next",command = onClick).place(x=325,y=270)






var = IntVar()
R1 = Radiobutton(root, text="Student", variable=var, value=1,
                  command=sel).place(x=325,y=270)

R2 = Radiobutton(root, text="Admin", variable=var, value=2,
                  command=sel2).place(x=325,y=300)


root.mainloop()
