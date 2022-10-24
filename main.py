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
from classes.Heal import Heal
from classes.Inimigo import Inimigo
from classes.InimigoSpaw import InimigoSpaw
from classes.Nave import Nave
from classes.Shoot import Shoot
from classes.player import Player
        
pygame.init()

fps = 60
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
jogador = Player()
explosao = Explosao()

inimigo_spawn = InimigoSpaw()
display_group = pygame.sprite.Group()

explode_group = pygame.sprite.Group()

player_group = pygame.sprite.Group()
player_group.add(jogador)

nave_group = pygame.sprite.Group()
nave_group.add(nave)

fire_group = pygame.sprite.Group()
buff_group = pygame.sprite.Group()

relogio = pygame.time.Clock()
particles = []

while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
        keystate = pygame.key.get_pressed()

        # if event.type == pygame.KEYUP:
            # nave.get_damage(50) #testando função de dano
        if keystate[pygame.K_SPACE]:
            if nave.bullet_qtd == 1:
                fire_group.add(nave.fire(nave.rect.center[0],nave.rect.center[1]))
            if nave.bullet_qtd == 2:
                fire_group.add(nave.fire(nave.rect.center[0],nave.rect.top))
                fire_group.add(nave.fire(nave.rect.center[0],nave.rect.bottom))
            if nave.bullet_qtd == 3:
                fire_group.add(nave.fire(nave.rect.center[0],nave.rect.top))
                fire_group.add(nave.fire(nave.rect.center[0],nave.rect.center[1]))
                fire_group.add(nave.fire(nave.rect.center[0],nave.rect.bottom))

    if(pygame.sprite.spritecollideany(nave,inimigo_spawn.inimigo_group) != None):
        nave.get_damage(50)
        pygame.sprite.spritecollide(nave,inimigo_spawn.inimigo_group,True)
    
    for shoot in fire_group:
        # drawParticles(shoot)
        inimigo_hit = pygame.sprite.spritecollide(shoot,inimigo_spawn.inimigo_group,False)
        for inimigo in inimigo_hit:
            inimigo.life -= shoot.dano
            if(inimigo.life <= 0):
                rand = randint(0,100)
                if rand < 100:
                    buff_group.add(inimigo.emit_buff())
                explosao.adiciona_particulas(inimigo.rect.center[0],inimigo.rect.center[1])
            shoot.kill()
    
    for buff in buff_group:
        get_buff = pygame.sprite.spritecollide(buff,nave_group,False)
        for nave in get_buff:
            if(nave.vida_atual < nave.vida_maxima):
                if buff.tipe == 0:
                    nave.vida_atual += buff.cura
                    buff.collide()
                elif buff.tipe == 1:
                    nave.velocidade += buff.velocidade
                    buff.collide()
    
    game.fill((70,70,70))
    
    inimigo_spawn.inimigo_group.draw(game)
    fire_group.draw(game)
    nave_group.draw(game)
    buff_group.draw(game)
    player_group.draw(game)

    explosao.update()
    player_group.update()
    fire_group.update()
    buff_group.update()
    inimigo_spawn.update(tela_largura,tela_altura)
    nave_group.update(game,tela_largura,tela_altura,vel,width,height)
    vel += 0.01
    pygame.display.flip()
    relogio.tick(fps)
pygame.quit()