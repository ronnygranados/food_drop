import pygame
from main import RED, GREEN, random_cell, CELL_SIZE, SCREEN


class Object:
    def __init__(self):
        self.red_surface = pygame.Surface((50, 50))
        self.red_surface.fill(RED)
        self.green_surface = pygame.Surface((50, 50))
        self.green_surface.fill(GREEN)

        self.x = random_cell * CELL_SIZE
        self.y = -100

        self.red_rect = self.red_surface.get_rect(center=(self.x, self.y))
        self.green_rect = self.green_surface.get_rect(center=(100, self.y))
        # self.pos = Vector2(self.x, self.y)

    def blit_shape(self):
        SCREEN.blit(self.red_surface, self.red_rect)
        SCREEN.blit(self.green_surface, self.green_rect)

    def fall_shape(self):
        self.red_rect.y += 2
        self.green_rect.y += 2
