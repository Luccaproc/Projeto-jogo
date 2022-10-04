from asyncio.windows_events import NULL
from copy import copy
from random import randint
from turtle import width
from pygame.locals import *

import math
import pygame 

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,25))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.y = randint(20,tela_altura-20)
        self.rect.x = tela_largura
        self.vel_x = randint(3,8)
        self.vel_y = 0
    def update(self):
        self.rect.x -= self.vel_x
        self.rect.y -= self.vel_y
        # self.rect.center = pygame.Vector2(math.dist())

class InimigoSpaw:
    def __init__(self):
        self.inimigo_group = pygame.sprite.Group()
        self.spaw_timer = randint(30,120)

    def update(self):
        self.inimigo_group.update()
        if self.spaw_timer == 0:
            self.spaw_inimigo()
            self.spaw_timer = randint(30,120)
            
        else:
            self.spaw_timer -= 1
    def spaw_inimigo(self):
        novo_inimigo = Inimigo()
        self.inimigo_group.add(novo_inimigo)

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,25))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (tela_largura/2,tela_altura/2))
    
    def fire(self):
        return Shoot(self.rect.center[0],self.rect.center[1])
        

    def update(self):
        # self.rect.center = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
            if(self.rect.center[0] >= 0):
                self.rect.center = pygame.Vector2(self.rect.center[0]-vel,self.rect.center[1])
            else:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1])
        if keys[pygame.K_RIGHT]:
            if self.rect.center[0] <= (tela_largura/2)-width:
                self.rect.center = pygame.Vector2(self.rect.center[0]+vel,self.rect.center[1])
            else: 
                self.rect.center = pygame.Vector2((tela_largura/2)-width,self.rect.center[1])
        if keys[pygame.K_UP]:
            if self.rect.center[1] >= 0:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1]-vel)
            else:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1])
        if keys[pygame.K_DOWN]:
            if self.rect.center[1] <= (tela_altura)-height:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1]+vel)
            else:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1])

class Shoot(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y) -> None:
        super().__init__()
        self.image = pygame.Surface((10,3))
        self.image.fill((30,30,230))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
    def update(self):
        self.rect.x += vel
        if(self.rect.center[0] >= (tela_largura-20)):
            self.kill()
        
pygame.init()

tela = None
tela_largura,tela_altura = 1024,512
jogando = True
background = (0,0,0)
x,y,width,height = 20,20,20,20
vel = 5

pygame.mouse.set_visible(0)
game = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Nave teste')

#Obejetos do jogo
nave = Nave() 
inimigo_spawn = InimigoSpaw()

nave_group = pygame.sprite.Group()
nave_group.add(nave)
fire_group = pygame.sprite.Group()

relogio = pygame.time.Clock()

while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                fire_group.add(nave.fire())
        
    game.fill((30,30,30))
    inimigo_spawn.inimigo_group.draw(game)
    fire_group.draw(game)
    nave_group.draw(game)

    inimigo_spawn.update()
    fire_group.update()
    nave_group.update()

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()