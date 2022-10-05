#definição do caminho (root)
import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

import pygame 
from pygame.locals import *

from random import randint
import math
from tkinter.tix import Tree

#Classes / Game objects
from classes.Inimigo import Inimigo
from classes.InimigoSpaw import InimigoSpaw
from classes.Nave import Nave
from classes.Shoot import Shoot

        
pygame.init()

fps = 60
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
nave = Nave(tela_largura,tela_altura) 

inimigo_spawn = InimigoSpaw()
display_group = pygame.sprite.Group()

nave_group = pygame.sprite.Group()
nave_group.add(nave)
fire_group = pygame.sprite.Group()

relogio = pygame.time.Clock()

while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
        if event.type == pygame.KEYUP:
            # nave.get_damage(50) #testando função de dano
            if event.key == pygame.K_SPACE:
                fire_group.add(nave.fire())
    game.fill((30,30,30))
    inimigo_spawn.inimigo_group.draw(game)
    fire_group.draw(game)
    nave_group.draw(game)

    inimigo_spawn.update(tela_largura,tela_altura)
    fire_group.update()
    nave_group.update(game,tela_largura,tela_altura,vel,width,height)

    pygame.display.flip()
    relogio.tick(fps)

pygame.quit()