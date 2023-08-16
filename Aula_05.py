from tkinter import *

menu = Tk()
menu.title("Título")
menu['bg'] = 'green'
menu.geometry("500x300")

def cmd_Click(msg):
    print(msg)

cmd1 = Button(menu, text="Executar", command=lambda: cmd_Click("Novo Click"))
cmd1.pack()

cmd2 = Button(menu, text="Clicar", command=lambda: cmd_Click("Outra msg"))
cmd2.pack()


menu.mainloop()