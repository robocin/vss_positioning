from drawing.soccer_field import SoccerFieldCanvas
from menus.main_menu import MainMenu

class Controller:
    def __init__(self, root):
        self.canvas = SoccerFieldCanvas(root, self)
        self.menu = MainMenu(root, self)
    
    def update_player(self, color, x, y, angle):
        self.menu.update(color, x, y, angle)