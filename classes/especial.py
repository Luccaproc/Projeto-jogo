import math
import pygame

from classes.Shoot import Shoot

class Especial(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,dano,velocidade,qtd):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.vel = velocidade
        self.dano = dano
        self.qtd = qtd
        self.bullets = []
        self.theta = 0
        self.spaw_timer = 50
        self.radius = 1

    def spawnBullets(self):
        anguloStep = 360/self.qtd
        angulo = 0

        for bullet in range(self.qtd):
            sen = math.sin((angulo * math.pi)/180)*self.radius
            cos = math.cos((angulo * math.pi)/180)*self.radius

            posicaoXbala = self.rect.centerx + sen
            posicaoYbala = self.rect.centery + cos

            vetorBala = pygame.Vector2(posicaoXbala,posicaoYbala)
            balaDirection = pygame.Vector2(vetorBala-self.rect.center).normalize() * self.vel

            bala = Shoot(self.rect.centerx,self.rect.centery,20,5,balaDirection,(255,255,32))

            angulo += anguloStep
            self.bullets.append(bala)

    def emitir(self):
        for bullet in self.bullets:
            bullet.update()
    # def rotate_bullet(self):

    def update(self) -> None:
        self.emitir()
        if(self.rect.centerx > (1024-20) or self.rect.centerx < 0):
            print('morreu')
            self.kill()
        if(self.rect.centery > (512-20) or self.rect.centery < 0):
            print('morreu')
            self.kill()
       
        self.theta += 0.1
        self.spaw_timer -= 1
