import pygame
pygame.init()

windows_size = (800, 600)
screen = pygame.display.set_mode(windows_size)
pygame.display.set_caption('Тестовая игра')

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    pygame.display.flip()


pygame.quit()
