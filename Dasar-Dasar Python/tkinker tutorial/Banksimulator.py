from tkinter import *
from typing import Collection, Sized, Tuple

screen = Tk()
screen.title("bank mandiri")

def button_lanjut():
    uname.get()
    pw.get()
    uname.delete(0, END)
    pw.delete(0, END)
    screen1 = Tk()
    screen1.title("hello welcome")
    screen1.mainloop()




#Pembuka

opening_text = Label(text="Welcome to Livin by Mandiri")
opening_text1 = Label(text="Silakan Masukan Username dan Password")
uname = Label(text="Username : ")
pw = Label(text="Passowrd : ")



opening_text.grid(row=0,column= 2, padx= 5)
opening_text1.grid(row=1,column= 2,padx= 5)
uname.grid(row=3,column=1)
pw.grid(row=4,column=1)

#Halaman Login

uname = Entry(width= 25, bg="grey")
uname.grid(row=3,column=2)
button_login = Button(screen, text="Login", command=button_lanjut)

pw = Entry(width= 25, bg="grey")
pw.grid(row=4,column=2)
button_login.grid(row=5,column=2,columnspan=100)

screen.mainloop()