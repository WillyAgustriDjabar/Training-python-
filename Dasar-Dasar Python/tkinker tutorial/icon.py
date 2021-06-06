from tkinter import *


root = Tk()
root.title("Simple Icon")
root.iconbitmap('D:\Kuliah\icon\icon.ico')


mylabel = Label(root, text= "budidaya ikan lele")
mylabel.grid(row=0,column=2,padx= 50,pady= 5)
mylabel2 = Label(root, text="budidaya geprek", bd=2, relief=SUNKEN)
mylabel2.grid(row=1,column=2,columnspan= 2, sticky=W+E)












root.mainloop()