#definição do caminho (root)
from random import randint
import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

import pygame 

from pygame.locals import *

#Classes / Game objects
from classes.Inimigo import Inimigo
from classes.InimigoSpaw import InimigoSpaw
from classes.Nave import Nave
from classes.Shoot import Shoot

        
pygame.init()

fps = 30
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
particles = []

def drawParticles(game_object):
    if(game_object.alive()):
        particles.append([[game_object.rect.x,game_object.rect.center[1]],[randint(0,20)/10-1,-2],randint(4,15)])
        for particle in particles:
            particle[0][0] += particle[1][1]
            particle[0][1] += particle[1][0]
            particle[2] -= 0.2
            particle[1][1] -= 0.3
            if(int(particle[2]*0.3) > 0):
                # pygame.draw.circle(game,(255//(int(particle[2]*0.7)),255//(int(particle[2]*2)),255//(int(particle[2]*2))),[int(particle[0][0]),int(particle[0][1])],int(particle[2]))
                pygame.draw.rect(game,(255//(int(particle[2]*0.3)),255//(int(particle[2]*0.6)),255//(int(particle[2]*2))),(int(particle[0][0]),int(particle[0][1]),int(particle[2]),int(particle[2])))
            if(particle[2] <= 0):
                particles.remove(particle)
    

while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
        if event.type == pygame.KEYUP:
            # nave.get_damage(50) #testando função de dano
            if event.key == pygame.K_SPACE:
                fire_group.add(nave.fire())
    if(pygame.sprite.spritecollideany(nave,inimigo_spawn.inimigo_group) != None):
        nave.get_damage(50)
        pygame.sprite.spritecollide(nave,inimigo_spawn.inimigo_group,True)
    
    for shoot in fire_group:
        # drawParticles(shoot)
        inimigo_hit = pygame.sprite.spritecollide(shoot,inimigo_spawn.inimigo_group,False)
        for inimigo in inimigo_hit:
            print('shoot:',shoot.dano) 
            print('inimigo:',inimigo.life)
            inimigo.life -= shoot.dano

    
    game.fill((30,30,30))
    inimigo_spawn.inimigo_group.draw(game)
    fire_group.draw(game)
    nave_group.draw(game)
    drawParticles(nave)
    inimigo_spawn.update(tela_largura,tela_altura)
    fire_group.update()
    nave_group.update(game,tela_largura,tela_altura,vel,width,height)

    pygame.display.flip()
    relogio.tick(fps)

pygame.quit()