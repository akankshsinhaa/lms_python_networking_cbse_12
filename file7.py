import csv
import mysql.connector

def a():
    f = open("currentuser.txt","r")
    global file
    file1 = f.read()
    file =file1+".csv"
    f.close()
    mydb = mysql.connector.connect(host="localhost",user="root",password="dps123",database='test')

    mycursor = mydb.cursor()
    avg = 0.0

    with open(str(file), mode='r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
    
            for i in row:
                avg+=float(i)*0.2

            avg = int(avg)
            sql = "UPDATE log1 SET marks = %d WHERE mail = '%s'" % (avg,file1)
            mycursor.execute(sql)
            mydb.commit()

