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
        options_frame = tk.Frame(self)
        options_frame.grid(row=0, column=0, pady=5, sticky="n")
        
        self.general_panel = GeneralControlPanel(options_frame)
        self.general_panel.grid(row=0, column=0, pady=5, sticky="n")
        
        # Add the players control panel next to the dropdown
        self.players_panel = PlayersControlPanel(self, self.canvas)
        self.players_panel.grid(row=0, column=1, pady=5, sticky="n")
    
    def update(self, color, x, y, angle):
        self.players_panel.update(color, x, y, angle)