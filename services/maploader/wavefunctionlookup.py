import pandas as pd
import requests
import json


# WAVE FUNCTION TILE LOOKUP TABLE

# URLs
managerurl = "http://139.6.65.27:31000"


tileCompatibilityList = []
tileCompatibilityLookUpTable = {}
binaryLookUpTable = {}

def requestRestrictions():
    global tileCompatibilityList
    global tileCompatibilityLookUpTable
    global binaryLookUpTable
    
    response = requests.get(managerurl+"/restrictions").json()
    
    temp = response[1]
    for i in temp.items():
        tileCompatibilityLookUpTable[int(i[0])] = i[1]
    tileCompatibilityList = response[0]
    binaryLookUpTable = response[2]
