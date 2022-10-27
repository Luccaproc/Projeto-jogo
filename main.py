#definição do caminho (root)
from ast import For
from pydoc import cli
import sys
import os
from classes.DisplayPonter import DisplayPointer
from classes.Font import Font
from classes.especial import Especial

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
background = (0,0,0)
x,y,width,height = 20,20,20,20

timeDelta = 0

menu_sound = pygame.mixer.Sound(os.path.join("assets","sounds","music","musica_menu_oficial.wav"))

game = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Nave teste')

#Obejetos do jogo

PERSONAGENS = [
    {   
        'id':1,
        'nome': 'ALEX',
        'velocidade': 10,
        'power': 30,
        'player_img': os.path.join("assets","player","persona1.png")
    },
    {
        'id':2,
        'nome': 'JOTA',
        'velocidade': 15,
        'power': 15,
        'player_img': os.path.join("assets","player","persona1.png")
    },
    {
        'id':3,
        'nome': 'ALITA',
        'velocidade': 15,
        'power': 15,
        'player_img': os.path.join("assets","player","persona1.png")
    },
    {
        'id':3,
        'nome': 'MART',
        'velocidade': 15,
        'power': 15,
        'player_img': os.path.join("assets","player","persona1.png")
    }
]

explosao = Explosao()

vel = 5

inimigo_spawn = InimigoSpaw()
display_group = pygame.sprite.Group()
explode_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

theta = 0

nave_group = pygame.sprite.GroupSingle()
especial_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()
fire_enemy_group = pygame.sprite.Group()
especial_enemy_group = pygame.sprite.Group()
buff_group = pygame.sprite.Group()

relogio = pygame.time.Clock()
particles = []
personas_obj = []

my_font = Font(os.path.join("assets","fonts","small_font.png"))
my_font_large = Font(os.path.join("assets","fonts","large_font.png"))

def menu():
    pygame.mouse.set_visible(1)
    main_menu = True
    click = False
    menu_sound.play()
    while main_menu:
        mx,my = pygame.mouse.get_pos()
        
        button_1 = pygame.Rect(50,(tela_altura)-155,100,40)
        button_2 = pygame.Rect(50,(tela_altura)-100,100,40)
        
        if button_1.collidepoint((mx,my)):
            button_1.inflate_ip(5,5)
            if click :
                menu_sound.fadeout(1000)
                print('clicou')
                main_menu = False
                person_select()
                click = False

        if button_2.collidepoint((mx,my)):
            button_2.inflate_ip(5,5)
            if click :
                pygame.quit()
                click = False

        for event in pygame.event.get():
            keystate = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                main_menu = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

            if keystate[pygame.K_ESCAPE]:
                menu()
        game.fill((0,30,50))
        my_font_large.render(game,"MENU PRINCIPAL",(20,20))

        pygame.draw.rect(game,(100,100,255),button_1,2)
        my_font_large.render(game,"NOVO JOGO",(button_1.center[0]- 30,button_1.center[1] - 5))
        pygame.draw.rect(game,(100,100,255),button_2,2)
        my_font_large.render(game,"SAIR",(button_2.center[0]- 15,button_2.center[1] - 5))



        pygame.display.update()
        relogio.tick(fps)

def person_select():
    selecionando = True
    click = False
    pygame.mouse.set_visible(1)
    while selecionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                selecionando = False
                pygame.quit()

            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                selecionando = False
                menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        game.fill((0,30,50))
        my_font_large.render(game,"ESCOLHA DE PERSONAGEM",((tela_largura/2)-80,50))
        mx, my = pygame.mouse.get_pos()

        for person in range(len(PERSONAGENS)):
            spacing_card = 45
            spacing = 45
            card_width = 200
            card_heigth = 200
            card = pygame.Rect(spacing_card*(person+1)+(200*person),tela_altura-400,card_width,card_heigth)
            persona = pygame.Rect((spacing*(person+1)+(200*person)+5),tela_altura-395,card_width-10,130)
            pygame.draw.rect(game,(100,100,255),card,2)
            pygame.draw.rect(game,(100,100,255),persona,2)
            img_person = pygame.image.load(PERSONAGENS[person]['player_img'])
            pygame.display.get_surface().blit(img_person,((spacing*(person+1)+(200*person)+5),tela_altura-395))
            my_font_large.render(game,"NOME :" + PERSONAGENS[person]['nome'],((spacing*(person+1)+(200*person)+5),tela_altura-260))
            my_font_large.render(game,"POWER :" + str(PERSONAGENS[person]['velocidade']),((spacing*(person+1)+(200*person)+5),tela_altura-240))
            my_font_large.render(game,"VELOCIDADE :" + str(PERSONAGENS[person]['velocidade']),((spacing*(person+1)+(200*person)+5),tela_altura-220))
            if card.collidepoint((mx,my)):
                card.move_ip(10,10)
                card.inflate_ip(5,5)
                if click :
                    jogador = Player(PERSONAGENS[person]['player_img'])
                    player_group.add(jogador)
                    nave = Nave(tela_largura,tela_altura,PERSONAGENS[person]['velocidade'],PERSONAGENS[person]['power']) 
                    nave_group.add(nave)
                    jogo()
                    click = False
        pygame.display.update()
        relogio.tick(fps)

        
def jogo():
    theta = 0
    jogando = True
    pontos = 0
    displayPoint = DisplayPointer(tela_largura/2,0)
    display_group.add(displayPoint)
    pygame.mouse.set_visible(0)
    while jogando:
        theta += 0.5
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                pygame.quit()

            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                jogando = False
                nave_group.empty()
                inimigo_spawn.inimigo_group.empty()
                buff_group.empty()
                fire_group.empty()
                player_group.empty()
                menu()
            # if event.type == pygame.KEYUP:
                # nave.get_damage(50) #testando função de dano

            if keystate[pygame.K_SPACE]:
                if len(nave_group) > 0:
                    # for fire in range(nave_group.sprites()[0].bullet_pow):
                    fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],(nave_group.sprites()[0].rect.center[1])))
                    # if nave_group.sprites()[0].bullet_pow == 1:
                    #     fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.center[1]))
                    # if nave_group.sprites()[0].bullet_pow == 2:
                    #     fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.top))
                    #     fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.bottom))
                    # if nave_group.sprites()[0].bullet_pow == 3:
                    #     fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.top))
                    #     fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.center[1]))
                    #     fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.bottom))
            
            if keystate[pygame.K_r]:
                if len(nave_group) > 0:
                    if nave_group.sprites()[0].especial_qtd > 0:
                        especial_group.add(nave_group.sprites()[0].especial().bullets)
                        nave_group.sprites()[0].especial_qtd -= 1
            if keystate[pygame.K_e]:
                if len(nave_group) > 0:
                    if nave_group.sprites()[0].especial_qtd > 0:
                        especial_group.add(nave_group.sprites()[0].especial2(theta).bullets)
                        nave_group.sprites()[0].especial_qtd -= 1
                    # fire_group.add(nave_group.sprites()[0].especial())
                    # nave_group.sprites()[0].especial().spawnBullets()
                    # if nave_group.sprites()[0].especial_qtd > 0:
                    # fire_group.add(nave_group.sprites()[0].especial(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.center[1]))
                    # nave_group.sprites()[0].especial_qtd -= 1
                    # else:
                    #     print('esgotou')
        for enemy in inimigo_spawn.inimigo_group:
            fire_enemy_group.add(enemy.shoots)
            if enemy.tipe == 5 and enemy.time_cooldown_especial <= 0:
                especial_enemy_group.add(enemy.especial().bullets)

            nave_hit = pygame.sprite.spritecollide(enemy,nave_group,False)
            for nave in nave_hit:
                inimigo_spawn.inimigo_group.remove(enemy)
                nave.get_damage(50)
                enemy.kill()

        for shoot in fire_group:
            inimigo_hit = pygame.sprite.spritecollide(shoot,inimigo_spawn.inimigo_group,False)
            for inimigo in inimigo_hit:
                fire_group.remove(shoot)
                shoot.kill()
                inimigo.life -= shoot.dano
                if(inimigo.life <= 0):
                    pontos += inimigo.pontos
                    display_group.remove(displayPoint)
                    displayPoint = DisplayPointer(tela_largura/2,0)
                    display_group.add(displayPoint)
                    displayPoint.set_point(pontos)
                    rand = randint(0,100)
                    if nave_group.sprites()[0].especial_qtd < nave_group.sprites()[0].especial_max: 
                        nave_group.sprites()[0].especial_qtd += 1
                    if rand < 10:
                        buff_group.add(inimigo.emit_buff())
                    explosao.adiciona_particulas(inimigo.rect.center[0],inimigo.rect.center[1])

        for shoot in especial_group:
            inimigo_hit = pygame.sprite.spritecollide(shoot,inimigo_spawn.inimigo_group,False)
            for inimigo in inimigo_hit:
                especial_group.remove(shoot)
                shoot.kill()
                inimigo.life -= shoot.dano
                if(inimigo.life <= 0):
                    pontos += inimigo.pontos
                    display_group.remove(displayPoint)
                    displayPoint = DisplayPointer(tela_largura/2,0)
                    display_group.add(displayPoint)
                    displayPoint.set_point(pontos)
                    rand = randint(0,100)
                    if nave_group.sprites()[0].especial_qtd < nave_group.sprites()[0].especial_max : 
                        nave_group.sprites()[0].especial_qtd += 1
                    if rand < 10:
                        buff_group.add(inimigo.emit_buff())
                    explosao.adiciona_particulas(inimigo.rect.center[0],inimigo.rect.center[1])

        for shoot in especial_enemy_group:
            nave_hit = pygame.sprite.spritecollide(shoot,nave_group,False)
            for nave in nave_hit:
                especial_enemy_group.remove(shoot)
                shoot.kill()
                nave.get_damage(shoot.dano)

        for shoot in fire_enemy_group:
            nave_hit = pygame.sprite.spritecollide(shoot,nave_group,False)
            for nave in nave_hit:
                fire_enemy_group.remove(shoot)
                nave.get_damage(shoot.dano)
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
                    elif buff.tipe == 2:
                        nave.bullet_pow += buff.power
                        buff.collide()
        
        game.fill((70,70,70))
        
        inimigo_spawn.inimigo_group.draw(game)
        fire_group.draw(game)
        nave_group.draw(game)
        buff_group.draw(game)
        player_group.draw(game)
        especial_group.draw(game)
        display_group.draw(game)
        fire_enemy_group.draw(game)
        especial_enemy_group.draw(game)
        # display_group.update()
        fire_enemy_group.update()
        especial_group.update()
        especial_enemy_group.update()
        explosao.update()
        player_group.update()
        fire_group.update()
        buff_group.update()
        inimigo_spawn.update(tela_largura,tela_altura)
        nave_group.update(game,tela_largura,tela_altura,width,height)
        pygame.display.flip()
        
        relogio.tick(fps)
menu()
pygame.quit()