from tkinter import *

root = Tk()
root.title("Simple buttonframe")


r = StringVar()
r.get()


#function for radiobutton:

MODES = [
    ("2")
    (4)
    (5)
    (6)
]




def clicked(variable):
    answer = Label(root, text= variable)
    answer.grid()









#this is radiobutton or in my opinion is choice text 

radio_button = Radiobutton(root, text="i love you fucking bitch",variable=MODES, padx= 5,pady= 6, command= lambda: clicked)
radio_button1 = Radiobutton(root, text="i love you fucking bitch",variable=MODES, padx= 5,pady= 6, command= lambda: clicked)


#this is confirm button to take a choice
choice_button = Button(root, text="click to confirm", command=lambda: clicked(r.get()))



# pack/grid

radio_button.grid()
radio_button1.grid()
choice_button.grid()


root.mainloop()