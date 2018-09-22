import pygame
import random
 
# Define some colors
BLACK    = (   0,   0,   0)
GREY     = (128, 128, 128)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
GREEND   = (0, 200, 51)
GREENDD  = (51, 102, 0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   100, 255)
BROWN    = (102, 51, 0)
YELLOW   = (252, 252, 6)

PI = 3.141592653

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()    

 
pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("BOOBARENA")

done = False

clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
 
    screen.fill(BLUE)
    #sun
    pygame.draw.circle(screen,YELLOW,(55, 58), 50, 0)
    
    #moutain
    pygame.draw.polygon(screen, GREY,[[650,80], [400,600], [900,600]])
    pygame.draw.polygon(screen, WHITE,[[650,80], [625,130], [675,130]])
     
    #Hills                                                         
    pygame.draw.circle(screen,GREENDD,(500, 1550), 1200, 0)
    pygame.draw.circle(screen,GREEND,(10, 1500), 1200, 0)
    
    #multiple tree tops
    for y_offset in range(0, 400, 135):
        pygame.draw.circle(screen,GREEN,(30+y_offset, 200), 75, 0)
    #Trunks
    for y_offset in range(0, 400, 135): 
        pygame.draw.line(screen,BROWN,[30+y_offset,350],[30+y_offset,275],20)
        
        # This is a list of 'sprites.' Each block in the program is
        # added to this list. The list is managed by a class called 'Group.'
    block_list = pygame.sprite.Group()
         
        # This is a list of every sprite. 
        # All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()
         
    for i in range(50):
            # This represents a block
        block = Block(WHITE, 4, 4)#snow size
         
            # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(screen_height)
         
            # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)  
        
    all_sprites_list.draw(screen)
        
    pygame.display.flip()
    
    clock.tick(10)#increase to speed up snow fall
 
pygame.quit()
 
 