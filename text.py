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
    
    font = pygame.font.SysFont('Calibri', 25, True, False)

# Render the text. "True" means anti-aliased text.
# Black is the color. The variable BLACK was defined
# above as a list of [0, 0, 0]
# Note: This line creates an image of the letters,
# but does not put it on the screen yet.
    text = font.render("FUCK YOU",True,BLACK)
 
# Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])
    

  
    pygame.display.flip()


    clock.tick(60)

 
pygame.quit()
 
 