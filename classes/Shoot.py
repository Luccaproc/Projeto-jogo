from random import randint
import pygame

clock = pygame.time.Clock()
class Shoot(pygame.sprite.Sprite):

    def __init__(self,pos_x,pos_y,dano,velocidade,direction, cor):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill(cor)
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.vel = velocidade
        self.dano = dano
        self.qtd = 2
        self.particles = []
        self.explosions = []
        self.direction = direction
    # def drawParticles(self):
    #     self.particles.append([[self.rect.x,self.rect.center[1]],[randint(0,20)/10-1,-2],randint(2,15)])
    #     for particle in self.particles:
    #         particle[0][0] += particle[1][1]
    #         # particle[0][1] += particle[1][0]//3
    #         particle[2] -= 0.5
    #         particle[1][1] -= 0.1
    #         if(int(particle[2]) > 0):
    #             # pygame.draw.circle(game,(255//(int(particle[2]*0.7)),255//(int(particle[2]*2)),255//(int(particle[2]*2))),[int(particle[0][0]),int(particle[0][1])],int(particle[2]))
    #             if(int(particle[2]) < 3):
    #                 pygame.draw.rect(pygame.display.get_surface(),(255//(int(particle[2]*10)),255//(int(particle[2]*10)),255//(int(particle[2]*10))),(int(particle[0][0]),int(particle[0][1]),int(particle[2]),int(particle[2])))
    #             elif(int(particle[2]) > 3):
    #                 pygame.draw.rect(pygame.display.get_surface(),(255//(int(particle[2])*0.5),255//(int(particle[2]*0.5)),255//(int(particle[2]*0.5))),(int(particle[0][0]),int(particle[0][1]),int(particle[2]),int(particle[2])))
    #         if(particle[2] <= 0):
    #             self.particles.remove(particle)

    def on_collide(self):
        self.kill()  

    def update(self):
        # self.drawParticles()
        self.rect.centerx += (self.direction[0]*self.vel)
        self.rect.centery += (self.direction[1]*self.vel)

        if(self.rect.center[0] >= (1024-20) or self.rect.center[0] < 0):
            self.kill()

        if(self.rect.center[1] >= (512-20) or self.rect.center[1] < 0):
            self.kill()