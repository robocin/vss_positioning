import tkinter as tk

from menus.formation_menu import FormationMenu
from menus.players_menu import PlayersMenu

class MainMenu(tk.Frame):
    def __init__(self, master, controller):     
        super().__init__(master)
        self.controller = controller
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.formation_menu = FormationMenu(self)
        self.formation_menu.grid(row=0, column=0, pady=5, sticky="nsew")

        self.players_panel = PlayersMenu(self, self.controller)
        self.players_panel.grid(row=0, column=1, pady=5, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def update_players_menu(self, color, x, y, angle):
        self.players_panel.update(color, x, y, angle)
    
    def is_attacking(self):
        return self.formation_menu.is_attacking()
    
    def get_play_type(self):
        return self.formation_menu.get_play_type()