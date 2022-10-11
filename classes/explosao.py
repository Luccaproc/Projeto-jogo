from random import randint
import pygame


import pygame

class Explosao(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.start_time = pygame.time.get_ticks()
        self.particles = []

    def emitir(self):
        if self.particles:
            self.delete_particles()
            seconds = (pygame.time.get_ticks() - self.start_time)//1000
            # if(seconds < 2):
                # self.particles.append([[self.rect.x,self.rect.y],[randint(-20,20)/10,-2],randint(4,30)])
            for particle in self.particles:
                particle[0][0] += particle[2][0]
                particle[0][1] += particle[2][1]
                particle[1] -= 0.5
                particle
                pygame.draw.circle(pygame.display.get_surface(),(255,255,255),[int(particle[0][0]),int(particle[0][1])],int(particle[1]))
                    # pygame.draw.rect(pygame.display.get_surface(),(255//(int(particle[2]*0.3)),255//(int(particle[2]*0.6)),255//(int(particle[2]*2))),(int(particle[0][0]),int(particle[0][1]),int(particle[2]),int(particle[2])))
            # else:
            #     self.kill()

    def adiciona_particulas(self,xpos,ypos):
        for i in range(0,20):
            radius = randint(4,30)
            direction_x = randint(-2,2)
            direction_y = randint(-2,2)
            particle_circle = [[xpos,ypos],radius,[direction_x,direction_y]]
            self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

    def update(self):
        self.emitir()
    