import tkinter as tk
from frames.single_player_control_panel import SinglePlayerControlPanel

class PlayersControlPanel(tk.Frame):
    def __init__(self, master, canvas):
        super().__init__(master)
        self.canvas = canvas
        self.create_players_panels()

    def create_players_panels(self):
        for i, color in enumerate(["red", "green", "blue"]):
            player_panel = SinglePlayerControlPanel(self, color, i, self.canvas)
            player_panel.grid(row=0, column=i, padx=10, pady=5)
    
    def update(self, color, x, y, angle):
        for widget in self.winfo_children():
            if isinstance(widget, SinglePlayerControlPanel) and widget.color == color:
                widget.update_labels(widget.canvas.players[color].number, x, y, angle)
