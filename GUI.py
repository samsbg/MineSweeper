# Nombre: Samantha Bautista
# Proyecto: Minesweeper
# Día de inicio: 30 de agosto de 2020
# Día de conclusión: 

from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import random


win2 = tk.Tk()

win2.title("Minesweeper")
win2.geometry("290x406")
win2.iconbitmap(r"C:\Users\Samantha\Desktop\Minesweeper\Media\BombIcon.ico")

#Dificultad que la da la página anterior
d = 1

#Titulo
titulo = tk.Button(text="Minesweeper", font = ("Bahnschrift", 32))
titulo.grid(column = 0, row = 0, columnspan = 10*d, rowspan = 2*d, sticky = "NSWE")

#Tiempo que falta poner
tiempo = tk.Label(text="0:00", font=("Bahnschrift"))
tiempo.grid(column = 4*d, row = 3*d, columnspan = 2*d, sticky = "NSWE")

#Lista de botones
LB = []

#Lista de listas con valores binarios para las bombas
LV = [[False for x in range(8*d)] for y in range(10*d)] 

bomb = ImageTk.PhotoImage(Image.open(r"C:\Users\Samantha\Desktop\Minesweeper\Media\Bomb.png"))

i = 0

while i < int(80*(d**2)*0.125*(1+0.2*(d-1))):
    x = random.randint(0, 8*d-1)
    y = random.randint(0, 10*d-1)
    if(LV[y][x] == False):
        LV[y][x] = True
        i = i + 1

# for x in range(8*d):
#    for y in range(10*d):
#        if (LV[y][x] == True)
            

for x in range(8*d):
    L = []
    for y in range(10*d):
        if(LV[y][x] == True):
            boton = tk.Button(bg="red", image=bomb)
#            boton.config(image=bomb)
        else:
            boton = tk.Button(bg="gray")
        boton.grid(column = (x+1*d), row = (y+4*d), sticky = "NSEW")
        L.append(boton)
    LB.append(L)

CantBombas = tk.Label(text=int(80*(d**2)*0.125*(1+0.2*(d-1))), font=("Bahnschrift"))
CantBombas.grid(column = 4*d, row = 14*d, columnspan = 2*d, sticky = "NSWE")



GreenFlag = ImageTk.PhotoImage(Image.open(r"C:\Users\Samantha\Desktop\Minesweeper\Media\GreenFlag.png"))
GreenFlagPhoto = Label(image=GreenFlag)

GrayFlag = ImageTk.PhotoImage(Image.open(r"C:\Users\Samantha\Desktop\Minesweeper\Media\GrayFlag.png"))
GrayFlagPhoto = Label(image=GrayFlag)

for y in range(14*d):
    win2.grid_rowconfigure(y, weight=1)

for x in range(10*d):
    win2.grid_columnconfigure(x, weight=1)

win2.mainloop()