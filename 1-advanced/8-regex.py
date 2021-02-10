#import regular expression package
import re

#Test string from earlier
testString = "Here is a string of characters. This string contains lots of letters, but not all of them. It also contains some punctuation!"

#Regular expression
#Made with help from: https://regexr.com/
regexString = "([^a-z A-Z\s])"

#Find all regex matches, and output
result = re.findall(regexString, testString)
print("Punctuation in the string:")

#Create a string to store matches
string = ""
#For each string in the result, append to current string
for s in result:
    string += s
    
print(string)

#More arcane black magic
emailRegex = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"

#List of email addresses
addressList = {
    "soc.hack@keele.ac.uk",
    "not-avalid-email123@keele",
    "@keele.ac.uk",
    "also-invalidkeele.ac.uk"
}

#Clear the result so that it doesn't get caught up with the other stuff
result.clear()

#For each address in addressList, see if it matches the regex
for address in addressList:
    result += re.findall(emailRegex, address)

#Do the same stuff as before for output
string = ""
for s in result:
    string += "'" + s +"',"
string = string[:-1]
print(string)

