import pygame
import wave
import wavefunctionlookup as wfl


# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True
highestEntropy = 9
finished = False
triggerTime = 0
timeToTrigger = 0

scaleValue = (512/wave.numberOfTiles[0],512/wave.numberOfTiles[1])

#grassImg = pygame.image.load("TILES/grass.png")
#waldImg = pygame.image.load("TILES/wald.png")
#kuhImg = pygame.image.load("TILES/kuh.png")
#strandImg = pygame.image.load("TILES/strand.png")
#wasserImg = pygame.image.load("TILES/wasser.png")
#fischImg = pygame.image.load("TILES/fisch.png")
#bergImg = pygame.image.load("TILES/berg.png")
#bergschneeImg = pygame.image.load("TILES/bergschnee.png")
#schneemannImg = pygame.image.load("TILES/schneemann.png")

tileImg = pygame.transform.scale(pygame.image.load("TILES/tile.png"), scaleValue)
grassImg = pygame.transform.scale(pygame.image.load("TILES/grass.png"), scaleValue)
waldImg = pygame.transform.scale(pygame.image.load("TILES/wald.png"), scaleValue)
kuhImg = pygame.transform.scale(pygame.image.load("TILES/kuh.png"), scaleValue)
strandImg = pygame.transform.scale(pygame.image.load("TILES/strand.png"), scaleValue)
wasserImg = pygame.transform.scale(pygame.image.load("TILES/wasser.png"), scaleValue)
fischImg = pygame.transform.scale(pygame.image.load("TILES/fisch.png"), scaleValue)
bergImg = pygame.transform.scale(pygame.image.load("TILES/berg.png"), scaleValue)
bergschneeImg = pygame.transform.scale(pygame.image.load("TILES/bergschnee.png"), scaleValue)
schneemannImg = pygame.transform.scale(pygame.image.load("TILES/schneemann.png"), scaleValue)

def selectImage(tile):
    if (wave.numberOfOnes(tile) > 1):
        return tileImg
    if (tile&wfl.binaryLookUpTable["grass"] != 0): return grassImg
    if (tile&wfl.binaryLookUpTable["wald"] != 0): return waldImg
    if (tile&wfl.binaryLookUpTable["kuh"] != 0): return kuhImg
    if (tile&wfl.binaryLookUpTable["strand"] != 0): return strandImg
    if (tile&wfl.binaryLookUpTable["wasser"] != 0): return wasserImg
    if (tile&wfl.binaryLookUpTable["fisch"] != 0): return fischImg
    if (tile&wfl.binaryLookUpTable["berg"] != 0): return bergImg
    if (tile&wfl.binaryLookUpTable["bergschnee"] != 0): return bergschneeImg
    if (tile&wfl.binaryLookUpTable["schneemann"] != 0): return schneemannImg


while running:
    timeToTrigger += clock.tick(60)  # limits FPS to 60
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if (not finished) and (timeToTrigger >= triggerTime):
        finished = wave.algorithmStep(highestEntropy)
        timeToTrigger = 0
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    for y in range (0,len(wave.map[0])):
        for x in range (0,len(wave.map)):
            screen.blit(selectImage(wave.map[y][x]),(scaleValue[0]*x,scaleValue[1]*y))
    # flip() the display to put your work on screen
    pygame.display.flip()

    

pygame.quit()