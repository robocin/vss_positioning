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
