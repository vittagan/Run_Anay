import pygame
import random


pygame.init()
clock = pygame.time.Clock()

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
    # user_x = 400
    # user_y = 350
    return user_x

def user2(user_height = 90):
    user_width = 60
    user_height = 90
    return user_width,user_height

def jump_user():

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        xx(500)

def xx(x=500):
    return x

def run_game():
    """"Основная функция игры"""

    while True:
        quit_game()
        jump_user()

        pygame.draw.rect(display_game(800, 600), ("Orange"),((xx(),100),user2()))    # Рисуем персонажа

        pygame.display.update()

        clock.tick(20)


run_game()
