from tkinter import *

menu = Tk()
menu.title("Título")
menu.geometry("500x500")

label1 = Label(
    menu,
    text="label1",
    font='Arial 20',
    bg='RED'
)
label2 = Label(
    menu,
    text="label2",
    font='Arial 20',
    bg='blue'
)

label3 = Label(
    menu,
    text="label3",
    font='Arial 20',
    bg='green'
)

btn1 = Button(menu, text='Click1')
btn2 = Button(menu, text='Click2')
btn3 = Button(menu, text='Click3')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)



menu.mainloop()