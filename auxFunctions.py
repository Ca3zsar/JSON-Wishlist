import json
from os.path import exists

infoFile = "data.json"
numberOfProducts = 0


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

def getNameURL():
    while True:
        print("Please enter the name of the product: ")
        name = input()
        
        if name != '':
            break
    
    while True:
        print("Please enter the url of the product: ")
        url = input()
        
        if url != '':
            break
        
    return name,url
    