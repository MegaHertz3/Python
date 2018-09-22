import pygame
pygame.init()
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

WHITE = (0xFF, 0xFF, 0xFF)
 


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
    pygame.draw.line(screen, RED, [0, 00], [700, 500], 10) #diag cross topleft to b/r
    pygame.draw.line(screen, RED, [0, 500], [700, 0], 10) #diag cross b/l to top/right
    pygame.draw.line(screen, RED, [0, 250], [700, 250], 10) #horizontal
    pygame.draw.line(screen, RED, [350, 500], [350, 0], 10) #vertical
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
 
 