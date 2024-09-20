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
        
        self.color_preview = tk.Label(vis_frame, text=str(self.id + 1), fg='white', font=('Arial', 12, 'bold'), bg=self.color, width=6, height=3)
        self.color_preview.pack()
        
        # Player control column
        ctrl_frame = tk.Frame(self)
        ctrl_frame.grid(row=0, column=1, pady=5)

        # Replace X control with Spinbox
        tk.Label(ctrl_frame, text="X:").grid(row=0, column=0)
        self.x_spinbox = tk.Spinbox(ctrl_frame, from_=-1000, to=1000, width=5, command=self.update_x_position)
        self.x_spinbox.grid(row=0, column=1, columnspan=3)

        # Replace Y control with Spinbox
        tk.Label(ctrl_frame, text="Y:").grid(row=1, column=0)
        self.y_spinbox = tk.Spinbox(ctrl_frame, from_=-1000, to=1000, width=5, command=self.update_y_position)
        self.y_spinbox.grid(row=1, column=1, columnspan=3)

        # Replace Angle control with Spinbox
        tk.Label(ctrl_frame, text="\u03B8:").grid(row=2, column=0)
        self.angle_spinbox = tk.Spinbox(ctrl_frame, from_=0, to=360, width=5, command=self.update_angle_position)
        self.angle_spinbox.grid(row=2, column=1, columnspan=3)

    def update_labels(self, number, x, y, angle):
        self.color_preview.config(bg=self.color)
        self.x_spinbox.delete(0, tk.END)
        self.x_spinbox.insert(0, str(x))
        self.y_spinbox.delete(0, tk.END)
        self.y_spinbox.insert(0, str(y))
        self.angle_spinbox.delete(0, tk.END)
        self.angle_spinbox.insert(0, str(angle))

    def update_position(self, dx, dy):
        player = self.canvas.players[self.color]
        player.update_position(dx, dy)
        x, y = player.get_coordinates()
        self.update_labels(player.number, x, y, player.angle)

    def update_x_position(self):
        x = int(self.x_spinbox.get())
        #original_x = (x * (2/5)) + 300
        current_x, _ = self.canvas.players[self.color].get_coordinates()
        #dx = original_x - current_x
        dx = x - current_x
        self.update_position(dx, 0)

    def update_y_position(self):
        y = int(self.y_spinbox.get())
        #original_y = -(y * (2/5)) + 260
        _, current_y = self.canvas.players[self.color].get_coordinates()
        #dy = original_y - current_y
        dy = y - current_y
        self.update_position(0, dy)

    def update_angle_position(self):
        angle = int(self.angle_spinbox.get())
        player = self.canvas.players[self.color]
        delta_angle = angle - player.angle
        player.set_angle(angle)
        self.update_labels(player.number, player.get_coordinates()[0], player.get_coordinates()[1], angle)
