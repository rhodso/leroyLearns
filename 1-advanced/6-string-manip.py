#Long string of many words
testString = "Here is a string of characters. This string contains lots of letters, but not all of them. It also contains some punctuation!"

#Print stats about the name
def printStats(testString):
    print("Test string is:\n" + testString)
    print("First letter is " + testString[0])
    print("Test string has " + str(testString.count("a")) + " a(s)")
    print("Test string has " + str(testString.count("b")) + " b(s)")
    print("Test string has " + str(testString.count("c")) + " c(s)")
    print("There are " + str(len(testString.split(" "))) + " words")
    print("Below are some slices:")
    print("\tFirst char " + testString[0:1])
    print("\tChars 1-3 " + testString[0:3])
    print("\tLast char " + testString[-1])
    print("\t9th to end " + testString[9:])
    print("")

#Print the stats
printStats(testString)

#Ask the user for input, then print more stats
testString = input("Enter a string: ")
printStats(testString)
