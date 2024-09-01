import tkinter as tk
from entities.controller import Controller 

class app(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.controller = Controller(self)
        self.mainloop()

if __name__ == "__main__":
    app()