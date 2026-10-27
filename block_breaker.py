import pygame
import random


pygame.init()

#DISPLAY
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Block Breaker")


#COLOURS
BLACK = (0,0,0)
RED = (255,0,0)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #BackGround        
    screen.fill(BLACK)
            
            
    pygame.draw.rect(screen,RED, (375,275,50,50))
    pygame.display.flip()


