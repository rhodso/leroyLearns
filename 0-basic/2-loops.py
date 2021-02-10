#Enter a number to print times table for
number = 4
for i in range(0,13):
    print(str(i*number) + "\t")

#Spacer
print("")

#Print full timetable
for i in range(0,13):
    for j in range(0,13):
        print(str(i*j) + "\t",end="")
    print("")