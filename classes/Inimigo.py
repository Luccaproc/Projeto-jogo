import math
import os
from random import randint
import pygame

from classes.Heal import Heal
from classes.Power import Power
from classes.explosao import Explosao
from classes.Shoot import Shoot
from classes.Velocidade import Velocidade

IMG_HEAL = pygame.image.load(os.path.join("assets","buffs","heal.png"))
class Inimigo(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.theta = 0
        self.tipe = 1
        self.life = 100
        self.pontos = randint(10,20)
        self.image = pygame.Surface((50,25))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.y = randint(int(pos_y-(pos_y*1)),pos_y-50)
        self.rect.x = pos_x
        self.vel_x = 2
        self.metade = False
        self.vel_y = 0
        self.time_cooldown = 100
        self.particles = []
        self.shoots = []

    def emit_buff(self):
        rand = randint(0,2)
        if rand == 0:
            return Heal(self.rect.center[0],self.rect.center[1])
        elif rand == 1:
            return Velocidade(self.rect.center[0],self.rect.center[1])
        elif rand == 2:
            return Power(self.rect.center[0],self.rect.center[1])
        
    def fire(self):
        if self.time_cooldown == 0:
            bala = Shoot(self.rect.centerx,self.rect.centery,20,5,(-1,0),1,(255,0,0))
            self.shoots.append(bala)
            self.time_cooldown = 100

    def on_colide_bullet(self,dano):
        self.life -= Shoot.dano
        print('levou tiro')
        if(self.life < 0):
            self.kill()
            
    def movement(self):
        seno = math.sin(self.theta)
        
        self.rect.move_ip(-self.vel_x,seno*5) 
        
   

    def update(self):
        if(self.life <= 0):
            self.kill()
        self.movement()
        self.fire()
        self.time_cooldown -= 1
        self.theta += 0.1