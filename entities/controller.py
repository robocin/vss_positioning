from drawing.soccer_field import SoccerFieldCanvas
from menus.main_menu import MainMenu

class Controller:
    def __init__(self, root):
        self.canvas = SoccerFieldCanvas(root, self)
        self.menu = MainMenu(root, self)
    
    def update_players_menu(self, color, x, y, angle):
        self.menu.update_players_menu(color, x, y, angle)

    def load_default_formations():
        