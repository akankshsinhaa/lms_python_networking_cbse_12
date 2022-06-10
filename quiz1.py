import csv
print("\n")
print('%50s' % "MULTIPLE CHOICE QUESTIONS")
print("\n")
mrks=0
print("Q1- Computer Network is") 
print("A. Collection of hardware components and computers")
print("B. Interconnected by communication channels")
print("C. Sharing of resources and information")
print("D. All of the Above") 
ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="D"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")
    #print("Correct answer is: " ,)

    
print("\n")
print("Q2- Protocols are?")
print("A. Agreements on how communication components and DTE's are to communicate")
print("B. Logical communication channels for transferring data")
print("C. Physical communication channels sued for transferring data")
print("D. None of above")

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
print("Q3. Two devices are in network if")
print("A. a process in one device is able to exchange information with a process in another device")
print("B. a process is running on both devices")
print("C. PIDs of the processes running of different devices are same")
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
    

print("\n")    
print("Q4. what is a Firewall in Computer Network?")
print(" A. The physical boundary of Network")
print(" B. An operating System of Computer Network")
print(" C. A system designed to prevent unauthorized access")
print(" D. A web browsing Software")

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
print("Q5. The IETF standards documents are called")
print("A. RFC")
print("B. RCF")
print("C. ID")
print("D. None of the mentioned")


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
print("Q6. Which data communication method is used to transmit the data over a serial communication link?")
print("A. Simplex")
print("B. Half-duplex")
print("C. Full duplex")
print("D. All of above")

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
print("Q7. Each IP packet must contain")
print("A. Only Source address")
print("B. Only Destination address")
print("C. Source and Destination address")
print("D. Source or Destination address")
 
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
print("Q8. What is the minimum header size of an IP packet?")
print("A. 16 bytes")
print("B. 10 bytes")
print("C. 20 bytes")
print("D. 32 bytes")
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
print("Q9. Routing tables of a router keeps track of")
print("A. MAC Address Assignments")
print("B. Port Assignments to network devices")
print("C. Distribute IP address to network devices")
print("D. Routes to use for forwarding data to its destination")

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
print("Q10. Which of the following is not the External Security Threats?")
print("A. Front-door Threats")
print("B. Back-door Threats")
print("C. Underground Threats")
print("D. Denial of Service (DoS)")
 
ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    
    ans = input()
if (ans.upper()=="c"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")

    
print("\n")
print("-------------------------------------------------------------------------")
print("\n")
print('%50s' %"FILL IN THE BLANKS")
print("\n")
quiz_dict={"11. PPP stands for ____":"Point to point protocol","12. A computer network that spans a relatively large geographical area is called ___":"WAN","13. ISP denotes ___":"Internet Service Provider","14. TCP/IP stands for ___":"Transmission control protocol/Internet protocol","15. The unique address of web page on the web is called ____":"URL"}
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
tf_dict={"16. HTTP is hyper text transfer protocol.":"T","17. WWW came into exist in 1980.":"F","18.  FTP is used for transferring files between networks.":"F","19. IP address is a sequence of four digit numbers separated by comma.":"F","20. A  LAN is connected to large geographical area.":"F"}
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
            row[0]=(mrks/20)*100
            with open(str(file), mode='w') as us:
                us = csv.writer(us, delimiter=',')
                us.writerow(row)
        except:
            continue



    








