import tkinter as tk
from canvas.player import Player

class SoccerFieldCanvas(tk.Canvas):
    def __init__(self, master, control_panel, **kwargs):
        super().__init__(master, **kwargs)
        self.control_panel = control_panel
        self.pack()
        
        # Set the background color to green
        self.configure(bg='green')
        
        # Draw the field markings
        self.create_field_markings()
        
        # Create player instances
        self.players = {
            "red": Player(self, 100, 150, 30, 'red', 1),
            "green": Player(self, 300, 150, 30, 'green', 2),
            "blue": Player(self, 500, 150, 30, 'blue', 3)
        }
    
    def create_field_markings(self):
        # Draw the center line
        self.create_line(300, 0, 300, 520, fill='white', width=2)
        
        # Draw the center circle
        self.create_oval(221, 181, 379, 339, outline='white', width=2)
        
        # Draw the goal areas
        self.create_rectangle(0, 120, 60, 400, outline='white', width=2)  # Left goal area
        self.create_rectangle(540, 120, 600, 400, outline='white', width=2)  # Right goal area
    
    def update_entries(self):
        for color, player in self.players.items():
            x, y = player.get_coordinates()
            angle = player.angle
            self.control_panel.update(color, x, y, angle)
   