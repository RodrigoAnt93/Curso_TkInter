from tkinter import *

root = Tk()
root.title("APP")

frama_login = Frame(root)

label_usuario = Label(frama_login, text='Usuário')
label_password = Label(frama_login, text='Password')
text_usuario = Entry(frama_login)
text_password = Entry(frama_login)
cmd_password = Button(frama_login, text='Entrar')

label_usuario.grid(row=0, column=0)
label_password.grid(row=1, column=0)
text_usuario.grid(row=0, column=1)
text_password.grid(row=1, column=1)
cmd_password.grid(row=2, column=1)

frama_login.grid()




root.mainloop()