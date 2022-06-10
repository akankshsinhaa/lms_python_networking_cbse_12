import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector


mydb = mysql.connector.connect(host="localhost",user="root",password="dps123",database='test')

mycursor = mydb.cursor()

root = tk.Tk()

#mycursor.execute("alter table log1 alter marks set default 0")
#mydb.commit()


    
def onClick():
    name, passw, mail, phone = t1.get(),t2.get(),t3.get(),int(t4.get())
    sql = """INSERT INTO log1 (username, password, mail, phone) VALUES ('%s', '%s', '%s', %d)""" % (name, passw, mail, phone)
    #sql2 = "alter table log1 add marks int"
    mycursor.execute(sql)
    #mycursor.execute(sql2)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    OnClick2()



def OnClick2():
    root.destroy()
    import file2
    



root.minsize(750,500)
root.title("Sign Up")

l1 = tk.Label(root, text = "Name")
l1.pack()

t1 = Entry(root, width = 45)
t1.pack()

l2 = tk.Label(root, text = "Password")
l2.pack()

t2 = Entry(root,show="*", width = 45)
t2.pack()

l3 = tk.Label(root, text = "Email")
l3.pack()

t3 = Entry(root, width = 45)
t3.pack()

l4 = tk.Label(root, text = "Phone Number")
l4.pack()

t4 = Entry(root, width = 45)
t4.pack()

b1 = tk.Button(root, text = "Sign Up",command = onClick).place(x=350,y=200)

l5 = tk.Label(root, text = "Already A User?").place(x=630,y=430)

b2 = tk.Button(root, text = "Login",command=OnClick2).place(x=650,y=450)



root.mainloop()





