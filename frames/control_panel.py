import tkinter as tk

from frames.general_control_panel import GeneralControlPanel
from frames.players_control_panel import PlayersControlPanel

class ControlPanel(tk.Frame):
    def __init__(self, master, canvas):
        super().__init__(master)
        self.canvas = canvas
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Add the dropdown menu for selecting the play type
        self.general_panel = GeneralControlPanel(self)
        self.general_panel.grid(row=0, column=0, pady=5, sticky="nsew")

        # Add the players control panel next to the dropdown
        self.players_panel = PlayersControlPanel(self, self.canvas)
        self.players_panel.grid(row=0, column=1, pady=5, sticky="nsew")

        # Configure the grid to make the widgets fill the space
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
    
    def update(self, color, x, y, angle):
        self.players_panel.update(color, x, y, angle)