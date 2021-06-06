
from tkinter import *
from tkinter import messagebox

#Show.display
root = Tk()
root.title("simple massage")
root.iconbitmap('D:\Kuliah\icon\icon.ico')
root.geometry("200x200")


def popup():
    messagebox.showinfo('attention!', ' password and username is incorrets')

mylabel = Button(root, text= 'login',command= popup).pack(padx= 20,pady= 20)


root.mainloop()