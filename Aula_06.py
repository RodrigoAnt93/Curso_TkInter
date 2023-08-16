from tkinter import *

menu = Tk()
menu.title("Título")

largura = 500
altura = 300

# Resolução do nosso sistema

largura_screen = menu.winfo_screenwidth()
altura_screen = menu.winfo_screenheight()

# Posição da janela

posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

# Definir a geometry

menu.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

print(largura_screen, altura_screen)




menu.mainloop()