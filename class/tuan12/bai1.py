# import pygame , sys
# from pygame.locals import *
# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((720, 480))  #Tao do lon man hinh game
# pygame.display.set_caption('Hello world!')  #Tieu de game

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     DISPLAYSURF.fill((255, 255, 255))
#     pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (100, 80, 150, 50))
#     pygame.display.update()


# import pygame
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# background = pygame.Surface(screen.get_size())
# background.fill((255, 255, 255))
# rect = pygame.Rect(0, 0, 20, 20)
# clock = pygame.time.Clock()
# fps = clock.get_fps()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         rect.x += 1
#         if rect.x > 780:
#             rect.x = 0
#         screen.blit(background, (0, 0))
#         pygame.draw.rect(screen, (0, 0, 0), rect)
#         pygame.display.update()
#         time = clock.get_time()
# # Thêm một đối tượng text để hiển thị thời gian:

#     font = pygame.font.SysFont('Arial', 18)
#     text = font.render('Time taken: {} ms'.format(time), True, (0, 0, 0))
#     screen.blit(text, (0, 0))

#     font = pygame.font.SysFont('Arial', 18)
#     text = font.render('FPS: {}'.format(fps), True, (0, 0, 0))
#     screen.blit(text, (0, 20))


import pygame, sys
pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hello')

ball_image = pygame.image.load('assets/ball.png')
paddle_image = pygame.image.load('assets/paddle.png')

ball_x = screen_width / 2
ball_y = screen_height / 2

w_press = False
s_press = False
up_press = False
down_press = False

pygame.time.Clock()
fps = 60
loop = True
event = pygame.event.get()

while loop:
    event.get(pygame.K_p)