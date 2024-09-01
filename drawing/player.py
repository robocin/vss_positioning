class Player:
    def __init__(self, canvas, cx, cy, size, color, number, controller):
        self.canvas = canvas
        self.size = size
        self.color = color
        self.number = number
        self.angle = 0
        self.cx, self.cy = cx, cy
        self.controller = controller

    def draw(self):
        half_size = self.size / 2
        self.rect_id = self.canvas.create_rectangle(
            self.cx - half_size, self.cy - half_size,
            self.cx + half_size, self.cy + half_size, fill=self.color)
        self.text_id = self.canvas.create_text(
            self.cx, self.cy, text=self.number, fill='white',
            font=('Arial', 12, 'bold'))
        
        self.canvas.tag_bind(self.rect_id, '<ButtonPress-1>', self.on_press)
        self.canvas.tag_bind(self.rect_id, '<B1-Motion>', self.on_motion)

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
        self.cx += dx
        self.cy += dy
        self.canvas.move(self.rect_id, dx, dy)
        self.canvas.move(self.text_id, dx, dy)
        self.controller.update_player(self.color, self.cx, self.cy, self.angle)

    def get_coordinates(self):
        return self.cx, self.cy