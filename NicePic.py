import pygame
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (150, 102, 54)
YELLOW = (255, 208, 0)
 
PI = 3.141592653
 
# Set the height and width of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My first game")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True #make done true so the loop is exited
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    screen.fill(BLUE)

    pygame.draw.ellipse(screen, GREEN, [-100,420,1000,300],)#floor
    
    for y_offset in range(0, 1800, 540):
        pygame.draw.rect(screen, BROWN, [50+y_offset,380,30,100],) #tree trunks

    for y_offset in range(0, 1800, 540):
        pygame.draw.ellipse(screen, GREEN, [20+y_offset,310,90,80],) #tree bushes
    pygame.draw.rect(screen, RED, [200,250,260,220],) #house
    pygame.draw.polygon(screen, BROWN, [[330,150], [480,250], [180,250]],) #roof
    pygame.draw.ellipse(screen, YELLOW, [40,40,90,90],) #sun

    for y_offset in range(0,250,125):
        pygame.draw.rect(screen, WHITE, [230 + y_offset, 275, 70, 70],) #Top Windows
    pygame.draw.rect(screen, WHITE, [230, 370, 70, 70],) #Bottom window
    pygame.draw.rect(screen, BLACK, [420 , 469, -50, -60]) #door
    pygame.draw.ellipse(screen, BLACK, [369, 388, 53, 50],) #door top
    pygame.draw.ellipse(screen, BROWN, [405, 425, 9, 9],) #door nob

    for y_offset in range(0,440,110):
        pygame.draw.ellipse(screen, WHITE, [250 + y_offset, -65, 170, 135],) #clouds

    #Add rainbow and shading to cloud, annother overlap with darker colour
    pygame.display.flip()
    
    clock.tick(60)
 
pygame.quit()
