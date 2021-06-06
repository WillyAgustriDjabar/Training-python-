from tkinter import *
from tkinter import messagebox

# display screen
root = Tk()
menubar = Menu(root)

#function
def do_nothing():
    file_open = Toplevel(root)
    aku = Message(file_open, text= "thanks you\n closing in 2 sec",)
    aku.pack()
    aku.after(2000,file_open.destroy)



file_menu = Menu(menubar, tearoff= 0)
file_menu.add_command(label= "", command= do_nothing)
file_menu.add_command(label= "", command=do_nothing)
file_menu.add_command(label= "", command=do_nothing)

#cascade is menu display under display tittle
menubar.add_cascade(label= "file", menu= file_menu)

Setting_menu = Menu(menubar,tearoff= 0)
Setting_menu.add_command(label= "", command= do_nothing)
Setting_menu.add_command(label= "", command= do_nothing)
Setting_menu.add_command(label= "", command= do_nothing)


#cascade is menu display under display tittle
menubar.add_cascade(label="option", menu= Setting_menu)




file_menu.add_separator()

root.config(menu= menubar)
root.mainloop()