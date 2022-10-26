import os
import pygame

from classes.buff import Buff

class Power(pygame.sprite.Sprite):
    def __init__(self,xpos, ypos):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets","buffs","Buff_power.png"))
        self.tipe = 2
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.power = 1

    # def draw(self):
    #     pygame.display.get_surface().blit(self.buff_img,(self.rect.x,self.rect.y))

    def collide(self):
        self.kill()

    def update(self):
        self.rect.x -= 5
