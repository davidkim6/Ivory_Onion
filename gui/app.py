import tkinter as tk

class GeoToolboxApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("GeoToolbox")
        self.root.geometry("600x400")
        
        self.init_ui()
        
    def init_ui(self):
        label = tk.Label(self.root, text="Weclome to GeoToolbox!", font=('Arial', 16))
        label.pack(pady=20)