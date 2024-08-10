import pygame
from constants import Colors
from robot import Robot

class SoccerField:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.top_margin = 30
        self.robots = [
            Robot(100, 100, 50),
            Robot(200, 100, 50),
            Robot(100, 200, 50),
        ]

    def draw(self):
        field_height = self.height - self.top_margin - 100
        self.screen.fill(Colors.GREEN)  # Field color

        # Outer lines
        pygame.draw.rect(self.screen, Colors.WHITE, pygame.Rect(50, self.top_margin, self.width - 100, field_height - 30), 3)

        # Center circle
        pygame.draw.circle(self.screen, Colors.WHITE, (self.width // 2, self.top_margin + field_height // 2), 70, 3)
        pygame.draw.circle(self.screen, Colors.WHITE, (self.width // 2, self.top_margin + field_height // 2), 5)

        # Penalty boxes
        pygame.draw.rect(self.screen, Colors.WHITE, pygame.Rect(50, self.top_margin + field_height // 2 - 110, 100, 220), 3)
        pygame.draw.rect(self.screen, Colors.WHITE, pygame.Rect(self.width - 150, self.top_margin + field_height // 2 - 110, 100, 220), 3)

        # Goals
        pygame.draw.rect(self.screen, Colors.WHITE, pygame.Rect(50, self.top_margin + field_height // 2 - 60, 20, 120), 3)
        pygame.draw.rect(self.screen, Colors.WHITE, pygame.Rect(self.width - 70, self.top_margin + field_height // 2 - 60, 20, 120), 3)

        # Halfway line
        pygame.draw.line(self.screen, Colors.WHITE, (self.width // 2, self.top_margin), (self.width // 2, self.top_margin + field_height - 30), 3)

        # Draw robots
        for robot in self.robots:
            robot.draw(self.screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for robot in self.robots:
                robot.start_drag(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            for robot in self.robots:
                robot.drag(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            for robot in self.robots:
                robot.stop_drag()

    def update(self):
        for robot in self.robots:
            # Ensure robots do not overlap with the menu
            if robot.rect.bottom > self.height - 100:
                robot.rect.bottom = self.height - 100
            if robot.rect.top < self.top_margin:
                robot.rect.top = self.top_margin
            if robot.rect.left < 50:
                robot.rect.left = 50
            if robot.rect.right > self.width - 50:
                robot.rect.right = self.width - 50
