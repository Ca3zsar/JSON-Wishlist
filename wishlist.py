import sys
import json
from os.path import exists
from os import system
from datetime import datetime

infoFile = "data.json"
numberOfProducts = 0

options = [
           "Show the wishlist",
           "Add an item",
           "Delete an item",
           "Quit"
           ]

def getNumberOfProducts():
    """ Get the number of products """
    readJson() # Update the global variable 'numberOfProducts'

def createJson():
    """ Create a brand new json file """
    with open(infoFile,'w') as fileObject:
        json.dump({"products":[]},fileObject,indent=4)


def writeJson(newData,action):
    """ Write inside the data file """
    
    if action == "add":
        # Read the current info and add the new item.
        data = readJson()
        values = data["products"]
        values.append(newData)
        
        with open(infoFile,"w") as fileObject:
            json.dump(data, fileObject, indent=4)
            
    if action == "remove":
        with open(infoFile,"w") as fileObject:
            json.dump(newData,fileObject,indent=4)
    

def readJson():
    """ Read the data from the data file and send it back where it is required"""
    
    global numberOfProducts
    
    if not exists(infoFile):
        createJson()
            
    with open(infoFile, 'r') as fileObject:
        data = json.load(fileObject)
    
    #Get the number of products
    numberOfProducts = len(data["products"])
    
    return data


def showList():
    """ Print the list with the actual items """
    
    #Clear the screen.
    system("cls")
    
    data = readJson()
    if not data["products"]:
        print("Your wishlist is currently empty.")
        return
    else:
        print("The products in the wishlist are: ")
        index = 1
        for product in data["products"]:
            print(f"{index}. Name : {product['name']}")
            print(f"   Date : {product['date']}")
            print(f"   URL : {product['url']}")

            index += 1
    
    print() # Print a blank line
    input("Press enter to go back ") # Wait for the user's feedback
    


def addItem():
    """ Add a new product in the wishlist """
    
    product = {} # Create an empty dictionary.
    
    print("Please enter the name of the product: ")
    product["name"] = input()
    
    print("Please enter the url of the product: ")
    product["url"] = input()
    
    now = datetime.now()
    dateAndTime = now.strftime("%d/%m/%Y %H:%M:%S")
    product["date"] = dateAndTime
    
    writeJson(product,"add")
    

def removeItem():
    """ Removes an existing item from the wishlist. """
    
    showList()
    
    while True:
        print("Type in the index of the product you want to remove or 'q' to return: ")
        choice = input()
        
        if choice == 'q':
            return
        else:
            if not (choice.isdecimal() and int(choice) <= numberOfProducts):
                continue
            else:
                data = readJson()
                
                #Delete the item from the value list.
                itemList = data["products"]
                del itemList[int(choice) - 1]
                
                #Write the new data into the file
                writeJson(data,"remove")
                
                return


def menu():
    """ Where the menu will be shown"""
    while True:
        for i in range(1,5):
            print(f"{i}. {options[i-1]} ")
        
        while True:
            choice = input("Please enter an option ( 1-4 ): ")
            if choice.isdecimal() and choice in "1234":
                break
            else:
                continue
        
        choice = int(choice)
        #See the what choice was made.
        
        if choice == 1: # Show the items list
            showList()
        
        if choice == 2: # Add an item
            addItem()
        
        if choice == 3: # Remove an item
            removeItem()
        
        if choice == 4: # Exit the program
            sys.exit()
            
menu()