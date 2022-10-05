import pygame

class Shoot(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y) -> None:
        super().__init__()
        self.image = pygame.Surface((10,3))
        self.image.fill((30,30,230))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.vel = 5
    def update(self):
        
        self.rect.x += self.vel
        # if(self.rect.center[0] >= (tela_largura-20)):
            # self.kill()