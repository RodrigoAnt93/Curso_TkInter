from tkinter import *

root = Tk()
root.title("APP")

frame_nome = Frame(root)
frame_morada = Frame(root)

label_nome = Label(frame_nome, text='Nome:')
label_apelido = Label(frame_nome, text='Apilido:')
label_rua = Label(frame_morada, text='Rua:')
label_cidade = Label(frame_morada, text='Cidade:')

t_nome = Entry(frame_nome)
t_apelido = Entry(frame_nome)
t_rua = Entry(frame_morada)
t_cidade = Entry(frame_morada)

cmd_salvar = Button(root, text='Salvar')


label_nome.grid(row=0, column=0)
label_apelido.grid(row=1, column=0)
t_nome.grid(row=0, column=1)
t_apelido.grid(row=1, column=1)

label_rua.grid(row=0, column=0)
label_cidade.grid(row=1, column=0)
t_rua.grid(row=0, column=1)
t_cidade.grid(row=1, column=1)

frame_nome.grid(row=0, column=0)
frame_morada.grid(row=0, column=1)

cmd_salvar.grid(column=1)

root.mainloop()