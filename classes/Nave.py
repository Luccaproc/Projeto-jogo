from random import randint
import pygame
from classes.Shoot import Shoot

class Nave(pygame.sprite.Sprite):
    def __init__(self,tela_largura,tela_altura):
        super().__init__()
        self.image = pygame.Surface((50,25))
        self.image.fill((255,255,255))
        self.vida_atual = 200
        self.vida_maxima = 800
        self.tamanho_barra_vida = 400
        self.vida_ratio = (self.tamanho_barra_vida/self.vida_maxima)
        self.rect = self.image.get_rect(center = (tela_largura/2,tela_altura/2))
        #poder
        self.bullet_damage = 20
        self.bullet_speed = 10
        self.particles = []

    def drawParticles(self):
        if(self.alive()):
            self.particles.append([[self.rect.x,self.rect.center[1]],[randint(0,20)/10-1,-2],randint(4,15)])
            for particle in self.particles:
                particle[0][0] += particle[1][1] * 2
                particle[0][1] += particle[1][0]
                particle[2] -= 0.2
                particle[1][1] -= 0.3
                if(int(particle[2]*0.3) > 0):
                    # pygame.draw.circle(game,(255//(int(particle[2]*0.7)),255//(int(particle[2]*2)),255//(int(particle[2]*2))),[int(particle[0][0]),int(particle[0][1])],int(particle[2]))
                    pygame.draw.rect(pygame.display.get_surface(),(255//(int(particle[2]*0.3)),255//(int(particle[2]*0.6)),255//(int(particle[2]*2))),(int(particle[0][0]),int(particle[0][1]),int(particle[2]),int(particle[2])))
                if(particle[2] <= 0):
                    self.particles.remove(particle)

    def fire(self):
        return Shoot(self.rect.center[0],self.rect.center[1],self.bullet_damage,self.bullet_speed)
    
    def get_damage(self,quantidade):
        if(self.vida_atual >= quantidade):
            self.vida_atual -= quantidade
        else:
            self.kill()

    def barra_vida(self,game_surface,tela_largura):
        pygame.draw.rect(game_surface, (255,0,0), ((tela_largura/2)-300,10,(self.vida_atual*self.vida_ratio),10))
        pygame.draw.rect(game_surface, (255,255,255), ((tela_largura/2)-300,10,self.tamanho_barra_vida,10), 2)

    def update(self,surface,tela_largura,tela_altura,vel,width,height):
        self.barra_vida(surface,tela_largura)
        self.drawParticles()
        # self.rect.center = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
            if(self.rect.center[0] >= 0):
                self.rect.center = pygame.Vector2(self.rect.center[0]-vel,self.rect.center[1])
            else:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1])
        if keys[pygame.K_RIGHT]:
            if self.rect.center[0] <= (tela_largura)-width:
                self.rect.center = pygame.Vector2(self.rect.center[0]+vel,self.rect.center[1])
            else: 
                self.rect.center = pygame.Vector2((tela_largura)-width,self.rect.center[1])
        if keys[pygame.K_UP]:
            if self.rect.center[1] >= 0:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1]-vel)
            else:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1])
        if keys[pygame.K_DOWN]:
            if self.rect.center[1] <= (tela_altura)-height:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1]+vel)
            else:
                self.rect.center = pygame.Vector2(self.rect.center[0],self.rect.center[1])
