import tkinter as tk
from tkinter import ttk

class GeneralControlPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Play Type Label and Combobox (non-editable)
        tk.Label(self, text="Play Type:").pack(side=tk.TOP, pady=5)
        self.play_type = ttk.Combobox(self, values=["Kickoff", "Penalty", "Freeball"], state="readonly", width=15)
        self.play_type.pack(side=tk.TOP, pady=5)
        self.play_type.current(0)
        
        # Attacking/Defending Toggle Button
        self.attack_defend_var = tk.StringVar(value="Attacking")
        self.toggle_button = tk.Button(self, text="Attacking", command=self.toggle_action)
        self.toggle_button.pack(side=tk.TOP, pady=10)
        
        # Save and Reset Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP, pady=10)
        
        self.save_button = tk.Button(button_frame, text="Save", command=self.save_action)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_action)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        

    def save_action(self):
        # Implement save functionality
        print(f"Play Type saved: {self.play_type.get()}")
        print(f"Current mode: {self.attack_defend_var.get()}")

    def reset_action(self):
        # Implement reset functionality
        self.play_type.current(0)
        self.attack_defend_var.set("Attacking")
        self.toggle_button.config(text="Attacking")
        print("Settings have been reset.")

    def toggle_action(self):
        # Toggle between Attacking and Defending
        if self.attack_defend_var.get() == "Attacking":
            self.attack_defend_var.set("Defending")
            self.toggle_button.config(text="Defending")
        else:
            self.attack_defend_var.set("Attacking")
            self.toggle_button.config(text="Attacking")
        print(f"Toggled to: {self.attack_defend_var.get()}")

