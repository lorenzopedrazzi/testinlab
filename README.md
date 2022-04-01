import tkinter


from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.title("Colori")
listacolori = ['red', 'blue', 'orange', 'green', 'purple', 'white', 'black', '']
colore = StringVar()


def cambiocolore():
    l.configure(background=listacolori[randint(0, len(listacolori)-1)])

l = ttk.Label(root, textvariable=colore, background= listacolori[randint(0,len(listacolori)-1)])
b = ttk.Button(root, command=cambiocolore, text='Cambio')
b.pack()
l.pack()

root.mainloop()

