import tkinter as tk
from drawing.player import Player

class SoccerFieldCanvas(tk.Canvas):
    def __init__(self, master, controller):
        super().__init__(master, width=600, height=520, bg='green')
        self.controller = controller
        self.pack()
        
        self.create_field_markings()
        
        self.players = {
            "red": Player(self, 100, 150, 30, 'red', 1, self.controller),
            "green": Player(self, 300, 150, 30, 'green', 2, self.controller),
            "blue": Player(self, 500, 150, 30, 'blue', 3, self.controller)
        }

        self.draw_players()

    def create_field_markings(self):
        self.create_line(300, 0, 300, 520, fill='white', width=2)
        
        # Draw the center circle
        self.create_oval(221, 181, 379, 339, outline='white', width=2)
        
        # Draw the goal areas
        self.create_rectangle(0, 120, 60, 400, outline='white', width=2)  # Left goal area
        self.create_rectangle(540, 120, 600, 400, outline='white', width=2)  # Right goal area

        # Draw the 6 field marks

        ## Top Left
        self.create_line(150, 92, 150, 108, fill='white', width=2)
        self.create_line(142, 100, 158, 100, fill='white', width=2)

        ## Mid Left
        self.create_line(150, 252, 150, 268, fill='white', width=2)
        self.create_line(142, 260, 158, 260, fill='white', width=2)

        ## Bottom Left
        self.create_line(150, 412, 150, 428, fill='white', width=2)
        self.create_line(142, 420, 158, 420, fill='white', width=2)

        ## Top Right
        self.create_line(450, 92, 450, 108, fill='white', width=2)
        self.create_line(442, 100, 458, 100, fill='white', width=2)

        ## Mid Right
        self.create_line(450, 252, 450, 268, fill='white', width=2)
        self.create_line(442, 260, 458, 260, fill='white', width=2)

        ## Bottom Right
        self.create_line(450, 412, 450, 428, fill='white', width=2)
        self.create_line(442, 420, 458, 420, fill='white', width=2)
 
    def draw_players(self):
        for player in self.players.values():
            player.draw()

    # def update_entries(self):
    #     for color, player in self.players.items():
    #         x, y = player.get_coordinates()
    #         angle = player.angle
    #         self.controller.update_player(color, (x-300)*5/2, -(y-260)*5/2, angle)
