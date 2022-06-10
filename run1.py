import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="dps123",database='test')

mycursor = mydb.cursor()

mycursor.execute("create table log1 (username char(15), password char(20), mail  varchar(25), phone  int(10), marks int(10))")

mycursor.execute("alter table log1 alter marks set default 0")

mycursor.execute("create table log2 (username char(15), password char(20), mail  varchar(25), phone  int(10))")

mycursor.execute("""insert into log2 (username,password,mail,phone) values ("simran","simran","simran",8783142)""")

mycursor.execute("""insert into log2 (username,password,mail,phone) values ("akanksh","akanksh","akanksh",0234562)""")

mycursor.execute("""insert into log2 (username,password,mail,phone) values ("steve","steve","steve",092453741)""")


mycursor.execute("""insert into log2 (username,password,mail,phone) values ("pushan","pushan","pushan",529782)""")


mydb.commit()
