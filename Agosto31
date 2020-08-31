# Proyecto: Minesweeper
# Día de inicio: 30 de agosto de 2020

import tkinter as tk

win = tk.Tk()

win.title("Minesweeper")
win.geometry("290x406")

d = 1

titulo = tk.Button(text="Minesweeper", font = ("Bahnschrift", 32))
titulo.grid(column = 0, row = 0, columnspan = 10*d, rowspan = 2*d, sticky = "NSWE")

tiempo = tk.Label(text="0:00", font=("Bahnschrift"))
tiempo.grid(column = 4*d, row = 3*d, columnspan = 2*d, sticky = "NSWE")

for x in range(8*d):
    for y in range(10*d):
        boton = tk.Button(bg="gray")
        boton.grid(column = (x+1*d), row = (y+4*d), sticky = "NSEW")

CantBombas = tk.Label(text="10", font=("Bahnschrift"))
CantBombas.grid(column = 4*d, row = 14*d, columnspan = 2*d, sticky = "NSWE")

for y in range(14*d):
    win.grid_rowconfigure(y, weight=1)

for x in range(10*d):
    win.grid_columnconfigure(x, weight=1)

win.mainloop()
