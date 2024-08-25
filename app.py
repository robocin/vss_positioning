import tkinter as tk

class Player:
    def __init__(self, canvas, cx, cy, size, color, number):
        self.canvas = canvas
        self.size = size
        self.color = color
        self.number = number
        self.angle = 0
        self.rect_id = self.create_rectangle(cx, cy)
        self.text_id = self.create_text(cx, cy)
        
        # Bind events
        self.canvas.tag_bind(self.rect_id, '<ButtonPress-1>', self.on_press)
        self.canvas.tag_bind(self.rect_id, '<B1-Motion>', self.on_motion)
    
    def create_rectangle(self, cx, cy):
        half_size = self.size / 2
        return self.canvas.create_rectangle(cx - half_size, cy - half_size, cx + half_size, cy + half_size, fill=self.color)
    
    def create_text(self, cx, cy):
        return self.canvas.create_text(cx, cy, text=self.number, fill='white', font=('Arial', 12, 'bold'))
    
    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
    
    def on_motion(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.update_position(dx, dy)
        self.start_x = event.x
        self.start_y = event.y
    
    def update_position(self, dx, dy):
        self.canvas.move(self.rect_id, dx, dy)
        self.canvas.move(self.text_id, dx, dy)
        self.canvas.update_entries()
    
    def set_angle(self, angle):
        self.angle = angle
        self.canvas.delete(self.rect_id)
        self.canvas.delete(self.text_id)
        cx, cy = self.get_coordinates()
        self.rect_id = self.create_rectangle(cx, cy)
        self.text_id = self.create_text(cx, cy)
        self.canvas.update_entries()
    
    def get_coordinates(self):
        x1, y1, x2, y2 = self.canvas.coords(self.rect_id)
        return int((x1 + x2) / 2), int((y1 + y2) / 2)

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
        self.create_line(400, 0, 400, 500, fill='white', width=2)
        
        # Draw the center circle
        self.create_oval(350, 200, 450, 300, outline='white', width=2)
        
        # Draw the goal areas
        self.create_rectangle(0, 175, 50, 325, outline='white', width=2)  # Left goal area
        self.create_rectangle(750, 175, 800, 325, outline='white', width=2)  # Right goal area
    
    def update_entries(self):
        for color, player in self.players.items():
            x, y = player.get_coordinates()
            angle = player.angle
            self.control_panel.update(color, x, y, angle)
            
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

class PlayersControlPanel(tk.Frame):
    def __init__(self, master, canvas):
        super().__init__(master)
        self.canvas = canvas
        self.pack(fill=tk.BOTH, expand=True)
        self.create_players_panels()

    def create_players_panels(self):
        for i, color in enumerate(["red", "green", "blue"]):
            player_panel = SinglePlayerControlPanel(self, color, i, self.canvas)
            player_panel.grid(row=0, column=i, padx=10, pady=5)
    
    def update(self, color, x, y, angle):
        for widget in self.winfo_children():
            if isinstance(widget, SinglePlayerControlPanel) and widget.color == color:
                widget.update_labels(widget.canvas.players[color].number, x, y, angle)

class ControPanel(tk.Frame):
    def __init__(self, master, canvas):
        super().__init__(master)
        self.canvas = canvas
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.players_panel = PlayersControlPanel(self, self.canvas)
    
    def update(self, color, x, y, angle):
        self.players_panel.update(color, x, y, angle)

def main():
    root = tk.Tk()
    root.title("VSS Positioning System")
    
    field = SoccerFieldCanvas(root, None, width=800, height=500)
    control_panel = PlayersControlPanel(root, field)
    field.control_panel = control_panel

    root.mainloop()

if __name__ == "__main__":
    main()
