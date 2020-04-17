import pygame



T2_img_1 =  pygame.image.load('blue_I.png')
T2_img_2 = pygame.image.load('blue_I_vert.png')


class Termino_1(pygame.sprite.Sprite):
    def __init__(self, x, y,img,boundries):
        pygame.sprite.Sprite.__init__(self)
        self.boundries = boundries
        self.image = img
        self.image =  pygame.transform.scale(self.image , (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move = True
        self.speed = 2
        self.speed_vert = 0
        self.spin = True
        self.spin_fps = 4
        self.angle = 90
        

    def update(self):
        """if self.spin == True:
            if self.spin_fps == 4:
                self.image = pygame.image.load(self.img)
                self.image =  pygame.transform.scale(self.image , (30,30))
                self.image = pygame.transform.rotate(self.image, self.angle)
                self.spin_fps = 0
                self.angle += 90
            else:
                self.spin_fps += 1"""
        if self.rect.x < 0 or self.rect.x > 380:
            self.speed_vert = 0
        if self.move == True:
            self.rect.y += self.speed
            self.rect.x += self.speed_vert
            if (self.rect.collidelist(self.boundries)) != -1  :
                self.speed = 0
                self.rect.y -= 1
                self.spin = False
                self.move = False
        """ if len(self.all_sprites) > 0:
                if(self.rect.collidelist(self.all_sprites)) != -1:
                    self.speed = 0
                    self.rect.y = 500
                    self.spin = False
                    self.move = False"""

    
class Boundry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('green.png')
        self.image =  pygame.transform.scale(self.image , (20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        

   



if __name__ == "__main__":
    pass
    
