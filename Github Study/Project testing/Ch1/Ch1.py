from tkinter import *
import tkinter as tk

class Diplay(tk.Tk):
    def __init__(self):
      super().__init__()
      self.title("hello world")

      label = tk.Label(self,text="Here we are")
      label.pack()



display = Diplay()
display.mainloop()
