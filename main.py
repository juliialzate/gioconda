
import pygame, sys
pygame.init()

size = (564, 804)

red = (255, 0, 0)
white = (0, 0, 255)


screen = pygame.display.set_mode(size)
pygame.display.set_caption('El puzzle deslizante')


while True: 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(red)

    pygame.display.update()
