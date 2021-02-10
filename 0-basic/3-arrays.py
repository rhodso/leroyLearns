#List of items
shoppingList = ["Beans", "Coffee", "Milk", "Butter", "A will to live"]

#Print the list
for item in shoppingList:
    print(item)
print("")

#Add an item to the list
shoppingList.append("Pringles")

#Print the list again
for item in shoppingList:
    print(item)
print("")

#Print the 4th item of the list
print("")
print(shoppingList[3])
print("")

#Remove an item from the list
shoppingList.remove("Butter")

#Print the list again
for item in shoppingList:
    print(item)
print("")
