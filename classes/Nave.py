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
    
    def fire(self):
        return Shoot(self.rect.center[0],self.rect.center[1])
    
    # def get_damage(self,quantidade):
    #     if(self.vida_atual >= quantidade):
    #         self.vida_atual -= quantidade
    #     else:
    #         self.kill()

    def barra_vida(self,game_surface,tela_largura):
        pygame.draw.rect(game_surface, (255,0,0), ((tela_largura/2)-300,10,self.vida_atual,10))
        pygame.draw.rect(game_surface, (255,255,255), ((tela_largura/2)-300,10,self.tamanho_barra_vida,10), 2)

    def update(self,surface,tela_largura,tela_altura,vel,width,height):
        self.barra_vida(surface,tela_largura)
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
