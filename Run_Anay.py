import pygame
import random

pygame.init()
clock = pygame.time.Clock()
fps = 40                        # Скорость
x = 50                          # Х координата персонажа
y = 300                         # у координата персонажа
make_jump = False
jump_count = 30                 # Высота прыжка
count = 0                       # Счётчик анимации персонажа


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

def user2():
    """Размер персонажа"""
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
    if keys[pygame.K_z]:
        fps -= 5
    if keys[pygame.K_p]:
        pause()


def jump_user():
    """   Функция прыжка    """
    global y,make_jump,jump_count

    if jump_count >= -30:
        y -= jump_count /3
        jump_count -= 1
    else:
        jump_count = 30
        make_jump = False

def print_text(message, x, y, font_color=(0,0,0), font_style="Shrift.ttf", font_size=30):
    """
    Функция вывода текста на экран
    :param message: Текст сообщения
    :param x: Расположение на экране по Х
    :param y: Расположение на экране по Н
    :param font_color: Цвет текста
    :param font_style: Шрифт
    :param font_size: Размер текста
    :return:
    """
    font_style = pygame.font.Font(font_style,font_size)
    text = font_style.render(message,True,font_color)
    display_game(200,200).blit(text,(x,y))

def pause():
    pause = True
    while pause:
        for event in pygame.event.get():  # Выход на крестик
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()

        keys = pygame.key.get_pressed()  # Функция обработки нажатия клавиш
        print("pause!!!, чтобы продолжить нажми О")
        if keys[pygame.K_o]:  # o
            pause = False

        pygame.display.update()
        clock.tick(10)

def jump_start():
    """Запускает прыжок"""
    global make_jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        make_jump = True
    if make_jump:
        jump_user()


def user_anim():
    global count
    if count == 36:
        count = 0
    user_img = [pygame.image.load("anim/1.png"), pygame.image.load("anim/2.png"), pygame.image.load("anim/3.png"),
                 pygame.image.load("anim/4.png"), pygame.image.load("anim/5.png"), pygame.image.load("anim/6.png"),
                 pygame.image.load("anim/7.png"), pygame.image.load("anim/8.png"), pygame.image.load("anim/9.png"),
                 pygame.image.load("anim/10.png"), pygame.image.load("anim/11.png"), pygame.image.load("anim/12.png")]

    display_game(800, 600).blit(user_img[count // 3],((x,y),user2()))    # Рисуем персонажа
    count += 1

def run_game():
    """"Основная функция игры"""

    while True:
        global x,y,fps
        quit_game()
        key_user()
        jump_start()
        user_anim()
        pygame.display.update()
        clock.tick(fps)


run_game()
