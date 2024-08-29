import tkinter as tk

from canvas.soccer_field import SoccerFieldCanvas
from frames.control_panel import ControlPanel

def main():
    root = tk.Tk()
    root.title("VSS Positioning System")
    
    field = SoccerFieldCanvas(root, None, width=600, height=520)
    control_panel = ControlPanel(root, field)
    field.control_panel = control_panel

    root.mainloop()

if __name__ == "__main__":
    main()