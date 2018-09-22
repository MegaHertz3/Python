import pygame
pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("BOLLOCKS")

done = False

clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
    import pygame
    pygame.init()
    
    for i in range(10):
        print("x", end=" ")    
 
pygame.quit()
 
 