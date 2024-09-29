import tkinter as tk
import math

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
    
    def create_polygon(self, points):
        return self.canvas.create_polygon(points, fill=self.color, outline='black', width=1)

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
        cx, cy = self.get_coordinates()
        self.canvas.delete(self.rect_id)
        self.canvas.delete(self.text_id)
        
        rotated_coordinates = self.calc_rotated_coords(cx, cy, angle)

        self.rect_id = self.create_polygon(rotated_coordinates)
        self.text_id = self.create_text(cx, cy)

        # Atualiza os bindings para o novo polígono
        self.canvas.tag_bind(self.rect_id, '<ButtonPress-1>', self.on_press)
        self.canvas.tag_bind(self.rect_id, '<B1-Motion>', self.on_motion)

        self.canvas.update_entries()

    def calc_rotated_coords(self, cx, cy, angle):
        half_size = self.size / 2
        theta = math.radians(angle)

        x1, y1 = cx - half_size, cy - half_size
        x2, y2 = cx + half_size, cy - half_size
        x3, y3 = cx + half_size, cy + half_size
        x4, y4 = cx - half_size, cy + half_size

        rotated_coordinates = [
            (cx + (x1 - cx) * math.cos(theta) - (y1 - cy) * math.sin(theta),
            cy + (x1 - cx) * math.sin(theta) + (y1 - cy) * math.cos(theta)),

            (cx + (x2 - cx) * math.cos(theta) - (y2 - cy) * math.sin(theta),
            cy + (x2 - cx) * math.sin(theta) + (y2 - cy) * math.cos(theta)),

            (cx + (x3 - cx) * math.cos(theta) - (y3 - cy) * math.sin(theta),
            cy + (x3 - cx) * math.sin(theta) + (y3 - cy) * math.cos(theta)),

            (cx + (x4 - cx) * math.cos(theta) - (y4 - cy) * math.sin(theta),
            cy + (x4 - cx) * math.sin(theta) + (y4 - cy) * math.cos(theta))
        ]

        return rotated_coordinates
    
    def get_coordinates(self):
        coords = self.canvas.coords(self.rect_id)

        x_sum = sum(coords[i] for i in range(0, len(coords), 2))
        y_sum = sum(coords[i] for i in range(1, len(coords), 2))
        n = len(coords) // 2

        return int(x_sum / n), int(y_sum / n)