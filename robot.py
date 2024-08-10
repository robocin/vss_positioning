import pygame
from constants import Colors

class Robot:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = Colors.WHITE
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def start_drag(self, pos):
        if self.rect.collidepoint(pos):
            self.dragging = True

    def drag(self, pos):
        if self.dragging:
            self.rect.topleft = (pos[0] - self.rect.width // 2, pos[1] - self.rect.height // 2)

    def stop_drag(self):
        self.dragging = False