import json
import tkinter as tk
from drawing.soccer_field import SoccerFieldCanvas
from menus.main_menu import MainMenu

class Controller:
    def __init__(self, root):
        self.canvas = SoccerFieldCanvas(root, self)
        self.menu = MainMenu(root, self)
        
        # Load default formation
        self.load_default_positions()

    def update_players_menu(self, color, x, y, angle):
        self.menu.update_players_menu(color, x, y, angle)

    def load_default_positions(self):
        # Load positions from the JSON file
        try:
            with open('default_positions.py', 'r') as file:
                formations = json.load(file)

                formation_name =  self.menu.get_play_type() + "_" + ("A" if self.menu.is_attacking() else "D")

                # Assuming 'default' formation is to be loaded initially
                current_formation = formations.get(formation_name, [])
            
            for player in current_formation:
                color = player['color']
                x = player['x']
                y = player['y']
                angle = player['angle']
                
                # Update the canvas and menu with the formation data
                self.canvas.players[color].update_position(x, y)
                # self.canvas.players[color].set_angle(angle)
                self.update_players_menu(color, x, y, angle)

        except FileNotFoundError:
            print("default_positions.json file not found.")
        except json.JSONDecodeError:
            print("Error decoding the default_positions.json file.")