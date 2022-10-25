#definição do caminho (root)
from ast import For
from pydoc import cli
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
        'player_img': os.path.join("assets","player","cabine.png")
    }
]

explosao = Explosao()
vel = 5

inimigo_spawn = InimigoSpaw()
display_group = pygame.sprite.Group()
explode_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


nave_group = pygame.sprite.GroupSingle()

fire_group = pygame.sprite.Group()
buff_group = pygame.sprite.Group()

relogio = pygame.time.Clock()
particles = []
personas_obj = []

def clip(surface,x,y,x_size,y_size):
    handle_surface = surface.copy()
    clipR = pygame.Rect(x,y,x_size,y_size)
    handle_surface.set_clip(clipR)
    image = surface.subsurface(handle_surface.get_clip())
    return image.copy()

class Font():
    def __init__(self,path):
        self.spacing = 1
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        font_img = pygame.image.load(path).convert()
        current_char_width = 0
        x = 0
        self.characters = {}
        char_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x,0))
            if c[0] == 127:
                char_img = clip(font_img,x - current_char_width,0,current_char_width,font_img.get_height())
                char_img = troca_paleta(char_img,(255,0,0),(255,255,255),char_img)
                char_img.set_colorkey((0, 0, 0))
                self.characters[self.character_order[char_count]] = char_img.copy()
                char_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def render(self,surf,text,loc):
        x_offset = 0
        for char in text :
            if char != ' ':
                surf.blit(self.characters[char],(loc[0]+ x_offset,loc[1]))
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing

def troca_paleta(surface,old_c,new_c,obj):
    img_copy = pygame.Surface(obj.get_size())
    img_copy.fill(new_c)
    surface.set_colorkey(old_c)
    img_copy.blit(surface,(0,0))
    return img_copy
    
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

        game.fill((0,30,50))
        my_font_large.render(game,"ESCOLHA DE PERSONAGEM",(20,20))
        mx, my = pygame.mouse.get_pos()

        for person in range(len(PERSONAGENS)):
            persona = pygame.Rect(50+(200*person),tela_altura-400,190,130)
            pygame.draw.rect(game,(100,100,255),persona,2)
            img_person = pygame.image.load(PERSONAGENS[person]['player_img'])
            pygame.display.get_surface().blit(img_person,(50+(200*person),tela_altura-400))
            my_font_large.render(game,"NOME :" + PERSONAGENS[person]['nome'],(55+(200*person),tela_altura-260))
            my_font_large.render(game,"POWER :" + str(PERSONAGENS[person]['velocidade']),(55+(200*person),tela_altura-240))
            my_font_large.render(game,"VELOCIDADE :" + str(PERSONAGENS[person]['velocidade']),(55+(200*person),tela_altura-220))
            if persona.collidepoint((mx,my)):
                persona.inflate_ip(10,10)
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
    jogando = True
    pygame.mouse.set_visible(0)
    while jogando:
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
                    if nave_group.sprites()[0].bullet_qtd == 1:
                        fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.center[1]))
                    if nave_group.sprites()[0].bullet_qtd == 2:
                        fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.top))
                        fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.bottom))
                    if nave_group.sprites()[0].bullet_qtd == 3:
                        fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.top))
                        fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.center[1]))
                        fire_group.add(nave_group.sprites()[0].fire(nave_group.sprites()[0].rect.center[0],nave_group.sprites()[0].rect.bottom))

        for enemy in inimigo_spawn.inimigo_group:
            nave_hit = pygame.sprite.spritecollide(enemy,nave_group,False)
            for nave in nave_hit:
                nave.get_damage(50)
                enemy.kill()

        for shoot in fire_group:
            # drawParticles(shoot)
            pygame.sprite.groupcollide(fire_group,inimigo_spawn.inimigo_group,True,False)
            inimigo_hit = pygame.sprite.spritecollide(shoot,inimigo_spawn.inimigo_group,False)
            for inimigo in inimigo_hit:
                inimigo.life -= shoot.dano
                shoot.kill()
                if(inimigo.life <= 0):
                    rand = randint(0,100)
                    if rand < 10:
                        buff_group.add(inimigo.emit_buff())
                    explosao.adiciona_particulas(inimigo.rect.center[0],inimigo.rect.center[1])
        
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
        nave_group.update(game,tela_largura,tela_altura,width,height)
        pygame.display.flip()
        relogio.tick(fps)
menu()
pygame.quit()