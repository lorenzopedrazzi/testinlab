ES1 

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


ES2 
import tkinter


from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.title("Colori")
colore = StringVar()
def cambiorosso ():
    l.configure(background = 'red')
def cambioviola ():
  l.configure(background = 'purple')
def cambionero ():
  l.configure(background = 'black')
def cambioverde ():
  l.configure(background = 'green')


l = ttk.Label(root)
b = ttk.Button(root, command= cambiorosso, text='Rosso')
c = ttk.Button(root, command = cambioviola, text = 'Viola')
f = ttk.Button(root, command = cambionero, text = 'Nero')
g = ttk.Button(root, command = cambioverde, text = 'Verde')

b.pack()
c.pack()
f.pack()
g.pack()
l.pack()

root.mainloop()

ES3 
import tkinter


from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.title("Colori")
infile = open("sabato.txt", "r")
listatext = []
for line in infile:
    line.strip()
    listatext.append(line)

parent = ttk.Frame(root)
parent.grid(column=0,row=0,sticky="nsew")

fruttaVar = StringVar(value=listatext)
l = Listbox(parent, listvariable=fruttaVar, height=3)
l.grid(column=0,row=0,sticky="nsew")
s = ttk.Scrollbar(parent, orient=VERTICAL, command=l.yview)
s.grid(column=1,row=0,sticky="nsew")
l['yscrollcommand'] = s.set
infile.close()
root.mainloop()

ES4
import tkinter

from tkinter import *
from tkinter import ttk



root = Tk()
spinval = StringVar()
def aggiungere2():
  s = ttk.Spinbox(root, from_=0, to=100.0, increment = 2, textvariable=spinval)
  s.pack()
def aggiungere4():
  s = ttk.Spinbox(root, from_=0, to=100.0, increment = 4, textvariable=spinval)
  s.pack()
def aggiungere8():
  s = ttk.Spinbox(root, from_=0, to=100.0, increment = 8, textvariable=spinval)
  s.pack()

def aggiungere1():
  s = ttk.Spinbox(root, from_=0, to=100.0, increment = 1, textvariable=spinval)
  s.pack()


button4 = Button(root, text = 'di 4 in 4', command = aggiungere4)
button2 = Button(root, text = 'di 2 in 2', command = aggiungere2)
button8 = Button(root, text = 'di 8 in 8', command = aggiungere8)
button1 = Button(root, text = 'di 1 in 1', command = aggiungere1)
button2.pack()
button4.pack()
button8.pack()
#Label1 = Label(root, text = 'Hello World')
#Label2 = Label(root, text = 'Stronzone')

#Label1.grid(row = 0, column = 0)
#Label2.grid(row = 2, column = 1)
root.mainloop()





