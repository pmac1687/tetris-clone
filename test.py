import pygame
import sys
p1 = 0
p2 = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((700, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 18)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    text = font.render("Score Player 1 = " + str(p1) + "Score Player 2 =" + str(p2) , 1, BLACK)
    screen.blit(text, (5, 10))
    pygame.display.update()

pygame.quit()
