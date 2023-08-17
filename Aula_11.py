from tkinter import *

menu = Tk()
menu.title("Título")
menu.geometry("500x500")

label1 = Label(
    menu,
    text="frase de testes\nteste",
    font="Arial 20",
    bd=1,
    relief='solid',
    width=30,
    height=5,
    justify=RIGHT,
    anchor=W

).pack()

label1 = Label(
    menu,
    text="frase de testes\noutra frase\nfrase",
    font="Arial 20",
    bd=1,
    relief='solid',
    padx=10,
    pady=10,
    justify=RIGHT
).pack()

menu.mainloop()