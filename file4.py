import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector
import os

def a ():
    root4 = tk.Tk()
    root4.minsize(750,500)
    root4.title("Study")

    def onclick():
        a = Board.get()
        if a == "Introduction":
            os.startfile("1-introduction.pdf")

        elif a=="Transmission Medium":
            os.startfile("2-transmission medium.pdf")
        
        elif a == "Types of Network":
            os.startfile("3-types of network.pdf")
        
        elif a == "Networking Topologies":
            os.startfile("4-networking topologies.pdf")
        
        elif a == "Networking Devices":
            os.startfile("5-networking devices.pdf")
        
        elif a == "Switching Techniques":
            os.startfile("6-switching techniques.pdf")
        
        elif a == "Data Transmission Terminology":
            os.startfile("7-Data Transmission Terminology.pdf")
        
        elif a == "Introduction to Networking Protocols":
            os.startfile("8-networking protocols(intro).pdf")
        
        elif a == "Networking Protocols":
            os.startfile("9-networking protocols.pdf")
        
        elif a == "Wireless Mobile Communication Protocols":
            os.startfile("10-Wireless Mobile Communication Protocols.pdf")    
        
        elif a == "Mobile Communication Technology":
            os.startfile("11-Mobile Communication Technology.pdf")
        
        elif a == "Remote Login":
            os.startfile("12-remote login.pdf")
        
        elif a == "Network Security":
            os.startfile("13-network security.pdf")   
        
        elif a == "Cookies, Firewall and India IT Act":
            os.startfile("14-cookies,firewall,india it act.pdf")
        
        elif a == "Cyber Crime":
            os.startfile("15-cyber crime.pdf")
        
        elif a == "Some Definitions":
            os.startfile("16-some definitions.pdf")
        
        elif a == "E-commerce":
            os.startfile("17-ecommerce.pdf")
        
        elif a == "Cloud Computing and iOT":
            os.startfile("18-cloud computing and iot.pdf")

 
    Board=Combobox(root4,height=5,width=15,values=["Introduction","Transmission Medium","Types of Network","Networking Topologies","Networking Devices","Switching Techniques","Data Transmission Terminology","Introduction to Networking Protocols","Networking Protocols","Wireless Mobile Communication Protocols","Mobile Communication Technology","Remote Login","Network Security","Cookies, Firewall and India IT Act","Cyber Crime","Some Definitions","E-commerce","Cloud Computing and iOT"])
    Board.place(x=325,y=240)
    
    search=Button(root4,text="Study",command=onclick).place(x=325,y=270)
    

