import pygame
import wavefunctionlookup as wfl
from wave import numberOfOnes


displaySizeX = 512
displaySizeY = 512

wfl.requestRestrictions()


def initializeTiles(scaleValue):
    global tileImg
    global grassImg
    global waldImg
    global kuhImg
    global strandImg
    global wasserImg
    global fischImg
    global bergImg
    global bergschneeImg
    global schneemannImg
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


def selectImage(tile, scaleValue):
    if (numberOfOnes(tile) > 1):
        canvas = pygame.Surface(scaleValue,pygame.SRCALPHA)
        canvas.fill((255,255,255,255))

        for e in range (0,8):
            if (tile&(2**e) != 0):
                tempImg = selectImage(2**e, scaleValue).copy()
                tempImg.set_alpha(128)
                canvas.blit(tempImg,(0,0),special_flags=pygame.BLEND_RGBA_MULT)
        return canvas
        
    if (tile&wfl.binaryLookUpTable["grass"] != 0): return grassImg
    if (tile&wfl.binaryLookUpTable["wald"] != 0): return waldImg
    if (tile&wfl.binaryLookUpTable["kuh"] != 0): return kuhImg
    if (tile&wfl.binaryLookUpTable["strand"] != 0): return strandImg
    if (tile&wfl.binaryLookUpTable["wasser"] != 0): return wasserImg
    if (tile&wfl.binaryLookUpTable["fisch"] != 0): return fischImg
    if (tile&wfl.binaryLookUpTable["berg"] != 0): return bergImg
    if (tile&wfl.binaryLookUpTable["bergschnee"] != 0): return bergschneeImg
    if (tile&wfl.binaryLookUpTable["schneemann"] != 0): return schneemannImg


def showmap(mapdata):
    pygame.init()
    screen = pygame.display.set_mode((displaySizeX, displaySizeY))
    clock = pygame.time.Clock()
    running = True
    scaleValue = (displaySizeX/len(mapdata[0]),displaySizeY/len(mapdata))
    initializeTiles(scaleValue)
    while running:
        clock.tick(60)  # limits FPS to 60
        
        # polls for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # fills the screen with a color
        screen.fill("white")

        # RENDERING
        for y in range (0,len(mapdata[0])):
            for x in range (0,len(mapdata)):
                screen.blit(selectImage(mapdata[y][x], scaleValue),(scaleValue[0]*x,scaleValue[1]*y))
        pygame.display.flip()
