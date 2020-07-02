import json
from os import system
from datetime import datetime

import auxFunctions

def showList():
    """ Print the list with the actual items """
    
    #Clear the screen.
    system("cls")
    
    data = auxFunctions.readJson()
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
    
    auxFunctions.writeJson(product,"add")
    

def removeItem():
    """ Removes an existing item from the wishlist. """
    
    showList()
    
    while True:
        print("Type in the index of the product you want to remove or 'q' to return: ")
        choice = input()
        
        if choice == 'q':
            return
        else:
            if not (choice.isdecimal() 
                    and int(choice) <= auxFunctions.numberOfProducts):
                continue
            else:
                data = auxFunctions.readJson()
                
                #Delete the item from the value list.
                itemList = data["products"]
                del itemList[int(choice) - 1]
                
                #Write the new data into the file
                auxFunctions.writeJson(data,"remove")
                
                return
    
