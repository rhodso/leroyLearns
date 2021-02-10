import os

#Get user input
number = int(input("Enter the number of times you want to write the string: "))

#Filepath of where the file is
theFilePath = "./aFile.txt"

#If the file exists, delete it
if os.path.exists(theFilePath):
    print("File exists, deleting")
    os.remove(theFilePath)

#Print the lines to the file
with open(theFilePath, "w") as theFile:
    print("Created file")
    print("Printing strings...")
    for i in range(0, number):
        theFile.write("theString\n")
print("Done!")