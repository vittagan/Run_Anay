import pygame
import random

pygame.init()
clock = pygame.time.Clock()
fps = 40
x = 50
y = 300
make_jump = False
jump_count = 30

def display_game(width, height, title='Аня убегай!!!'):
    """Функция размера дисплея, цвета, icon и заголовкq"""
    pygame.display.set_caption(title, 'Hello')  # Устанавливаем заголовок
    display = pygame.display.set_mode((width, height))  # размер дисплея
    icon = pygame.image.load('Png/Dino.png')  # Загружаем иконку окна
    pygame.display.set_icon(icon)  # Устанавливает иконку окна
    display.fill("PaleTurquoise")  # Заливаем фон игры
    return display

def quit_game():
    """выход из игры"""
    for event in pygame.event.get():  # Выход на крестик
        if event.type == pygame.QUIT:
            pygame.QUIT
            quit()
    keys = pygame.key.get_pressed()  # Функция обработки нажатия клавиш
    if keys[pygame.K_ESCAPE]:  # Пробел
        quit()


def user2(user_height = 90):
    user_width = 60
    user_height = 90
    return user_width,user_height

def key_user():
    global x,y,fps
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 3
    if keys[pygame.K_s]:
        y += 3
    if keys[pygame.K_a]:
        x -= 3
    if keys[pygame.K_d]:
        x += 3
    if keys[pygame.K_q]:
        fps += 5


def jump_user():
    """   Функция прыжка    """
    global y,make_jump,jump_count

    if jump_count >= -30:
        y -= jump_count /3
        jump_count -= 1
    else:
        jump_count = 30
        make_jump = False

def jump_start():
    global make_jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        make_jump = True
    if make_jump:
        jump_user()

def run_game():
    """"Основная функция игры"""

    while True:
        global x,y,fps,make_jump
        quit_game()
        key_user()
        jump_start()
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     make_jump = True
        # if make_jump:
        #     jump_user()
        pygame.draw.rect(display_game(800, 600), ("Orange"), ((x,y), user2()))    # Рисуем персонажа


        pygame.display.update()
        clock.tick(fps)


run_game()
