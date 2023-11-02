import pygame
from sprites import *
from config import *
import sys
import random


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font('Arial', 32)
        self.running = True

    def createTilemap(self):
        for i, row in enumerate(self.map[self.roomIndex1][self.roomIndex2]):
            for j, column in enumerate(row):
                if column == 'B':
                    Block(self, j, i)
                if column =='P':
                    Player(self, j, i)

    def new(self):
    # a new game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.map=self.generateMap()
        self.roomIndex1=2
        self.roomIndex2=2
        self.roomChanged=False#hacky fix, remove later
        #self.attacks + pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def generateMap(self):
        map=[]
        for j in range(5):
            row=[]
            for i in range(5):
                row.append(self.generateRoom())
            map.append(row)

        #This puts the player on the map in the middle room, Kinda unreadable ill fix later
        new = list(map[2][2][6])
        new[11] = 'P'
        replace=''.join(new)
        map[2][2][6]=replace
        #

        return map
    

    def generateRoom(self):
        baseTileMap= [
            'BBBBBBBB...BBBBBBBBB',
            'B..................B',
            'B..................B',
            'B..................B',
            'B..................B',
            'B..................B',
            'B..................B',
            'B..................B',
            '....................',
            '....................',
            'B..................B',
            'B..................B',
            'B..................B',
            'B..................B',
            'BBBBBBBB...BBBBBBBBB',
        ]
        newTileMap=[]
        for row in baseTileMap:
            rowString=""
            for tile in row:
                if tile==".":
                    blockCheck=random.uniform(0, 1)
                    if blockCheck>0.95:
                        rowString+='B'
                    else:
                        rowString+='.'
                else:
                    rowString+='B'
            newTileMap.append(rowString)
        return (newTileMap)


    def events(self): 
        #game loop event s
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False


    def update(self):
        #game loop update
        self.all_sprites.update()
    
    def draw(self):
        #a game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self): 
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    
    def gameOver(self):
        pass

    def intro_screen(self):
            pass

print('l66')
g = Game()
print('l68')
g.intro_screen()
g.new()

while g.running:
    g.main()

pygame.quit()
print('l78')
sys.exit()