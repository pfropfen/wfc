import random
import wavefunctionlookup as wfl

numberOfTiles = (16,16)
entropyTolerance = 5

# SET MAP
map = [[0b111111111 for x in range(0,numberOfTiles[0])] for y in range(0,numberOfTiles[1])]


def numberOfOnes(n):
    c = 0
    while n:
        c += 1
        n &= n - 1
    return c


def findLowestEntropyTile():
    # FIND LOWEST ENTROPY TILE 
    lowest = 10
    highest = 1
    listOfLowest = []
    for i in range (0,entropyTolerance+1):
        listOfLowest.append([])
        

    for y,row in enumerate(map):
        for x,col in enumerate(row):
            if (numberOfOnes(col) > 1):
                if (numberOfOnes(col) < lowest):
                    lowest = numberOfOnes(col)
                    for i in range (0,len(listOfLowest)-1):
                        if (i != len(listOfLowest)-1):
                            listOfLowest[len(listOfLowest)-1-i] = listOfLowest[len(listOfLowest)-i-2]
                        else:
                            listOfLowest[0].clear() 

                    listOfLowest[0].append((x,y,col))
                elif (numberOfOnes(col) <= lowest+entropyTolerance and numberOfOnes(col) >= lowest):

                    listOfLowest[numberOfOnes(col)-lowest].append((x,y,col))
                    
                    
    for y,row in enumerate(map):
        for x,col in enumerate(row):
            if (numberOfOnes(col) > highest):
                highest = numberOfOnes(col)
                

    
    listCombined = []
    for i in listOfLowest:
        listCombined += i
        
    if (len(listCombined) == 0):
        return 0, highest
    
    return random.choice(listCombined), highest
    
    
def collapseTile(tile):
    t = tile
    num = numberOfOnes(t)
    r = random.randint(1,num)  
    ind = 0
   
    while (r>0):
        if (t&(2**ind) != 0):
            r -= 1
            if (r == 0):
                t = 2**ind
        ind+=1
    return t
 
 
def combinedTileCondition(tile):
    combined = 0b111111111

    for t in wfl.tileCompatibilityLookUpTable.items():
        if (tile & t[1] == 0):
            combined &= t[0]^0b111111111
    return combined
            
            


def updateMap(toUpdate):
    nextUpdate = []
    for tile in toUpdate:
        x = tile[0]
        y = tile[1]
        condition = combinedTileCondition(tile[2])
        if (x+1 < len(map[0])):
            temp = map[y][x+1]
            map[y][x+1] &= condition
            if (temp != map[y][x+1]):
                nextUpdate.append((x+1,y,map[y][x+1]))
        if (y+1 < len(map)):
            temp = map[y+1][x]
            map[y+1][x] &= condition
            if (temp != map[y+1][x]):
                nextUpdate.append((x,y+1,map[y+1][x]))
        if (x-1 >= 0):
            temp = map[y][x-1]
            map[y][x-1] &= condition
            if (temp != map[y][x-1]):
                nextUpdate.append((x-1,y,map[y][x-1]))
        if (y-1 >=0):
            temp = map[y-1][x]
            map[y-1][x] &= condition
            if (temp != map[y-1][x]):
                nextUpdate.append((x,y-1,map[y-1][x]))
 
 
#        if (x+1 < len(map[0]) and y-1 > 0):
#            temp = map[y-1][x+1]
#            map[y-1][x+1] &= condition
#            if (temp != map[y-1][x+1]):
#                nextUpdate.append((x+1,y-1,map[y-1][x+1]))
#        if (x+1 < len(map[0]) and y+1 < len(map)):
#            temp = map[y+1][x+1]
#            map[y+1][x+1] &= condition
#            if (temp != map[y+1][x+1]):
#                nextUpdate.append((x+1,y+1,map[y+1][x+1]))
#        if (x-1 > 0) and y+1 < len(map):
#            temp = map[y+1][x-1]
#            map[y+1][x-1] &= condition
#            if (temp != map[y+1][x-1]):
#                nextUpdate.append((x-1,y+1,map[y+1][x-1]))
#        if (x-1 > 0) and y-1 > 0:
#            temp = map[y-1][x-1]
#            map[y-1][x-1] &= condition
#            if (temp != map[y-1][x-1]):
#                nextUpdate.append((x-1,y-1,map[y-1][x-1]))
        
    if (len(nextUpdate)>0):
        updateMap(nextUpdate)
        

def prettyPrintMap(map):
    def drawHorizontalLine(length):
        for r in range(0,length):
            print("-", end='')
             
    distance = 6
    drawHorizontalLine(distance*numberOfTiles[0]-1+11*numberOfTiles[0]+1)
    for y in range (0,len(map[0])):
        print("")
        print("|   ", end='')
        for x in range (0,len(map)):
            print(bin(map[y][x]), end='')
            fill = 11 - len(bin(map[y][x]))
            for f in range (0,fill):
                print(" ", end='')
            for a in range (0,int(distance/2)):
                print(" ", end='')
            print("|", end='')
            for a in range (0,int(distance/2)):
                print(" ", end='')
        print("")
        drawHorizontalLine(distance*numberOfTiles[0]-1+11*numberOfTiles[0]+1)          
    print("")

    
                


def algorithmStep(highestEntropy):
    lowestEntropyTile, highestEntropy = findLowestEntropyTile()
    if (highestEntropy <= 1):
        return True
    #print("highestEntropy: ", highestEntropy)
    x = lowestEntropyTile[0]
    y = lowestEntropyTile[1]

    #print("x: ",x)
    #print("y: ",y)

    map[y][x] = collapseTile(map[y][x])
    updateMap([(x,y,map[y][x])])

    #prettyPrintMap(map)
    
    return False
         









