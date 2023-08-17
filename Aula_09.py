from tkinter import *

menu = Tk()
menu.title("Título")
menu.geometry("500x500")

label1 = Label(
    menu,
    text="solid\n",
    font="Arial 20",
    bd=5,
    relief='solid'
).pack()

label1 = Label(
    menu,
    text="flat\n",
    font="Arial 20",
    bd=5,
    relief='flat'
).pack()

label1 = Label(
    menu,
    text="raised\n",
    font="Arial 20",
    bd=5,
    relief='raised'
).pack()

label1 = Label(
    menu,
    text="sunken\n",
    font="Arial 20",
    bd=5,
    relief='sunken'
).pack()

label1 = Label(
    menu,
    text="ridge\n",
    font="Arial 20",
    bd=5,
    relief='ridge'
).pack()

label1 = Label(
    menu,
    text="grove",
    font="Arial 20",
    bd=5,
    relief='groove'
).pack()



menu.mainloop()