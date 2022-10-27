import pygame

def clip(surface,x,y,x_size,y_size):
    handle_surface = surface.copy()
    clipR = pygame.Rect(x,y,x_size,y_size)
    handle_surface.set_clip(clipR)
    image = surface.subsurface(handle_surface.get_clip())
    return image.copy()


def troca_paleta(surface,old_c,new_c,obj):
    img_copy = pygame.Surface(obj.get_size())
    img_copy.fill(new_c)
    surface.set_colorkey(old_c)
    img_copy.blit(surface,(0,0))
    return img_copy
    

class Font():
    def __init__(self,path):
        self.spacing = 1
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        self.font_img = pygame.image.load(path).convert()
        current_char_width = 0
        x = 0
        self.characters = {}
        char_count = 0
        for x in range(self.font_img.get_width()):
            c = self.font_img.get_at((x,0))
            if c[0] == 127:
                char_img = clip(self.font_img,x - current_char_width,0,current_char_width,self.font_img.get_height())
                char_img = troca_paleta(char_img,(255,0,0),(255,255,255),char_img)
                char_img.set_colorkey((0, 0, 0))
                self.characters[self.character_order[char_count]] = char_img.copy()
                char_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def render(self,surf,text,loc):
        x_offset = 0
        for char in text :
            if char != ' ':
                surf.blit(self.characters[char],(loc[0]+ x_offset,loc[1]))
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing

    def clear(self,surface):
        handle_surface = surface.copy()
        clipR = pygame.Rect(0,0,0,0)
        handle_surface.set_clip(clipR)
        image = self.font_img.subsurface(handle_surface.get_clip())
        return image.copy()

