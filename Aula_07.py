from tkinter import *

menu = Tk()
menu.title("Título")

label_1 = Label(menu, text="Este é o label 1")
label_2 = Label(menu, text="Este é o label 2")
cmd = Button(menu, text="Executar")

#pack

label_2.pack()
cmd.pack()
label_1.pack()

menu.mainloop()