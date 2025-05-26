import os
import requests
import visualization

HUBADDR = "139.6.65.27"
HUBPORT = "31002"

huburl = "http://"+HUBADDR+":"+HUBPORT+"/"

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

visualization.showmap(fullmap)

    
    
