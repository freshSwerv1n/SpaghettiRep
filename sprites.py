import pygame
from config import *
import math 
import random 

class Player(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.xChange = 0
        self.yChange = 0

        # attempting to animate player 
        sprite_sheet = pygame.image.load("spriteImages/knightImages/Knight_1/Idle.png")
        frame_width = sprite_sheet.get_width() //4
        frame_height = sprite_sheet.get_height()

        #list to store individual frames
        self.frames = []

        #extracting frames from sprite sheet and append them to list 
        for i in range (4):
            frame = sprite_sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
            self.frames.append(frame)
        
        #initializing frame index and setting frame to initial image
        self.current_frame = 0
        self.image = self.frames[self.current_frame]

        #set animation variables
        self.animation_speed = 10
        self.animation_counter = 0

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        self.movement()

        self.rect.x += self.xChange
        self.rect.y += self.yChange

        self.xChange = 0
        self.yChange = 0

        #update the animation 
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.imagev= self.frames[self.current_frame]

#left 
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.rect.x<0:
                if self.game.roomIndex1>0:
                    if not self.game.roomChanged:
                        #This puts the player on the map in the middle room, Kinda unreadable ill fix later
                        new = list(self.game.map[2][2][6])
                        new[11] = '.'
                        replace=''.join(new)
                        self.game.map[2][2][6]=replace
                        self.game.roomChanged=True
                        #
                    self.rect.x=640
                    self.game.roomIndex1-=1
                    for sprite in self.game.blocks:
                        sprite.kill()
                    self.game.createTilemap()
            else:
                self.xChange -= PLAYER_SPEED
                #slf.facing = 'let]ft'
#right 
        if keys[pygame.K_d]:
            if self.rect.x>640:#replace 640 with proper variable
                if self.game.roomIndex1<4:
                    if not self.game.roomChanged:
                        #This puts the player on the map in the middle room, Kinda unreadable ill fix later
                        new = list(self.game.map[2][2][6])
                        new[11] = '.'
                        replace=''.join(new)
                        self.game.map[2][2][6]=replace
                        self.game.roomChanged=True
                        #
                    self.rect.x=0
                    self.game.roomIndex1+=1
                    for sprite in self.game.blocks:
                        sprite.kill()
                    self.game.createTilemap()
            else:
                self.xChange += PLAYER_SPEED
                #slf.facing = 'RIGHT'
   #up     
        if keys[pygame.K_w]:
            if self.rect.y<0:#replace 0 with proper variable
                if self.game.roomIndex2>0:
                    if not self.game.roomChanged:
                        #This puts the player on the map in the middle room, Kinda unreadable ill fix later
                        new = list(self.game.map[2][2][6])
                        new[11] = '.'
                        replace=''.join(new)
                        self.game.map[2][2][6]=replace
                        self.game.roomChanged=True
                        #
                    self.rect.y=480
                    self.game.roomIndex2-=1
                    for sprite in self.game.blocks:
                        sprite.kill()
                    self.game.createTilemap()
            else:
                self.yChange -= PLAYER_SPEED
                #slf.facing = 'up'
 #down       
        if keys[pygame.K_s]:
            if self.rect.y>480:#replace 480 with proper variable
                if self.game.roomIndex2<4:
                    if not self.game.roomChanged:
                        #This puts the player on the map in the middle room, Kinda unreadable ill fix later
                        new = list(self.game.map[2][2][6])
                        new[11] = '.'
                        replace=''.join(new)
                        self.game.map[2][2][6]=replace
                        self.game.roomChanged=True
                        #
                    self.rect.y=0
                    self.game.roomIndex2+=1
                    for sprite in self.game.blocks:
                        sprite.kill()
                    self.game.createTilemap()
            else:
                self.yChange += PLAYER_SPEED
                #slf.facing = 'down'
    #dodge
        if keys [pygame.K_SPACE]:
            self.yChange += PLAYER_SPEED + PLAYER_SPEED
            self.xChange += PLAYER_SPEED + PLAYER_SPEED
            #player moves diagonally down the screen, 

    
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        blockImage = pygame.image.load("spriteImages/rockImages /PNG/Objects_separately/Rock1_1_no_shadow.png")
        self.image = blockImage

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y