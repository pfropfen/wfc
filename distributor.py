import wave
import math



#RULES
numberOfTiles = (16,16)
entropyTolerance = 5


fullMap = [[0b111111111 for x in range(0,numberOfTiles[0])] for y in range(0,numberOfTiles[1])]

numberOfParts = 4


    


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
            
#    for i in range (0,divisions):
#        for j in range (0,divisions):
#            if (i == divisions-1 and j == divisions-1):
#                mapParts[j].append(map[j*int(numberOfTiles[1]/divisions):][i*int(numberOfTiles[0]/divisions):])
#            elif (i==divisions-1):
#                mapParts[j].append(map[j*int(numberOfTiles[1]/divisions):(j+1)*int(numberOfTiles[1]/divisions)][i*int(numberOfTiles[0]/divisions):])
#            elif (j == divisions-1):
#                mapParts[j].append(map[j*int(numberOfTiles[1]/divisions):][i*int(numberOfTiles[0]/divisions):(i+1)*int(numberOfTiles[0]/divisions)])
#            else:
#                print("appening: ", map[j*int(numberOfTiles[1]/divisions):(j+1)*int(numberOfTiles[1]/divisions)][i*int(numberOfTiles[0]/divisions):(i+1)*int(numberOfTiles[0]/divisions)])
#                mapParts[j].append(map[j*int(numberOfTiles[1]/divisions):(j+1)*int(numberOfTiles[1]/divisions)][i*int(numberOfTiles[0]/divisions):(i+1)*int(numberOfTiles[0]/divisions)])
      

    for x in range (0,len(map[0])):
        for y in range (0,len(map)):
            mapParts[int(y/(len(map)/divisions))][int(x/(len(map[0])/divisions))][y%int(len(map)/divisions)][x%int(len(map[0])/divisions)] = map[y][x]
    wave.prettyPrintMap(mapParts[0][0])
    #print(mapParts)
    return mapParts    



        
        
        


