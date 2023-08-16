from tkinter import *

menu = Tk()
menu.title("Primeiro app")

menu.geometry("500x250+200+200")
menu.resizable(True, True)
menu.iconbitmap("imagens/icon.ico")

#menu.minsize(500,250)
#menu.maxsize(700, 400)

#menu.state("zoomed")
menu.state("iconic")

menu.tk.mainloop()

