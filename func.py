import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="dps123",
database='test'
)


mycursor = mydb.cursor()

mycursor.execute("alter table log1 modify column password char(20)")
mydb.commit()


def allr():
    try:
        print("")
        print('%35s' % "RECORDS OF ALL STUDENTS")
        print("")
        mycursor.execute("select * from log1")
        print("-"*75)
        F="%10s %13s %5s %30s %9s"
        print(F % ("username","password","mail","phone","marks"))
        print("-"*75)
        a=mycursor.fetchall()
        for row in a:
          username=row[0]
          pas=row[1]
          em=row[2]
          ph=row[3]
          marks=row[4]
          print("{0:<15} {1:<10}{2:<30}{3:<10}{4:<10}".\
                format(username,pas,em,ph,marks))
        print("-"*75)
    except:
        print()



def asc():
    try:
        print("")
        print('%45s' % "MARKS OF ALL STUDENTS IN ASCENDING ORDER")
        print("")
        mycursor.execute("select * from log1 order by marks")
        print("-"*75)
        F="%10s %13s %5s %30s %9s"
        print(F % ("username","password","mail","phone","marks"))
        print("-"*75)
        b=mycursor.fetchall()
        for row in b:
          username=row[0]
          pas=row[1]
          em=row[2]
          ph=row[3]
          marks=row[4]
          print("{0:<15}{1:<10}{2:<30}{3:<10}{4:<10}".\
                format(username,pas,em,ph,marks))
        print("-"*75)
    except:
        print()
        


def desc():
    try:
        print("")
        print('%45s' % "MARKS OF ALL STUDENTS IN DESCENDING ORDER")
        print("")
        mycursor.execute("select * from log1 order by marks desc ")
        print("-"*75)
        F="%10s %13s %5s %30s %9s"
        print(F % ("username","password","mail","phone","marks"))
        print("-"*75)
        b=mycursor.fetchall()
        for row in b:
          username=row[0]
          pas=row[1]
          em=row[2]
          ph=row[3]
          marks=row[4]
          print("{0:<15}{1:<10}{2:<30}{3:<10}{4:<10}".\
                format(username,pas,em,ph,marks))
        print("-"*75)
    except:
        print()





def cnt():
    print("")
    print('%45s' % "NUMBER OF STUDENTS LOGGED IN TO THE WEBSITE")
    print("")
    mycursor.execute("select COUNT(username) from log1  ")
    b=mycursor.fetchall()
    for row in b:
      username=row[0]
      print("{0:^40} ".\
            format(username))



def avg():
    print("")
    print('%35s' % "AVERAGE MARKS OF ALL STUDENTS")
    print("")
    mycursor.execute("select AVG(marks) from log1")
    b=mycursor.fetchall()
    for row in b:
      marks=row[0]
      print("{0:^40}".\
            format(marks))




def mx():
    print("")
    print('%30s' % "MAXIMUM MARKS")
    print("")
    mycursor.execute("select MAX(marks) from log1 ")
    b=mycursor.fetchall()
    for row in b:
      marks=row[0]
      print("{0:^50}".\
            format(marks))


def mn():
    print("")
    print('%30s' % "MINIMUM MARKS")
    print("")
    mycursor.execute("select MIN(marks) from log1 ")
    b=mycursor.fetchall()
    for row in b:
      marks=row[0]
      print("{0:^50}".\
            format(marks))



def abv():
    above=int(input("Enter marks"))
    print("")
    print('%35s' % "STUDENTS WHO SCORED ABOVE", above)
    print("")
    mycursor.execute("select * from log1 where marks>%d"%above)
    print("-"*75)
    F="%10s %13s %5s %30s %9s"
    print(F % ("username","password","mail","phone","marks"))
    print("-"*75)
    b=mycursor.fetchall()
    for row in b:
      username=row[0]
      pas=row[1]
      em=row[2]
      ph=row[3]
      marks=row[4]
      print("{0:<15} {1:<10}{2:<30}{3:<10}{4:<10}".\
            format(username,pas,em,ph,marks))
    print("-"*75)


def blw():
    below=int(input("Enter marks"))
    print("")
    print('%35s' % "STUDENTS WHO SCORED BELOW", below)
    print("")
    print("-"*75)
    mycursor.execute("select * from log1 where marks<%d"%below)
    F="%10s %13s %5s %30s %9s"
    print(F % ("username","password","mail","phone","marks"))
    print("-"*75)
    b=mycursor.fetchall()
    for row in b:
      username=row[0]
      pas=row[1]
      em=row[2]
      ph=row[3]
      marks=row[4]
      print("{0:<15} {1:<10}{2:<30}{3:<10}{4:<10}".\
            format(username,pas,em,ph,marks))
    print("-"*75)
