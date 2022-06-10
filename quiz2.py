import csv
print("\n")
print('%50s' % "MULTIPLE CHOICE QUESTIONS")
print("\n")
mrks=0
print("Q1- What is the IP Address range of APIPA?") 
print("A. 169.254.0.1 to 169.254.0.254")
print("B. 169.254.0.1 to 169.254.0.255")
print("C. 169.254.0.1 to 169.254.255.254")
print("D. 169.254.0.1 to 169.254.255.255") 
ans=input("Please enter the option number of your answer:")
while ans.isdigit():
    print("Invalid input. Please enter a valid option.")
    ans = input()
if (ans.upper()=="C"):
    mrks=mrks+1
    print("Your answer is correct.")
else:
    print("Your answer is wrong.")
    #print("Correct answer is: " ,)

    
print("\n")
print("Q2- Which of the following is not the possible ways of data exchange?")
print("A. Simplex")
print("B. Multiplex")
print("C. Half-duplex")
print("D. Full-duplex")

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
print("Q3. The management of data flow between computers or devices or between nodes in a network is called")
print("A. Flow control")
print("B. Data Control")
print("C. Data Management")
print("D. Flow Management")
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
print("Q4. What does the port number in a TCP connection specify?")
print(" A. It specifies the communication process on the two end systems")
print(" B. It specifies the quality of the data & connection")
print(" C. It specify the size of data")
print(" D. All of the above")

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
print("Q5. What is the purpose of the PSH flag in the TCP header?")
print("A. Typically used to indicate end of message")
print("B. Typically used to indicate beginning of message")
print("C. Typically used to push the message")
print("D. Typically used to indicate stop the message")


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
print("Q6. Which of the following protocol is/are defined in Transport layer?")
print("A. FTP")
print("B. TCP")
print("C. UDP")
print("D. option B & C")

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
print("Q7. The meaning of Straight-through Cable is")
print("A. Four wire pairs connect to the same pin on each end")
print("B. The cable Which Directly connects Computer to Computer")
print("C. Four wire pairs not twisted with each other")
print("D. The cable which is not twisted")
 
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
print("Q8. What is the size of MAC Address?")
print("A. 16-bytes")
print("B. 32-bytes")
print("C. 48-bytes")
print("D. 64-bytes")
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
print("Q9. Repeater operates in which layer of the OSI model?")
print("A. Physical layer")
print("B. Data link layer")
print("C. Network layer")
print("D. Transport layer")

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
print("Q10. Which of the following layer of OSI model also called end-to-end layer?")
print("A. Presentation layer")
print("B. Network layer")
print("C. Session layer")
print("D. Transport layer")
 
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
print("-------------------------------------------------------------------------")
print("\n")
print('%50s' %"FILL IN THE BLANKS")
print("\n")
quiz_dict={"11. WAN stands for ____":"Wide Area Network","12. ____ is a protocol which allows users to download E Mail messages from mail server to a local computer.":"IMAP","13. FTP stands for ___":"File Transfe Protocol","14. Network speed is measured in ___":"Bandwidth","15. SMTP stands for ____":"Simple mail transfer protocol"}
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
tf_dict={"16. Yahoo.com is a domain name.":"T","17. The ARPANET stands for Advanced Research Projects Area.":"F","18.  Tim Berners-Lee proposed WWW.":"T","19.  A modem converts digital signals to analog signals only.":"F","20. The domain name .edu stands for educational institutions.":"T"}
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
            row[1]=(mrks/20)*100
            with open(str(file), mode='w') as us:
                us = csv.writer(us, delimiter=',')
                us.writerow(row)
        except:
            continue

input()









    








