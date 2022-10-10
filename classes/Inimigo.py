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
        self.particles = []

    def on_colide_bullet(self,dano):
        self.life -= Shoot.dano
        print('levou tiro')
        self.explode()
        if(self.life < 0):
            self.kill()

    def explode(self):
        if(not self.alive()):
            for explosion in range(0,5):
                self.particles.append([[self.rect.center[0],self.rect.center[1]],[randint(0,20)/10-1,-2],randint(4,15)])
                for particle in self.particles:
                    print(particle)
                    particle[0][0] += particle[1][0]
                    particle[0][1] += particle[1][0]
                    particle[2] -= 0.01
                    particle[1][1] -= 0.3
                    pygame.draw.circle(pygame.display.get_surface(),(255//(int(particle[2]*0.7)),255//(int(particle[2]*2)),255//(int(particle[2]*2))),[int(particle[0][0]),int(particle[0][1])],int(particle[2]))

    def update(self):
        self.explode()
        if(self.life <= 0):
            self.kill()
        seno = math.sin(self.theta)
        self.rect.x -= self.vel_x
        self.rect.y -= seno*5
        self.theta += 0.1