import tkinter as tk

class SinglePlayerControlPanel(tk.Frame):
    def __init__(self, parent, color, id, canvas):
        super().__init__(parent)
        self.color = color
        self.canvas = canvas
        self.id = id
        self.create_widgets()

    def create_widgets(self):
        # Player visualization column
        vis_frame = tk.Frame(self)
        vis_frame.grid(row=0, column=0, padx=5, pady=5)
        
        self.color_preview = tk.Label(vis_frame, text=str(self.id + 1), fg='white', font=('Arial', 12, 'bold'), bg=self.color, width=10, height=5)
        self.color_preview.pack()
        
        # Player control column
        ctrl_frame = tk.Frame(self)
        ctrl_frame.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(ctrl_frame, text="X:").grid(row=0, column=0)
        self.x_label = tk.Label(ctrl_frame, text="0", width=5)
        self.x_label.grid(row=0, column=1)
        tk.Button(ctrl_frame, text="-", command=lambda: self.update_position(-1, 0)).grid(row=0, column=2)
        tk.Button(ctrl_frame, text="+", command=lambda: self.update_position(1, 0)).grid(row=0, column=3)
        
        tk.Label(ctrl_frame, text="Y:").grid(row=1, column=0)
        self.y_label = tk.Label(ctrl_frame, text="0", width=5)
        self.y_label.grid(row=1, column=1)
        tk.Button(ctrl_frame, text="-", command=lambda: self.update_position(0, -1)).grid(row=1, column=2)
        tk.Button(ctrl_frame, text="+", command=lambda: self.update_position(0, 1)).grid(row=1, column=3)
        
        tk.Label(ctrl_frame, text="Angle:").grid(row=2, column=0)
        self.angle_label = tk.Label(ctrl_frame, text="0", width=5)
        self.angle_label.grid(row=2, column=1)
        tk.Button(ctrl_frame, text="-", command=lambda: self.update_angle(-10)).grid(row=2, column=2)
        tk.Button(ctrl_frame, text="+", command=lambda: self.update_angle(10)).grid(row=2, column=3)
    
    def update_labels(self, number, x, y, angle):
        self.color_preview.config(bg=self.color)
        self.x_label.config(text=x)
        self.y_label.config(text=y)
        self.angle_label.config(text=angle)
    
    def update_position(self, dx, dy):
        player = self.canvas.players[self.color]
        player.update_position(dx, dy)
        x, y = player.get_coordinates()
        self.update_labels(player.number, x, y, player.angle)
    
    def update_angle(self, delta_angle):
        player = self.canvas.players[self.color]
        new_angle = (player.angle + delta_angle) % 360
        player.set_angle(new_angle)
        x, y = player.get_coordinates()
        self.update_labels(player.number, x, y, new_angle)
