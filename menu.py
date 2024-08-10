import pygame
from constants import Colors

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.menu_height = 100

    def draw(self):
        pygame.draw.rect(self.screen, Colors.DARK_GRAY, pygame.Rect(0, self.height - self.menu_height, self.width, self.menu_height))
