import math
import os
from random import randint
import pygame

from classes.Heal import Heal
from classes.explosao import Explosao
from classes.Shoot import Shoot
from classes.Velocidade import Velocidade

IMG_HEAL = pygame.image.load(os.path.join("assets","buffs","heal.png"))
class Inimigo(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.theta = 0
        self.life = 50
        self.image = pygame.Surface((50,25))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.y = randint(int(pos_y-(pos_y*1)),pos_y-50)
        self.rect.x = pos_x
        self.vel_x = 5
        self.metade = False
        self.vel_y = 0
        self.particles = []

    def emit_buff(self):
        rand = randint(0,1)
        if rand == 0:
            return Heal(self.rect.center[0],self.rect.center[1])
        elif rand == 1:
            return Velocidade(self.rect.center[0],self.rect.center[1])
        

    def on_colide_bullet(self,dano):
        self.life -= Shoot.dano
        print('levou tiro')
        if(self.life < 0):
            self.kill()
            
    # def explode_bullet(self):
    #     return Explosao(self.rect.center[0],self.rect.center[1])

    def update(self):
        if(self.life <= 0):
            self.kill()
        seno = math.sin(self.theta)
        self.rect.x -= self.vel_x
        self.rect.centery = (self.rect.centery) - (seno*5)
        self.theta += 0.1