from tkinter import *

root = Tk()
root.title("APP")
root.geometry('300x200')

def pegar():
    print(slide.get())

slide = Scale(root, from_=0, to=100,
              orient=HORIZONTAL,
              resolution= 0.5,
              )
slide.pack()

cmd = Button(root, text='Ver Valor', command=pegar).pack()




root.mainloop()