from random import randint
import pygame
from classes.Boss import Boss
from classes.Inimigo import Inimigo

class InimigoSpaw:
    def __init__(self):
        self.inimigo_group = pygame.sprite.Group()
        self.spaw_timer = randint(30,120)
        self.spaw_timer_boss = randint(500,1000)
        self.deltaTime = 0
        self.start_time = pygame.time.get_ticks()
        self.boss = False

    def update(self,tela_largura,tela_altura):
        seconds = (pygame.time.get_ticks() - self.start_time)//1000
        self.inimigo_group.update()
        if self.spaw_timer == 0:
            self.spaw_inimigo(tela_largura,tela_altura)
            self.spaw_timer = randint(20,100)
        elif self.spaw_timer_boss == 0:
            self.spaw_boss(tela_largura,tela_altura)
            self.spaw_timer_boss = randint(500,1000)
        else:
            self.spaw_timer -= 1
            self.spaw_timer_boss -= 1

    def spaw_inimigo(self,tela_largura,tela_altura):
        novo_inimigo = Inimigo(tela_largura,tela_altura)
        self.inimigo_group.add(novo_inimigo)
    
    def spaw_boss(self,tela_largura,tela_altura):
        # seconds = (pygame.time.get_ticks() - self.start_time)//1000
        novo_boss = Boss(tela_largura,tela_altura)
        self.inimigo_group.add(novo_boss)
    # def mob_enemy(self,tela_largura,tela_altura):
    #     seconds = (pygame.time.get_ticks() - self.start_time)//1000
    #     if(seconds % 1 == 0):
    #         novo_inimigo = Inimigo(tela_largura,tela_altura)
    #         self.inimigo_group.add(novo_inimigo)
            