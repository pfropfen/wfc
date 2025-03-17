import wave
import math
import requests
from flask import Flask, request, render_template, redirect
import uuid
import json


app = Flask(__name__)

huburl = "http://localhost:5002"
managerurl = "http://localhost:5000"

@app.route("/")
def showHome():
    return "SERVICE FOR DISTRIBUTING MAPS"
    
@app.route("/mapGenerator",methods=["GET","POST"])
def mapGenerator():
    if request.method == 'POST':
        generateMap()
        return render_template('distributor.html')+"\n<H1> GENERATED </H1>"
    elif request.method == 'GET':
        return render_template('distributor.html')




def getRules():
    # GET RULES
    numberOfTilesResponse = requests.get(managerurl+"/numberOfTiles").json()
    numberOfPartsResponse = requests.get(managerurl+"/numberOfParts").json()
    entropyToleranceResponse = requests.get(managerurl+"/entropyTolerance").json()

    numberOfTiles = (numberOfTilesResponse[0],numberOfTilesResponse[1])
    numberOfParts = numberOfPartsResponse
    entropyTolerance = entropyToleranceResponse
    
    return {"numberOfTiles":numberOfTiles, "numberOfParts":numberOfParts, "entropyTolerance":entropyTolerance}



def setMap(t):
    # SET MAP
    fullMap = [[0b111111111 for x in range(0,t[0])] for y in range(0,t[1])]
    return fullMap




    


def distributeMap(map, numberOfParts):
    divisions = int(math.sqrt(numberOfParts))
    mapChunks = []
    for i in range (0,divisions):
        mapChunks.append([])
        for j in range (0,divisions):
            mapChunks[i].append([])
            for k in range (0,int(len(map)/divisions)):
                mapChunks[i][j].append([])
                for l in range (0,int(len(map[0])/divisions)):
                    mapChunks[i][j][k].append(0)
        
        
    if (len(map) % divisions != 0) or (len(map[0]) % divisions != 0):
        print("MAP SIZE NOT DISTRIBUTABLE")
        return 0
        
    for y in range (0,len(map)):
        for i in range (1, int(divisions)):
            x = int(len(map[0])/(divisions))*i-1
            map[y][x] = wave.collapseTile(map[y][x])
            wave.updateMap([(x,y,map[y][x])])
            map[y][x+1] = wave.collapseTile(map[y][x+1])
            wave.updateMap([(x+1,y,map[y][x+1])])
    for x in range (0,len(map[0])):
        for i in range (1, int(divisions)):
            y = int(len(map)/(divisions))*i-1
            map[y][x] = wave.collapseTile(map[y][x])
            wave.updateMap([(x,y,map[y][x])])
            map[y+1][x] = wave.collapseTile(map[y+1][x])
            wave.updateMap([(x,y+1,map[y+1][x])])
              

    for x in range (0,len(map[0])):
        for y in range (0,len(map)):
            mapChunks[int(y/(len(map)/divisions))][int(x/(len(map[0])/divisions))][y%int(len(map)/divisions)][x%int(len(map[0])/divisions)] = map[y][x]
    #wave.prettyPrintMap(mapChunks[0][0])
    #print("MAPCHUNKS: ",mapChunks)
    return mapChunks    



def generateMap():
    rules = getRules()
    wave.numberOfTiles = rules["numberOfTiles"]
    wave.entropyTolerance = rules["entropyTolerance"]
    fullMap = setMap(rules["numberOfTiles"])
    wave.map = fullMap
    mapChunks = distributeMap(fullMap, rules["numberOfParts"])
    
    
    data = []
    mapID = str(uuid.uuid4())

    for x in range(0,len(mapChunks[0])):
        for y in range(0,len(mapChunks)):
            data.append({"mapID":mapID,"chunkID":str(uuid.uuid4()), "locX":x,"locY":y,"entropyTolerance":rules["entropyTolerance"],"content":mapChunks[y][x]})
    obj = json.dumps(data)
    result = requests.post(huburl+"/saveChunks", json=obj)
    # SEND PARTS TO HUB
        
        
        
        


