import time

import pygame
pygame.init()

windows_size = (800, 600)
screen = pygame.display.set_mode(windows_size)
pygame.display.set_caption('Тестовая игра')

image = pygame.image.load('mordacat.png')
image_rect = image.get_rect()

image_m = pygame.image.load('mouse.png')
image_m_rect = image_m.get_rect()

speed = 0.6

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - 19
            image_rect.y = mouseY - 17.5
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect.x += speed
    if keys[pygame.K_UP]:
        image_rect.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect.y += speed

    if image_rect.colliderect(image_m_rect):
        print('Котик скушал мышку')
        time.sleep(1)

    screen.fill((0, 34, 0))
    screen.blit(image, image_rect)
    screen.blit(image_m, image_m_rect)
    pygame.display.flip()


pygame.quit()
