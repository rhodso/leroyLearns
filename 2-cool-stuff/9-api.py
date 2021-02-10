import requests
import json

#Read the docs at: https://pokeapi.co/docs/v2

#Set the base URL
urlBase = "https://pokeapi.co/api/v2/pokemon/"

#Ask user for input
pkName = input("Enter name of pokemon, or it's ID: ")

#Make the request
res = requests.get(url=urlBase + pkName)
if(res.status_code == 200): #Request worked

    #Decode the json
    jsonDict = res.json()

    #Get the name and ID
    name = jsonDict["name"]
    id = jsonDict["id"]

    #Print out the types
    print("Types for " + name + " (ID: " + str(id) + "):")

    #Get the types dict
    types = jsonDict["types"]
    for t in types: #For all types, print out the type
        print(t["type"]["name"])

elif(res.status_code == 404): #Pokemon not found
    print("Pokemon not found")
else: #Other error
    print("Unknown error, code: " + res.status_code)
    