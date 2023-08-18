from tkinter import *

menu = Tk()
menu.title("Título")
menu.geometry("500x500")

texto = StringVar()
texto.set('Novo texto')

label1 = Label(
    menu,
    font='Arial 20',
    bg='red',
    fg='white',
    textvariable=texto
)

texto.set('Rodrigo Antonio')
label1.pack()
menu.mainloop()