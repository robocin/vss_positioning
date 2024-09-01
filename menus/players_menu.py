import tkinter as tk
from menus.single_player_menu import SinglePlayerMenu

class PlayersMenu(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller  # Use the controller to access the canvas and players
        self.create_players_panels()

    def create_players_panels(self):
        for i, color in enumerate(["red", "green", "blue"]):
            player_panel = SinglePlayerMenu(self, color, i, self.controller.canvas)
            player_panel.grid(row=0, column=i, padx=10, pady=5)
    
    def update(self, color, x, y, angle):
        # Access the players from the controller's canvas
        for widget in self.winfo_children():
            if isinstance(widget, SinglePlayerMenu) and widget.color == color:
                player = self.controller.canvas.players[color]
                widget.update_labels(player.number, x, y, angle)
