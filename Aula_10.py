from tkinter import *

menu = Tk()
menu.title("Título")
menu.geometry("500x500")

label1 = Label(
    menu,
    text="0123456789",
    font='Arial 20',
    bd=1,
    relief='solid',
    width=25,
    height=4,
    anchor=S
).pack()

menu.mainloop()