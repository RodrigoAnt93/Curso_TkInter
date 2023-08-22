from tkinter import *

root = Tk()
root.title("APP")

lista = Listbox(
    root,

)
lista.grid()

#inserir um item de cada vez
lista.insert(0, 'Primeiro item da lista')
lista.insert(END, 'Segundo item da lista')
lista.insert(END, 'Terceiro item da lista')

#inserir vários itens:

nomes = ['Rodrigo', 'Paula', 'Cecilia']
for nome in nomes:
    lista.insert(END, nome)

lista.delete(4,4)

def executar():
    print(lista.get(ACTIVE))

cmd = Button(root, text='Clique', command=executar).grid()

root.mainloop()