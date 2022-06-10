import csv
print("\n")
print('%50s' % "MULTIPLE CHOICE QUESTIONS")
print("\n")
mrks=0
print("Q1- Router operates in which layer of OSI Reference Model?") 
print("A. Layer 1 (Physical Layer)")
print("B. Layer 3 (Network Layer)")
print("C. Layer 4 (Transport Layer)")
print("D. Layer 7 (Application Layer)") 
ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="B"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")
    #print("Correct answer is: " ,)

    
print("\n")
print("Q2- ADSL is the abbreviation of")
print("A. Asymmetric Dual Subscriber Line")
print("B. Asymmetric Digital System Line")
print("C. Asymmetric Dual System Line")
print("D. Asymmetric Digital Subscriber Line")

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
print("Q3. How many layers does OSI Reference Model has?")
print("A. 4")
print("B. 5")
print("C. 6")
print("D. 7")
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
print("Q4. Bridge works in which layer of the OSI model?")
print(" A. Application layer")
print(" B. Transport layer")
print(" C. Network layer")
print(" D. Datalink layer")

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
print("Q5. Why IP Protocol is considered as unreliable?")
print("A. A packet may be lost")
print("B. Packets may arrive out of order")
print("C. Duplicate packets may be generated")
print("D. All of the above")


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
print("Q6. What is the benefit of the Networking?")
print("A. File Sharing")
print("B. Easier access to Resources")
print("C. Easier Backups")
print("D. All of the above")

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
print("Q7. Which of the following is not the Networking Devices?")
print("A. Gateways")
print("B. Linux")
print("C. Routers")
print("D. Firewalls")
 
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
print("Q8. What is the maximum header size of an IP packet?")
print("A. 32 bytes")
print("B. 64 bytes")
print("C. 30 bytes")
print("D. 60 bytes")
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
print("Q9. Which of the following is correct in VLSM?")
print("A. Can have subnets of different sizes")
print("B. Subnets must be in same size")
print("C. No required of subnet")
print("D. All of above")

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
print("Q10. DHCP Server provides _____ to the client.")
print("A. Protocol")
print("B. IP Address")
print("C. MAC Address")
print("D. Network Address")
 
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
print("-------------------------------------------------------------------------")
print("\n")
print('%50s' %"FILL IN THE BLANKS")
print("\n")
quiz_dict={"11. VPN stands for ____":"Virtual private network","12. The domain name for educational institutions is ___":".edu","13. DNS denotes ___":"Domain name server","14. The DNS for commercial businesses is ___":".com","15. ____ comprises multiple LANs.":"WAN"}
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
tf_dict={"16.  Descriptive and locative are two types of domain names.":"T","17. BSNL also provides ISP in India.":"F","18. ASCII stands for American Standard Code For Interchange Information.":"F","19.  A computer is identified by 64 bit IP address":"F","20. The domain name .com stands for computational purpose.":"F"}
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
            row[2]=(mrks/20)*100
            with open(str(file), mode='w') as us:
                us = csv.writer(us, delimiter=',')
                us.writerow(row)
        except:
            continue









    








