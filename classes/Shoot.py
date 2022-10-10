from random import randint
import pygame

clock = pygame.time.Clock()
class Shoot(pygame.sprite.Sprite):

    def __init__(self,pos_x,pos_y,dano,velocidade):
        super().__init__()
        self.image = pygame.Surface((10,3))
        self.image.fill((30,30,230))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.vel = velocidade
        self.dano = dano
        self.particles = []
        self.explosions = []
    
    def drawParticles(self):
        self.particles.append([[self.rect.x,self.rect.center[1]],[randint(0,20)/10-1,-2],randint(2,15)])
        for particle in self.particles:
            particle[0][0] += particle[1][1]//3
            particle[0][1] += particle[1][0]//3
            particle[2] -= 0.5
            particle[1][1] -= 0.1
            if(int(particle[2]) > 0):
                # pygame.draw.circle(game,(255//(int(particle[2]*0.7)),255//(int(particle[2]*2)),255//(int(particle[2]*2))),[int(particle[0][0]),int(particle[0][1])],int(particle[2]))
                if(int(particle[2]) < 3):
                    pygame.draw.rect(pygame.display.get_surface(),(255//(int(particle[2]*10)),255//(int(particle[2]*10)),255//(int(particle[2]*10))),(int(particle[0][0]),int(particle[0][1]),int(particle[2]),int(particle[2])))
                elif(int(particle[2]) > 3):
                    pygame.draw.rect(pygame.display.get_surface(),(255//(int(particle[2])*0.5),255//(int(particle[2]*0.5)),255//(int(particle[2]*0.5))),(int(particle[0][0]),int(particle[0][1]),int(particle[2]),int(particle[2])))
            if(particle[2] <= 0):
                self.particles.remove(particle)

    def on_collide(self):
        self.drawExplosion()
        self.kill()

    def drawExplosion(self):
        n_explosions = 10
        for part in range(0,n_explosions):
            self.explosions.append([[self.rect.x,self.rect.center[1]],[randint(0,20)/10-1,-2],randint(2,50)])
        for particle in self.explosions:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][0]
            particle[2] -= 0.01
            particle[1][1] -= 0.3
            if(int(particle[2]*0.3) > 0):
                pygame.draw.circle(pygame.display.get_surface(),(255//(int(particle[2]*0.7)),255//(int(particle[2]*2)),255//(int(particle[2]*2))),[int(particle[0][0]),int(particle[0][1])],int(particle[2]))
                # pygame.draw.rect(pygame.display.get_surface(),(255//(int(particle[2]*3)),255//(int(particle[2]*2)),255//(int(particle[2]*2))),(int(particle[0][0]),int(particle[0][1]),int(particle[2]),int(particle[2])))
            if(particle[2] <= 0):
                self.explosions.remove(particle)
        

    def update(self):
        self.drawParticles()
        self.rect.x += self.vel
        if(self.rect.center[0] >= (1024-20)):
            self.kill()