import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector
import os


def a():
    root = tk.Tk()

    root.minsize(750,500)
    root.title("Test")
    
    def onClick2():
        a = Board.get()
        if a == "1":
            os.startfile('quiz1.py')
        elif a=="2":
            os.startfile('quiz2.py')
        elif a=="3":
            os.startfile('quiz3.py')
        elif a=="4":
            os.startfile('quiz4.py')
        elif a=="5":
            os.startfile('quiz5.py')

    Board=Combobox(root,height=5,width=15,values=["1","2","3","4","5"])
    Board.place(x=325, y= 240)

    b2 = tk.Button(root, text = "Test",command = onClick2).place(x=325,y=270)
