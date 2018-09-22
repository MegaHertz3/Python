import pygame
import math
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("GAME")

done = False

clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
 
    screen.fill(WHITE)
    
    for i in range(200):
     
        radians_x = i / 20
        radians_y = i / 6
     
        x = int( 75 * math.sin(radians_x)) + 200
        y = int( 75 * math.cos(radians_y)) + 200
     
        pygame.draw.line(screen, GREEN, [x,y], [x+10,y], 10)    
 
        pygame.display.flip()
 
        clock.tick(60)
 
pygame.quit()
 
 