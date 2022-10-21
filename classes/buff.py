import pygame

class Buff(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.buff_img = None
        self.xpos = xpos
        self.ypos = ypos
        # self.rect.center[0] = xpos
        # self.rect.center[1] = ypos

    def draw(self):
        pygame.display.get_surface().blit(self.buff_img, (self.xpos,self.ypos))
    # def rederizar(self):
    #     self.rect.center[0] -= 5

    # def update(self):
    #     self.rederizar()