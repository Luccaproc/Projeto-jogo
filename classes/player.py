import os
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,player_image):
        super().__init__()
        self.image = pygame.image.load(player_image)
        self.player_img = pygame.image.load(os.path.join("assets","player","cabine.png"))
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (160,96))
        self.persona = pygame.mask.from_surface(self.player_img)
        self.person = pygame.transform.scale(self.player_img, (160,96))

        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

        # self.play_rect = self.player_img.get_rect()
        # self.play_rect.x = 10
        # self.play_rect.y = 10

    def update(self):
        pygame.display.get_surface().blit(self.person,(10,10))