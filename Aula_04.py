from tkinter import *

menu = Tk()
menu.title("Título")
menu['bg'] = 'blue'
menu.geometry("500x300+100+100")

btn = Button(menu, text="Executar")
btn.pack()


menu.mainloop()