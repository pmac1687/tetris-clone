import pygame


T2_img_1 =  pygame.image.load('blue_I.png')
T2_img_2 = pygame.image.load('blue_I_vert.png')


class Termino_1(pygame.sprite.Sprite):
    def __init__(self, x, y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image =  pygame.transform.scale(self.image , (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move = True
        self.speed = 2
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
        if self.move == True:
            self.rect.y += self.speed

class Boundry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('green.png')
        self.image =  pygame.transform.scale(self.image , (20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Termino_2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = T2_img_2
        self.image =  pygame.transform.scale(self.image , (75,25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move = True
        self.speed = 2
        self.spin = True
        self.spin_fps = 3
        self.angle = 90
        

    def update(self):
        self.get_rotate()


    def get_rotate(self):
        if self.spin == True:
            if self.spin_fps == 4:
                if self.image == T2_img_1 :
                    self.image = T2_img_2
                    self.image =  pygame.transform.scale(self.image , (75,25))
                elif self.image == T2_img_2:
                    self.image = T2_img_1 
                    self.image =  pygame.transform.scale(self.image , (75,25))
                    
                self.spin_fps = 0
            else:
                self.spin_fps += 1
        if self.move == True:
            self.rect.y += self.speed




if __name__ == "__main__":
    pass
    
