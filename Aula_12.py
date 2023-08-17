from tkinter import *

menu = Tk()
menu.title("Título")
menu.geometry("500x500")

label1 = Label(
    menu,
    text='Frase de teste',
    font='Arial 20',
    bd=1,
    relief='solid'
).pack()

label2 = Label(menu)
label2['text'] = 'texto do label2'
label2['font'] = 'Arial 20'
label2['bd'] = 1
label2['relief'] = 'solid'
label2.pack()


menu.mainloop()