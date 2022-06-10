import matplotlib.pyplot as plt
import mysql.connector
import csv
import file7
file7.a()
def a ():
    try:
        
        x = [1,2,3,4,5]
        f = open("currentuser.txt","r")
        global file
        file1 = f.read()
        file =file1+".csv"
        f.close()

        with open(str(file), mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                plt.plot(x,row)
                plt.xlabel("Test Number")
                plt.ylabel("Marks")
                plt.show()
        
       
    except:
        print()
    
