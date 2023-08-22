from tkinter import *

root = Tk()
root.title("APP")

img = PhotoImage(file="imagens/trg2.png")

label_imagem = Label(root, image=img).pack()


root.mainloop()