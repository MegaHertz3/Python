import pygame
import random
 
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

   

 
pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Mountain")

done = False

clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # so that we are done so the loop is exited
 
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
        

        
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
 
 
