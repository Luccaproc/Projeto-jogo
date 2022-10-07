import math
from random import randint
import pygame

from classes.Shoot import Shoot
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

    def on_colide_bullet(self,dano):
        self.life -= Shoot.dano
        print('levou tiro')
        if(self.life < 0):
            self.kill()
    
    def update(self):
        if(self.life <= 0):
            self.kill()
        seno = math.sin(self.theta)
        self.rect.x -= self.vel_x
        self.rect.y -= seno*5
        self.theta += 0.1