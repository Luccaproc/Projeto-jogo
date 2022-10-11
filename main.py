#definição do caminho (root)
import sys
import os

from classes.explosao import Explosao
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

import pygame 

from pygame.locals import *
from random import randint

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
timeDelta = 0
pygame.mouse.set_visible(0)
game = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Nave teste')

#Obejetos do jogo
nave = Nave(tela_largura,tela_altura) 
explosao = Explosao()

inimigo_spawn = InimigoSpaw()
display_group = pygame.sprite.Group()

explode_group = pygame.sprite.Group()

nave_group = pygame.sprite.Group()
nave_group.add(nave)
fire_group = pygame.sprite.Group()

relogio = pygame.time.Clock()
particles = []

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
            inimigo.life -= shoot.dano
            if(inimigo.life <= 0):
                explosao.adiciona_particulas(inimigo.rect.center[0],inimigo.rect.center[1])
            shoot.kill()
    
    game.fill((70,70,70))
    
    inimigo_spawn.inimigo_group.draw(game)
    fire_group.draw(game)
    nave_group.draw(game)


    explosao.update()

    fire_group.update()
    inimigo_spawn.update(tela_largura,tela_altura)
    nave_group.update(game,tela_largura,tela_altura,vel,width,height)

    pygame.display.flip()
    relogio.tick(fps)
pygame.quit()