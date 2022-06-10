import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector
import func


mydb = mysql.connector.connect(host="localhost",user="root",password="dps123",database='test')

mycursor = mydb.cursor()

def a():
    root = tk.Tk()

    root.minsize(750,500)
    root.title("Check Database")
    l2 = tk.Label(root, text = "Admin")
    l2.pack()
    b1 = tk.Button(root,text="Display All",command = func.allr).place(x = 100,y=100)
    b2 = tk.Button(root,text="Display Average Marks",command = func.avg).place(x = 100,y=130)
    b3 = tk.Button(root,text="Display Maximum Marks",command = func.mx).place(x = 100,y=160)
    b6 = tk.Button(root,text="Display Minimum Marks",command = func.mn).place(x = 100,y=190)
    b4 = tk.Button(root,text="Count Records",command = func.cnt).place(x = 100,y=220)
    
    l2 = tk.Label(root, text = "Sort").place(x=100,y=260)

    var = IntVar()
    R1 = Radiobutton(root, text="Ascending",variable=var, value=1,command=func.asc).place(x=120,y=290)
    R2 = Radiobutton(root, text="Descending",variable=var, value=2,command=func.desc).place(x=120,y=310)
    R3 = Radiobutton(root, text="Above (Input)",variable=var, value=1,command=func.abv).place(x=120,y=330)
    R4 = Radiobutton(root, text="Below (Input)",variable=var, value=2,command=func.blw).place(x=120,y=350)

#CheckVar1 = IntVar()

#CheckVar2 = IntVar()

#C1 = Checkbutton(root, text = "Less Than", variable = CheckVar1,onvalue = 1, offvalue = 0)
#C2 = Checkbutton(root, text = "Greater Than", variable = CheckVar2, onvalue = 1, offvalue = 0)
#C1.place(x = 120,y=340)
#C2.place(x = 120,y =360)

#b5 = tk.Button(root,text="Group By Marks",command = groupby).place(x = 100,y=380)
    root.mainloop()
