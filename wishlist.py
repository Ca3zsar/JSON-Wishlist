import sys
import json


import wishFunctions
import auxFunctions

options = [
           "Show the wishlist",
           "Add an item",
           "Delete an item",
           "Edit an item",
           "Clear the list",
           "Quit"
           ]

def menu():
    """ Where the menu will be shown"""
    while True:
        for i in range(len(options)):
            print(f"{i+1}. {options[i]} ")
        
        while True:
            choice = input("Please enter an option ( 1-6 ): ")
            if choice.isdecimal() and choice in "123456":
                break
            else:
                continue
        
        choice = int(choice)
        #See the what choice was made.
        
        if choice == 1: # Show the items list
            wishFunctions.showList()
        
        if choice == 2: # Add an item
            wishFunctions.addItem()
        
        if choice == 3: # Remove an item
            wishFunctions.removeItem()
        
        if choice == 4: # Edit an item
            wishFunctions.editItem()
        
        if choice == 5: # Clear the list
            wishFunctions.clearList()
        
        if choice == 6: # Exit the program
            sys.exit()
            
menu()