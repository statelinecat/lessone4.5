
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
green = (0, 255, 0)

# Шрифты
font = pygame.font.Font(None, 36)

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
mouse_speed = 0.6

# Переменные игры
game_time = 0
start_time = 0
caught_mice = 0
input_active = True
game_active = False
user_input = ""

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

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                try:
                    game_time = int(user_input)
                    start_time = time.time()
                    input_active = False
                    game_active = True
                except ValueError:
                    user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    if game_active:
        # Проверка времени игры
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > game_time:
            game_active = False

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

        mouse_x += random.randint(-1, 1) * mouse_speed
        mouse_y += random.randint(-1, 1) * mouse_speed

        mouse_x = max(0, min(mouse_x, screen_width - mouse_width))
        mouse_y = max(0, min(mouse_y, screen_height - mouse_height))

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

        # Отображение оставшегося времени и пойманных мышей
        time_left = max(0, int(game_time - elapsed_time))
        time_text = font.render(f'Время: {time_left} сек', True, white)
        screen.blit(time_text, (10, 10))

        mouse_text = font.render(f'Поймано мышей: {caught_mice} ', True, white)
        screen.blit(mouse_text, (500, 10))

    elif not game_active and not input_active:
        result_text = font.render(f'Игра окончена! Вы поймали {caught_mice} мышей.', True, white)
        screen.blit(result_text, (
        screen_width // 2 - result_text.get_width() // 2, screen_height // 2 - result_text.get_height() // 2))

    else:
        instruction_text = font.render('Введите время игры в секундах и нажмите Enter:', True, white)
        screen.blit(instruction_text, (10, 10))
        user_input_text = font.render(user_input, True, green)
        screen.blit(user_input_text, (10, 50))

        # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()