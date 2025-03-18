import os
import requests



huburl = "http://localhost:5002"

mapID = "-1"

# MAP VISUALIZATION

def showmenu():
    os.system('cls')
    print("")
    print("---------------------")
    print("| MAP VISUALIZATION |")
    print("---------------------")
    print("")
    mapID = input("MAP#: ")
    return mapID
    

mapID = showmenu()
fullmap = requests.get(huburl+"/getMapByID/"+mapID).json()
print("Fullmap: ", fullmap)
    
    
