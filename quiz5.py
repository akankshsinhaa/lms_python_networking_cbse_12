import csv
print("\n")
print('%50s' % "MULTIPLE CHOICE QUESTIONS")
print("\n")
mrks=0
print("Q1- Network congestion occurs") 
print("A. in case of traffic overloading")
print("B. when a system terminates")
print("C. when connection between two nodes terminates")
print("D. none of the mentioned") 
ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="A"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")
    #print("Correct answer is: " ,)

    
print("\n")
print("Q2- What is the meaning of Bandwidth in Network?")
print("A. Transmission capacity of a communication channels")
print("B. Connected Computers in the Network")
print("C. Class of IP used in Network")
print("D. None of Above")

ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="A"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")

    
print("\n")
print("Q3. Which of the following is correct regarding Class B Address of IP address")
print("A.. Network bit – 14, Host bit – 16")
print("B. Network bit – 16, Host bit – 14")
print("C. Network bit – 18, Host bit – 16")
print("D. Network bit – 12, Host bit – 14")

ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="A"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")
    

print("\n")    
print("Q4. ____ provides a connection-oriented reliable service for sending messages")
print(" A. A. TCP")
print("B. IP")
print("C. UDP")
print("D. All of the above")

ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="A"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")


print("\n")    
print("Q5. What does Router do in a network?")
print("A. Forwards a packet to all outgoing links")
print("B. Forwards a packet to the next free outgoing link")
print("C. Determines on which outing link a packet is to be forwarded")
print("D. Forwards a packet to all outgoing links except the originated ")

ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="C"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")



print("\n") 
print("Q6. What is the use of Ping command?")
print("A. To test a device on the network is reachable")
print("B. To test a hard disk fault")
print("C. To test a bug in a Application")
print("D. To test a Pinter Quality")

ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="A"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")


print("\n")    
print("Q7. What is the size of Host bits in Class B of IP address?")
print("A.  04")
print("B. 08")
print("C. 16")
print("D. 32")


ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="C"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")


print("\n")   
print("Q8.Which of the following is correct in CIDR?")
print("A. . Class A includes Class B network")
print("B. There are only two networks")
print("C. There are high & low class network")
print("D. There is no concept of class A, B, C networks")

ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="D"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")


print("\n")    
print("Q9. The processes on each machine that communicate at a given layer are called")
print("A. UDP process")
print("B. Intranet process")
print("C. Server technology")
print("D. Peer-peer process")

ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="D"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")


print("\n")    
print("Q10. Which of the following layer is not network support layer?")
print("A. Transport Layer")
print("B. Network Layers")
print("C. Data link Layer")
print("D. Physical Layer")
 
ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    
    ans = input()
if (ans.upper()=="A"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")

    
print("\n")
print("-------------------------------------------------------------------------")
print("\n")
print('%50s' %"FILL IN THE BLANKS")
print("\n")
quiz_dict={"11. The language used to develop web pages is called ___":"HTMP","12. The DNS for commercial businesses is ___":".com","13.  The _____ describes the machines location in a name space from right to left":"Domain name system","14.  The software which helps to view the websites is called____":"Web browser","15.  A ____ is a computer that performs actions for another computer.":"server"}
for i in quiz_dict:
    print(i)
    ans1=input("Enter your answer")
    if (ans1.lower()==quiz_dict[i].lower()):
        mrks=mrks+1
        print("Your answer is correct")
    else:
        print("Wrong answer")
        print("The correct answer is:",quiz_dict[i])

print("\n") 
print("-------------------------------------------------------------------------")



print("\n")
print('%50s' %"TRUE OR FALSE")
print("\n")
tf_dict={"16. A virus may get into your computer, only by copying an infected file into your computer.":"T","17. A tag is always in between “<” and “>” symbols.":"T","18.  DNS stands for domain name system.":"T","19. CGI stands for common gateway interaction. ":"F","20. IP addresses are addresses which are numbers by which a computer can be located in the internet.":"T"}
for i in tf_dict:
    print(i)
    ans=input("Enter your answer (T/F)")
    if (ans.upper()==tf_dict[i].upper()):
        mrks=mrks+1
        print("Your answer is correct")
    else:
        print("Wrong answer")
        print("The correct answer is:",tf_dict[i])




print("-------------------------------------------------------------------------")

print("\n")
print("You answered " , mrks, " of 20 questions correctly.")
print("Your score is", (mrks/20)*100, "%")

f = open("currentuser.txt","r")
global file
file = f.read()
file+=".csv"
f.close()

with open(str(file), mode='r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        try:
            row[4]=(mrks/20)*100
            with open(str(file), mode='w') as us:
                us = csv.writer(us, delimiter=',')
                us.writerow(row)
        except:
            continue










    








