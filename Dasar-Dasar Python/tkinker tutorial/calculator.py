from tkinter import *

call = Tk()
call.title("Simple Calculator")

label_hasil = Entry(call, width= 60,bg="white", borderwidth= 5)
label_hasil.grid(row= 0, column= 0, columnspan= 50, padx= 1, pady= 15)
#label_hasil.insert(0,"Here")

def button_click(number):
    Cureent = label_hasil.get()
    label_hasil.delete(0, END)
    label_hasil.insert(0, str(Cureent) + str(number))

def button_hapus():
    label_hasil.delete(0, END)

def button_add():
     First_number = label_hasil.get()
     global f_num
     global calculator
     calculator = "tambah"
     f_num = int(First_number)
     label_hasil.delete(0, END)

def button_kurangin():
    first_number = label_hasil.get()
    global f_num
    global calculator
    calculator = "kurang"
    f_num = int(first_number)
    label_hasil.delete(0, END)

def button_bagiin():
    first_number = label_hasil.get()
    global f_num
    global calculator
    calculator = "bagi"
    f_num = int(first_number)
    label_hasil.delete(0, END)

def button_kalian():
    first_number = label_hasil.get()
    global f_num
    global calculator
    calculator = "kalian"
    f_num = int(first_number)
    label_hasil.delete(0, END)





def button_hasil():
    second_number = label_hasil.get()
    label_hasil.delete(0, END)

    if calculator == "kurang":
      label_hasil.insert(0, f_num - int(second_number))

    if calculator == "tambah":
      label_hasil.insert(0, f_num + int(second_number))

    if calculator == "kalian":
      label_hasil.insert(0, f_num * int(second_number))

    if calculator == "bagi":
      label_hasil.insert(0, f_num / int(second_number))

 


 
#Tombol Display Calculator

button0 = Button(call, text="0", padx=45, pady= 20, command=lambda:button_click(0))
button1 = Button(call, text="1", padx=45, pady= 20, command=lambda: button_click(1))
button2= Button(call, text="2", padx=45, pady= 20, command=lambda: button_click(2))
button3= Button(call, text="3", padx=45, pady= 20, command=lambda: button_click(3))
button4= Button(call, text="4", padx=45, pady= 20, command=lambda: button_click(4))
button5 = Button(call, text="5", padx=45, pady= 20, command=lambda: button_click(5))
button6= Button(call, text="6", padx=45, pady= 20, command=lambda: button_click(6))
button7= Button(call, text="7", padx=45, pady= 20, command=lambda: button_click(7))
button8= Button(call, text="8", padx=45, pady= 20, command=lambda: button_click(8))
button9= Button(call, text="9", padx=45, pady= 20, command=lambda: button_click(9))

#Function tombol

button_tambah = Button(call, text="+", padx=45, pady=20,command=button_add)
button_kurang = Button(call, text="-", padx=45, pady=20, command=button_kurangin)
button_kali = Button(call, text="x", padx=45, pady=20, command= button_kalian)
button_bagi = Button(call,text="/", padx=45,pady=20, command=button_bagiin)
button_clear =  Button(call, text="Hapus", padx=31, pady=20, command=lambda: button_hapus())
button_titik = Button(call, text="=", padx= 47, pady=20, command= button_hasil)

#Grid Display Calculator

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4, column=0)
button_titik.grid(row=4, column=1)

button_tambah.grid(row=4, column=3)
button_kurang.grid(row=3, column=3)
button_bagi.grid(row=1,column=3)
button_kali.grid(row=2, column=3)



button_clear.grid(row=4, column=2)






call.mainloop()