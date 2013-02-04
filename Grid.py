from pygame import Rect
from random import randrange


class Tile:
    def __init__(self, rect):
        self.rect = rect
        self.color = tuple([randrange(1,255) for x in range(3)] + [0])

    def draw(self, game, surf):
        game.draw.rect(surf, self.color, self.rect)



class Grid:
    def __init__(self, offX, offY, totalWidth, totalHeight, padSize=0.95):
        self.size = 5
        self.width = totalWidth
        self.height = totalHeight
        self.tileWidth = int(padSize * totalWidth/self.size)
        self.tileHeight = int(padSize * totalHeight/self.size)
        self.padWidth = int( (totalWidth - self.tileWidth*self.size)/self.size )
        self.padHeight = int((totalHeight - self.tileHeight*self.size)/self.size)
        self.offX = offX
        self.offY = offY
        self.tiles = []

        self.genTiles()


    def genTiles(self):
        tileWUnit = self.tileWidth + self.padWidth
        xoffsets = [x+self.padWidth+self.offX for x in xrange(0, self.width-self.padWidth, tileWUnit)]

        tileHUnit = self.tileHeight + self.padHeight
        yoffsets = [y+self.padHeight + self.offY for y in xrange(0, self.height-self.padHeight, tileHUnit)]


        for x in xoffsets:
            for y in yoffsets:
                self.tiles.append(Tile(Rect(x,y, self.tileWidth, self.tileHeight)))



    def draw(self, game, surface):
        for t in self.tiles:
            t.draw(game, surface)
