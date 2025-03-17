import wave
import math
import requests
from flask import Flask, request, render_template, redirect
import uuid


app = Flask(__name__)

@app.route("/")
def showHome():
    return "SERVICE FOR DISTRIBUTING MAPS"
    
@app.route("/generateMap",methods=["GET","POST"])
def generateMap():
    if request.method == 'POST':
        generateMap()
        return render_template('distributor.html')+"\n<H1> BLABLA </H1>"
    elif request.method == 'GET':
        return render_template('distributor.html')




def getRules():
    # GET RULES
    numberOfTilesResponse = requests.get("http://127.0.0.1:5000/numberOfTiles").json()
    numberOfPartsResponse = requests.get("http://127.0.0.1:5000/numberOfParts").json()
    entropyToleranceResponse = requests.get("http://127.0.0.1:5000/entropyTolerance").json()

    numberOfTiles = (numberOfTilesResponse[0],numberOfTilesResponse[1])
    numberOfParts = numberOfPartsResponse
    entropyTolerance = entropyToleranceResponse
    
    return {"numberOfTiles":numberOfTiles, "numberOfParts":numberOfParts, "entropyTolerance":entropyTolerance}



def setMap(numberOfTiles):
    # SET MAP
    fullMap = [[0b111111111 for x in range(0,numberOfTiles[0])] for y in range(0,numberOfTiles[1])]
    return fullMap




    


def distributeMap(map, numberOfParts):
    divisions = int(math.sqrt(numberOfParts))
    mapParts = []
    for i in range (0,divisions):
        mapParts.append([])
        for j in range (0,divisions):
            mapParts[i].append([])
            for k in range (0,int(len(map)/divisions)):
                mapParts[i][j].append([])
                for l in range (0,int(len(map[0])/divisions)):
                    mapParts[i][j][k].append(0)
        
        
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
            mapParts[int(y/(len(map)/divisions))][int(x/(len(map[0])/divisions))][y%int(len(map)/divisions)][x%int(len(map[0])/divisions)] = map[y][x]
    wave.prettyPrintMap(mapParts[0][0])
    #print(mapParts)
    return mapParts    



    def generateMap():
        rules = getRules()
        wave.numberOfTiles = rules["numberOfTiles"]
        wave.entropyTolerance = rules["entropyTolerance"]
        fullMap = setMap(rules["numberOfTiles"])
        mapParts = distributeMap(fullMap, rules["numberOfParts"])
        
        # 
        mapID = str(uuid.uuid4())
        
        for x in range(0,len(mapParts[0])):
            for y in range(0,len(mapParts)):
                # ETWAS
                
        # SEND PARTS TO HUB
        
        
        
        


