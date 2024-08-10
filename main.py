import pygame
import sys
from soccer_field import SoccerField
from menu import Menu
from constants import window

class SoccerGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((window.WIDTH, window.HEIGHT))
        pygame.display.set_caption("VSS positioning System")
        self.field = SoccerField(self.screen, window.WIDTH, window.HEIGHT)
        self.menu = Menu(self.screen, window.WIDTH, window.HEIGHT)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.field.handle_event(event)

            self.field.update()
            self.field.draw()
            self.menu.draw()
            pygame.display.flip()

if __name__ == "__main__":
    game = SoccerGame()
    game.run()