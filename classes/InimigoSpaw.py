from random import randint
import pygame
from classes.Inimigo import Inimigo

class InimigoSpaw:
    def __init__(self):
        self.inimigo_group = pygame.sprite.Group()
        self.spaw_timer = randint(30,120)

    def update(self,tela_largura,tela_altura):
        self.inimigo_group.update()
        if self.spaw_timer == 0:
            self.spaw_inimigo(tela_largura,tela_altura)
            self.spaw_timer = randint(20,100)
        else:
            self.spaw_timer -= 1

    def spaw_inimigo(self,tela_largura,tela_altura):
        novo_inimigo = Inimigo(tela_largura,tela_altura)
        self.inimigo_group.add(novo_inimigo)