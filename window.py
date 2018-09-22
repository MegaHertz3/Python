import pygame
pygame.init()

# Loop until the user clicks the close button.
done = False

size = (700, 500)
screen = pygame.display.set_mode(size)

WHITE = (0xFF, 0x1F, 0x11)

pygame.display.set_caption("BSKYB project Overlord")
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
    `pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
pygame.quit()