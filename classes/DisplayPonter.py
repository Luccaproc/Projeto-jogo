import os
import pygame

from classes.Font import Font

class DisplayPointer(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        super().__init__()
        # self.image = pygame.Surface((96,32))
        self.image = pygame.image.load(os.path.join("assets","display","pointer.png"))
        self.image = pygame.transform.scale(self.image,(160,32))
        self.rect = self.image.get_rect()
        self.rect.centerx = xpos
        self.rect.top = ypos
        self.pontos = 0
        self.my_font_large = Font(os.path.join("assets","fonts","large_font.png"))

    def set_point(self,pontos):
        self.pontos = pontos
        # self.my_font_large.render(self.image,'',(30,10))
        self.my_font_large.render(self.image,str(pontos),(40,6))

    def update(self):
        print(self.pontos)
        # self.clear_point()
        self.set_point(self.pontos)