from tkinter import *

menu = Tk()
menu.title("Título")

label_1 = Label(menu, text="Este é o label 1", font= "Arial 20", bg="red", width= 20)
label_1.pack()

label_2 = Label(menu, text="Este é o label 1", font= "Arial 40", bg="blue", width= 20)
label_2.pack()

menu.mainloop()