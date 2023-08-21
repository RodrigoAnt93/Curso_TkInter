from tkinter import *


#--------------------------------------
# funções
def mostrarNome():
    vartexto.set(textbox1.get())


#--------------------------------------
# GUI
root = Tk()
root.title("APP")

vartexto = StringVar()


#--------------------------------------
# widgets
label1 = Label(root, text='O teu nome é: ')
textbox1 = Entry(root)
button1 = Button(root, text='Executar', command=mostrarNome)
label2 = Label(root, textvariable=vartexto)

#--------------------------------------
# layout
label1.grid()
textbox1.grid()
button1.grid()
label2.grid()


root.mainloop()