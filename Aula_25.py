from tkinter import *

root = Tk()
root.title("APP")

def apresentar():
    print(valor_check.get())

valor_check = IntVar()
check = Checkbutton(
    root,
    text='Está é uma checkbox.',
    variable=valor_check,
    command=apresentar
    ).grid()

root.mainloop()