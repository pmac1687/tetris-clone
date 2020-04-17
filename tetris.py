import pygame
import time
import terminoes

green_l = pygame.image.load('green_L.png')
T2_img_2 = pygame.image.load('blue_I_vert.png')

"""def check_collide():
    for i in all_sprites:
        if (i.rect.collidelist(boundries)) != -1:
            termino.speed = 0
            termino.rect.y = 500
            termino.spin = False
            create_new()"""

def create_new():
    for i in all_sprites:
        if i.speed == 0:
            #make termino condition so it doesnt call if statement again
            i.speed = 5
            i.move = False
            for b in all_sprites:
                if b not in boundries:
                    boundries.append(b)
                    new = b
                    all_sprites_2.add(new)
                    all_sprites.remove(b)
                    termino = terminoes.Termino_1(59,25,T2_img_2,boundries)
                    termino_group.append(termino)
                    all_sprites.add(termino)

def populate_boundry():
    boundry_lst = []
    x= 0
    y= 550
    for i in range(40):
        boundry_section = terminoes.Boundry(x,y)
        boundries.append(boundry_section)
        x += 10
    all_sprites_boundry.add(boundry_lst)
    #boundries.add(boundry_lst)
        

pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('title')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites_2 = pygame.sprite.Group()
all_sprites_boundry = pygame.sprite.Group()
termino_group = []
boundries = []
populate_boundry()
termino_1 = terminoes.Termino_1(925,625, green_l,boundries )
termino = terminoes.Termino_1(25,25, green_l,boundries )
termino_group.append(termino)
termino_group.append(termino)
all_sprites.add(termino)
all_sprites_2.add(termino_1)

running = True

while running:
    clock.tick(60)
    all_sprites.update()
    all_sprites_2.update()
    create_new()
    
    #check_collide()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
               for e in all_sprites:
                   if e.rect.x > 0 and e.rect.x < 380:
                       e.speed_vert += 5
            if event.key == pygame.K_LEFT:
               for e in all_sprites:
                   if e.rect.x > 0 and e.rect.x < 380:
                       e.speed_vert -= 5
            if event.key == pygame.K_DOWN:
                for i in all_sprites:
                   if i.move == True:
                       i.speed = 9
        
            if event.key == pygame.K_UP:
               for i in all_sprites:
                   if i.move == True:
                       i.image = pygame.transform.rotate(i.image, i.angle)
            if event.key == pygame.K_SPACE:
               for i in all_sprites:
                   if i.move == True:
                       i.image = pygame.transform.rotate(i.image, -i.angle)


        if event.type == pygame.KEYUP:

            if event.key == pygame.K_DOWN:
                for i in all_sprites:
                   if i.move == True:
                       i.speed = 2
            if event.key == pygame.K_RIGHT:
               for e in all_sprites:
                   if e.rect.x > 0 and e.rect.x < 380:
                       e.speed_vert -= 5
            if event.key == pygame.K_LEFT:
               for e in all_sprites:
                   if e.rect.x > 0 and e.rect.x < 380:
                       e.speed_vert += 5 
            

    screen.fill((255,0,0))
    all_sprites.draw(screen)
    all_sprites_2.draw(screen)
    all_sprites_boundry.draw(screen)

    #screen.blit
    #all sprite.draw

    pygame.display.update()
    pygame.display.flip()


pygame.quit()
