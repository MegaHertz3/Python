import pygame
pygame.init()
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        print("User asked to quit.")
    elif event.type == pygame.KEYDOWN:
        print("User pressed a key.")
    elif event.type == pygame.KEYUP:
        print("User let go of a key.")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print("User pressed a mouse button")
