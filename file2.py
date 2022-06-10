import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector
import csv
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dps123",
  database="test"
)

mycursor = mydb.cursor()


root = tk.Tk()
root.minsize(750,500)
root.title("Login")

def log(a):
    if a == True:
        root.destroy()
        
        f = open("currentuser.txt","w")
        f.write(str(result[2]))
        
        f = open("currentuser.txt","r")
        global file
        file = f.read()
        file+=".csv"
        f.close()

        if os.path.isfile(str(file)):
            import file3
        else:

            with open(str(file), mode='w') as us:
                us = csv.writer(us, delimiter=',')

                us.writerow([0,0,0,0,0])
            import file3
    elif a == False:
        tk.messagebox.showerror("Error","Wrong Email and Password Combination")
        b = True

def c(x):
    if x== False:
        tk.messagebox.showerror("Error","Credentials Do Not Match")
        x = True

def onClick():
    em, pas = t1.get(),t2.get()
    mycursor.execute("SELECT * FROM log1")
    myresult = mycursor.fetchall()
    lenmy = len(myresult)

    for i in myresult:
        if i[2]==em:
            if i[1]==pas:
                logged = True
                global result
                result = i
                log(logged)
            else:
                logged = False
                log(logged)
        else:
            logged = False
            b=False
   







l1 = tk.Label(root, text = "Email")
l1.pack()

t1 = Entry(root, width = 45)
t1.pack()

l2 = tk.Label(root, text = "Password")
l2.pack()

t2 = Entry(root,show="*", width = 45)
t2.pack()

b1 = tk.Button(root, text = "Login",command = onClick).place(x=350,y=200)



b1 = tk.Button(root, text = "Login",command = onClick).place(x=350,y=200)
