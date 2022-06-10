import csv
print("\n")
print('%50s' % "MULTIPLE CHOICE QUESTIONS")
print("\n")
mrks=0
print("Q1- What is the address size of IPv6?") 
print("A. 32 bit")
print("B. 64 bit")
print("C. 128 bit")
print("D. 256 bit") 
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
print("Q2- What is the size of Network bits & Host bits of Class A of IP address?")
print("A. Network bits 7, Host bits 24")
print("B. Network bits 8, Host bits 24")
print("C. Network bits 7, Host bits 23")
print("D. Network bits 8, Host bits 23")

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
print("Q3. What is the full form of RAID?")
print("A. Redundant Array of Independent Disks")
print("B. Redundant Array of Important Disks")
print("C. Random Access of Independent Disks")
print("D. Random Access of Important Disks")
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
print("Q4. What do you mean by broadcasting in Networking?")
print(" A. It means addressing a packet to all machine")
print(" B. It means addressing a packet to some machine")
print(" C. It means addressing a packet to a particular machine")
print(" D. It means addressing a packet to except a particular machine")

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
print("Q5. What is the size of Source and Destination IP address in IP header?")
print("A. 4 bits")
print("B. 8 bits")
print("C. 16 bits")
print("D. 32 bits")

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
print("Q6. What is the typical range of Ephemeral ports?")
print("A. 1 to 80")
print("B. 1 to 1024")
print("C. 80 to 8080")
print("D. 1024 to 65535")

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
print("Q7. A set of rules that govern all aspects of information communication is called")
print("A. Server")
print("B. Internet")
print("C. Protocol")
print("D. OSI Model")
 
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
print("Q8. Controlling access to a network by analyzing the incoming and outgoing packets is called")
print("A. IP Filtering")
print("B. Data Filtering")
print("C. Packet Filtering")
print("D. Firewall Filtering")
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
print("Q9. DHCP is the abbreviation of")
print("A. Dynamic Host Control Protocol")
print("B. Dynamic Host Configuration Protocol")
print("C. Dynamic Hyper Control Protocol")
print("D. Dynamic Hyper Configuration Protocol")

ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="B"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")


print("\n")    
print("Q10. What is the use of Bridge in Network?")
print("A. to connect LANs")
print("B. to separate LANs")
print("C. to control Network Speed")
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
print("-------------------------------------------------------------------------")
print("\n")
print('%50s' %"FILL IN THE BLANKS")
print("\n")
quiz_dict={"11. All computers connected to the internet and wanting to use it for sending/receiving data must follow a common set of rules for communication called ____":"Protocol","12. ____ protocol tells each system how to form mail messages and transfer them between computers.":"SMTP","13. Internet began in ___":"1969","14. IEEE 802.3 is otherwise known as -------------.":"Ethernet","15. The domain name for miscellaneous organizations is ___.":".org"}
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
tf_dict={"16.  In a multipoint network addition of new computers to the network is difficult.":"F","17.  E mail stands for electronic mail.":"T","18. In a ring topology nodes are arranged in ring pattern.":"T","19.  There is only one search engine in internet.":"F","20. A very popular LAN is Ethernet.":"T"}
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
            row[3]=(mrks/20)*100
            with open(str(file), mode='w') as us:
                us = csv.writer(us, delimiter=',')
                us.writerow(row)
        except:
            continue










    








