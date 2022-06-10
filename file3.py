import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector
import os
import file4

import file5
root = tk.Tk()

root.minsize(750,500)
root.title("Main")

def onClick1():
    file4.a()
    


def onClick2():
    import file6
    file6.a()

def onClick3():
    
    file5.a()

def onClick4():
    import file7
    file7.a()
    os.remove("currentuser.txt")
    root.destroy()
    


b1 = tk.Button(root, text = "Study",command = onClick1).place(x=150,y=100)

b2 = tk.Button(root, text = "Test",command = onClick2).place(x=150,y=200)

b3 = tk.Button(root, text = "See Progress",command = onClick3).place(x=150,y=300)

b4 = tk.Button(root, text = "Logout And Exit",command = onClick4).place(x=600,y=400)
