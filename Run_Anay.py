import pygame
import random


pygame.init()
clock = pygame.time.Clock()
fps = 10
x = 50
y = 50

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

def user(user_x=400):
    if user_x < 1000:
        user_x += 10
    else:
        user_x = 200
    return user_x

def user2(user_height = 90):
    user_width = 60
    user_height = 90
    return user_width,user_height

def jump_user():
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


def run_game():
    """"Основная функция игры"""

    while True:
        global x,y,fps
        quit_game()
        jump_user()

        pygame.draw.rect(display_game(800, 600), ("Orange"), ((100,50), user2()))    # Рисуем персонажа

        pygame.display.update()

        clock.tick(fps)


run_game()
