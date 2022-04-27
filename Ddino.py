import pygame
import random

pygame.init()

color_display = 175, 238, 238

pygame.display.set_caption("Аня убегай!!!")

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width,display_height))
icon = pygame.image.load('Png/Dino.png')

pygame.display.set_icon(icon)

cactus_img = [pygame.image.load("Png/Rukzak.png"),pygame.image.load("Png/Gorshok.png"),pygame.image.load("Png/Styl.png")]
cactus_opt = [40,430,60,430,50,450]

stone_img = [pygame.image.load("Png/Stone.png"),pygame.image.load("Png/Stone2.png")]
cloud_img = [pygame.image.load("Png/Cloud.png"),pygame.image.load("Png/Cloud1.png")]
class Object:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        # self.height = height
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= - self.width:
            display.blit (self.image,(self.x,self.y))                              # Картинка кактуса
            # pygame.draw.rect(display, (46, 139, 87), (self.x, self.y, self.width, self.height))     #Рисуем кактус
            self.x -= self.speed
            return True
        else:
            # self.x = display_width + 100 + random.randrange(-80,+60)
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))


user_width = 60
user_height = 30
user_x = display_width // 3
user_y = display_height - user_width - 100

cactus_width = 20
cactus_height = 60
cactus_x = display_width -100
cactus_y = user_y

make_jump = False
clock = pygame.time.Clock()
jump_counter = 30


def run_game():
    """Основная функция, запуска игры"""
    game = True
    global make_jump
    cactus_arr = []
    create_cactus_arr(cactus_arr)
    land = pygame.image.load('Png/Fon.png')     #Фон игры

    stone, cloud = open_random_objects()

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()

        # display.fill((255, 69, 0))            #Заливаем фон игры
        display.blit(land,(0,0))              #Прорисовываем фон игры
        draw_array(cactus_arr)
        move_objects(stone,cloud)
        pygame.draw.rect(display, (255, 69, 0),(user_x, user_y, user_height, user_width))    # Рисуем персонажа
        pygame.display.update()
        clock.tick(80)


def jump():
    """
    Функция прыжка
    """
    global user_y,make_jump, jump_counter
    if jump_counter >= -30:
        user_y -= jump_counter /3
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def create_cactus_arr(array):
    """Создаёт 3 кактуса"""
    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_opt[choice * 2]
    height = cactus_opt[choice * 2 + 1]
    array.append(Object(display_width + 20,height,width,img,4))

    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_opt[choice * 2]
    height = cactus_opt[choice * 2 + 1]
    array.append(Object(display_width + 300,height,width,img,4))

    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_opt[choice * 2]
    height = cactus_opt[choice * 2 + 1]
    array.append(Object(display_width + 600,height,width,img,4))


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice ==0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)

    return radius




def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            radius = find_radius(array)

            choice = random.randrange(0, 3)
            img = cactus_img[choice]
            width = cactus_opt[choice * 2]
            height = cactus_opt[choice * 2 + 1]

            cactus.return_self(radius,height,width,img)

def open_random_objects():
    choice = random.randrange(0,2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0,2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width,display_height - 80,10, img_of_stone,4)
    cloud = Object(display_width,80,70, img_of_cloud,1)

    return stone,cloud

def move_objects(stone, cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width, 500 + random.randrange(10, 60), stone.width, img_of_stone)

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width, random.randrange(10, 200), cloud.width, img_of_cloud)
run_game()