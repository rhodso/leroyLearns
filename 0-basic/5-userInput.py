#Import a library to do things for us
import random

#List of names
newName = [
    "richard",
    "dave",
    "chris",
    "jonah",
    "leroy",
    "jane",
    "jessica",
    "chloe",
    "amy",
    "susan",
    "camilla"
]

#Prompt user for a name
name = input("Enter name: ")

#Tell the user how many characters are in there name
print("You have " + str(len(name)) + " characters in your name")

#Judge their name
if(name.lower() in newName):
    print("Nice name")
else:
    print("That's a shit name, try " + random.choice(newName) + " instead")
