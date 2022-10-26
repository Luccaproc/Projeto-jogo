import math
import pygame

from classes.Shoot import Shoot

class Especial(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,dano,velocidade):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.vel = velocidade
        self.dano = dano
        self.qtd = 2
        self.particles = []
        self.explosions = []
        self.theta = 0
        self.spaw_timer = 50

    # def rotate_bullet(self):

    def update(self) -> None:
        sen = math.sin(self.theta)
        cos = math.cos(self.theta)
        
        self.rect.centerx += cos*self.theta
        self.rect.centery += sen*self.theta
        if(self.rect.centerx > (1024-20) or self.rect.centerx < 0):
            self.kill()
        if(self.rect.centery > (512-20) or self.rect.centery < 0):
            self.kill()
        # for num in range(20):
        #     return Shoot(xpos,ypos,20,5)
        self.theta += 0.1
        self.spaw_timer -= 1
