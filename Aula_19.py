from tkinter import *

root = Tk()
root.title("APP")

def calcular():
    F = float(textbox1.get())
    C = (F-32) * 5/9
    final.set(str(round(C)) + " graus Celsius")


final = StringVar()

label = Label(root, text='Graus Fahrenheit:')
textbox1 = Entry(root)
button = Button(root, text="Calcular", command=calcular)
label_resultado = Label(root, textvariable=final)

label.grid()
textbox1.grid()
button.grid()
label_resultado.grid()


root.mainloop()