import tkinter as tk
from tkinter import filedialog

class GeoToolboxApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("GeoToolbox")
        self.root.geometry("600x400")
        
        self.init_ui()
        
    def init_ui(self):
        label = tk.Label(self.root, text="Weclome to GeoToolbox!", font=('Arial', 16))
        label.grid(row=0, column=0)
        
        entry = tk.Entry(self.root, width=50)
        entry.grid(row=1, column=0)
        
        browse_btn = tk.Button(self.root, text="Browse", command=lambda: self.openfile(entry))
        browse_btn.grid(row=1, column=1)
            
    def openfile(self, entryBox):
        filename = filedialog.askopenfilename()
        entryBox.delete(0, tk.END)
        entryBox.insert(tk.END, filename)