import os

theFilePath = "./aFile.txt"

#Check that the file exists
if not os.path.exists(theFilePath):
    print("File doesn't exist, exiting")
    quit(0)

lines = ""
#File exists, attempting read
with open(theFilePath, "r") as theFile:
    lines = theFile.readlines()
    allLines = ""
    for line in lines:
        allLines += line
    print("There are " + str(allLines.count("theString")) + " instances of the string")

#If the file exists, delete it
if os.path.exists(theFilePath):
    os.remove(theFilePath)

print("Done!")