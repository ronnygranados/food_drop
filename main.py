import pygame
import sys
import random
from object import Object
# from pygame.math import Vector2

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 500
FPS = 60
TITLE = 'FOOD DROP'
SIZE = 190
CELL_SIZE = 50
CELL_NUMBER = 8

random_cell = random.randint(1, CELL_NUMBER - 1)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE_SKY = (152, 166, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (204, 255, 209)

# Display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Surfaces
floor_surface = pygame.Surface((WIDTH, 100))
floor_surface.fill(BLUE_SKY)
floor_rect = floor_surface.get_rect(midbottom=(200, 500))

# Images
LOAD_DITTO = pygame.image.load('Graphics/ditto.png')
DITTO = pygame.transform.scale(LOAD_DITTO, (SIZE, SIZE))

# Time
CLOCK = pygame.time.Clock()


class Figure:

    def draw_figure(self, mouse_x):
        SCREEN.blit(DITTO, (mouse_x - 90, 330))


class Main:
    def __init__(self):
        self.object = Object()

    def check_figures(self):
        pass


# Game loop

SCREEN_UPDATE = pygame.USEREVENT
figure = Figure()
object_class = Object()

running = True
while running:
    CLOCK.tick(FPS)
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(LIGHT_GREEN)
    SCREEN.blit(floor_surface, floor_rect)
    figure.draw_figure(mx)
    object_class.blit_shape()
    object_class.fall_shape()
    pygame.display.update()
