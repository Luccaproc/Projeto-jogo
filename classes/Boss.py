import math
from random import randint
import pygame

from classes.Heal import Heal
from classes.Power import Power
from classes.Shoot import Shoot
from classes.Velocidade import Velocidade
from classes.especial import Especial

class Boss(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.theta = 0
        self.tipe = 5
        self.life = 1000
        self.startTime = pygame.time.get_ticks()
        self.pontos = randint(100,300)
        self.image = pygame.Surface((100,100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.centery = pos_y/2 - 100
        self.time_cooldown = 50
        self.time_cooldown_especial = 300
        self.rect.x = pos_x
        self.vel_x = 2
        self.metade = False
        self.vel_y = 0
        self.particles = []
        self.shoots = []
        self.especial_boss = []

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

    def especial(self) -> None:
        if self.time_cooldown_especial <= 0:
            time = (pygame.time.get_ticks() - self.startTime)//1000
    
            if time < 10 and time > 0:
                especial = Especial(self.rect.centerx,self.rect.centery,20,2,10)
                especial.spawnBullets()
                return especial
            else:
                self.startTime = pygame.time.get_ticks()
                self.time_cooldown_especial = 300
                especial = Especial(self.rect.centerx,self.rect.centery,20,2,10)
                return especial
        

    def on_colide_bullet(self,dano):
        self.life -= Shoot.dano
        print('levou tiro')
        if(self.life < 0):
            self.kill()
            
    # def explode_bullet(self):
    #     return Explosao(self.rect.center[0],self.rect.center[1])
    def movement(self):

        if self.rect.centerx > 700 and not self.metade:
            coseno = math.cos(self.theta)
            coseno -= self.vel_x
            seno = math.sin(self.theta)
            self.rect.move_ip(coseno,seno*5)
        if self.rect.centerx <= 700 or self.metade:
            self.metade = True
            coseno = math.cos(self.theta/2)
            seno = math.sin(self.theta/2)
            # self.rect.centerx = 600
            self.rect.move_ip(coseno*5,seno*5)

    def update(self):
        if(self.life <= 0):
            self.kill()
        # if(self.rect.centerx < 500):
        #     coseno = math.cos(self.theta)
        #     seno = math.sin(self.theta)
        #     self.rect.centerx += coseno*5
        #     self.rect.centery += seno*5
        #     self.theta += 0.1
        # elif(self.rect.centerx >= 1024):
        self.movement()
        self.time_cooldown -= 1
        self.time_cooldown_especial -= 1
        self.theta += 0.1