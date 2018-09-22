import pygame.random
pygame.init()
clock = pygame.time.Clock()
WIDTH=600; HEIGHT=600; BLACK=(0,0,0)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
screen.fill(BLACK)

def draw_circle(colour):
    x=random.randint(1, WIDTH)
    y=random.randint(1, HEIGHT)
    size=random.randint(1, 5)
    pygame.draw.circle(screen, colour, (x, y), size)

def random_colour(minimum, maximum):
    red=random.randint(minimum, maximum)
    green=random.randint(minimum, maximum)
    blue=random.randint(minimum, maximum)
    colour=[red,green,blue]
    return colour

for n in range in range(100):
    clock.tick(25)
    colour=random_colour(100, 255)
    draw_circle(colour)
    pygame.display.update()

raw_input("press a key")


    
