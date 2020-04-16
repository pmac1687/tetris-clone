import pygame
import time
import terminoes

green_l = pygame.image.load('green_L.png')

def check_collide():
    for i in termino_group:
        if (i.rect.collidelist(boundries)) != -1:
            termino.speed = 0
            termino.rect.y = 500
            termino.spin = False
            termino_group = termino_group.remove(i)
            create_new()

def create_new():
    termino = terminoes.Termino_2(55,25)
    all_sprites.add(termino)

def populate_boundry():
    boundry_lst = []
    x= 0
    y= 550
    for i in range(10):
        boundry_section = terminoes.Boundry(x,y)
        boundries.append(boundry_section)
        x += 20
    all_sprites.add(boundry_lst)
    #boundries.add(boundry_lst)
        

pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('title')

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
termino_group = []
boundries = []
populate_boundry()
termino = terminoes.Termino_1(25,25, green_l )
termino_group.append(termino)
all_sprites.add(termino)

running = True

while running:
    clock.tick(60)
    all_sprites.update()
    check_collide()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               pass
            if event.key == pygame.K_DOWN:
                pass
        if event.type == pygame.KEYUP:
            pass
            

    screen.fill((255,0,0))
    all_sprites.draw(screen)

    #screen.blit
    #all sprite.draw

    pygame.display.update()
    pygame.display.flip()


pygame.quit()
