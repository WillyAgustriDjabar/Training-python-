import tkinter as tk
from tkinter.constants import BOTH

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("hello")
        
        my_table = tk.Button(text= "hello world")
        my_table.pack(fill= tk.BOTH)


label = Window()
label.mainloop()
