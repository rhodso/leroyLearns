#Imports
import random

#Vars
Output = ""

def getLowercaseLetter():
    #Random ascii character between 97 and 122
    randomNumber = random.randint(97,122)
    return chr(randomNumber)
    
def getUppercaseLetter():
    #Random ascii character between 65 and 90
    randomNumber = random.randint(65,90)
    return chr(randomNumber)
    
def getNumber():
    #Random number between 0 and 9
    return str(random.randint(0,9))
    
print("Enter password format using the key below: \n U = Uppercase letter \n L = Lowercase letter \n N = Number \n")
PasswordFormat = input()
PasswordFormat = PasswordFormat.upper()
PasswordList = [""]*len(PasswordFormat)

for i in range (0,len(PasswordFormat)):
    if(PasswordFormat[i] == "U"):
        PasswordList[i] = getUppercaseLetter()
    
    elif(PasswordFormat[i] == "L"):
        PasswordList[i] = getLowercaseLetter()
    
    elif(PasswordFormat[i] == "N"):
        PasswordList[i] = getNumber()
    
    else:
        print("Character at index " + str(i) + " not recognized, skipping")
    
    Output = Output + PasswordList[i]

print("Generated password = " + Output)