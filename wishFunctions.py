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
    
    name, url = auxFunctions.getNameURL()
    
    product["name"] = name
    product["url"] = url
    
    now = datetime.now()
    dateAndTime = now.strftime("%d/%m/%Y %H:%M:%S")
    product["date"] = dateAndTime
    
    auxFunctions.writeJson(product,"add")
    

def removeItem():
    """ Removes an existing item from the wishlist. """
    
    # If there are no items, return.
    if auxFunctions.numberOfProducts == 0:
        print("There are no items to remove!")
        return
    
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
    
    
def editItem():
    """ Edit an item from the list """
    
    # If there is no item in the list, return.
    if auxFunctions.numberOfProducts == 0:
        print("There are no items to edit!")
        return 
    
    showList()
    
    while True:
        print("Type in the index of the product you want to edit or 'q' to return: ")
        choice = input()
        
        if choice == 'q':
            return
        else:
            if not (choice.isdecimal() 
                    and int(choice) <= auxFunctions.numberOfProducts):
                continue
            else:
                choice = int(choice)
            
                data = auxFunctions.readJson()
                products = data["products"]
                tempProduct = products.pop(choice-1)
                
                auxFunctions.writeJson(data,"remove")
                
                choice = int(choice)
                
                #Edit the item from the value list.
                name = input("Enter a new name or press enter to leave it as it is: ")
                
                if name != '':
                    tempProduct["name"] = name
                    
                url = input("Enter a new url or press enter to leave it as it is: ")
                
                if url != '':
                    tempProduct["url"] = url
                    
                auxFunctions.writeJson(tempProduct,"add")
                
                return
                    

def clearList():
    """ Clear the list """
    if auxFunctions.deleteJson():
        auxFunctions.createJson()
    else:
        print("There is no list at the moment!")
                
            
            