import pygame
import random
import sys
import time

# Инициализация Pygame
pygame.init()

# Параметры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Кот ловит мышей")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Загрузка изображений
cat_img = pygame.image.load('mordacat.png')
mouse_img = pygame.image.load('mouse.png')

# Размеры изображений
cat_width, cat_height = cat_img.get_size()
mouse_width, mouse_height = mouse_img.get_size()

# Позиции кота
cat_x = screen_width // 2
cat_y = screen_height // 2
cat_speed = 1

# Время игры
game_time = int(input("Введите время игры в секундах: "))
start_time = time.time()

# Счетчик пойманных мышей
caught_mice = 0


# Генерация новой мыши в случайном месте
def generate_mouse():
    mouse_x = random.randint(0, screen_width - mouse_width)
    mouse_y = random.randint(0, screen_height - mouse_height)
    return mouse_x, mouse_y


mouse_x, mouse_y = generate_mouse()

# Основной игровой цикл
running = True
while running:
    screen.fill((0, 34, 0))

    # Проверка времени игры
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > game_time:
        running = False
        continue

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление котом
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cat_x -= cat_speed
    if keys[pygame.K_RIGHT]:
        cat_x += cat_speed
    if keys[pygame.K_UP]:
        cat_y -= cat_speed
    if keys[pygame.K_DOWN]:
        cat_y += cat_speed

    # Ограничение движения кота по границам экрана
    cat_x = max(0, min(cat_x, screen_width - cat_width))
    cat_y = max(0, min(cat_y, screen_height - cat_height))

    # Проверка столкновения с мышью
    if (cat_x < mouse_x + mouse_width and cat_x + cat_width > mouse_x and
        cat_y < mouse_y + mouse_height and cat_y + cat_height > mouse_y):
        caught_mice += 1
        mouse_x, mouse_y = generate_mouse()

    # Отображение кота и мыши
    screen.blit(cat_img, (cat_x, cat_y))
    screen.blit(mouse_img, (mouse_x, mouse_y))

    # Обновление экрана
    pygame.display.flip()

# Конец игры
print(f"Игра окончена! Вы поймали {caught_mice} мышей.")
pygame.quit()