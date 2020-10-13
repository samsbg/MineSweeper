# Nombre: Samantha Bautista
# Proyecto: Minesweeper
# Día de inicio: 30 de agosto de 2020
# Día de conclusión: 

from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from random import randint


win2 = tk.Tk()

win2.title("Minesweeper")
win2.geometry("290x406")
win2.iconbitmap(r"C:\Users\Samantha\Desktop\Minesweeper\Media\BombIcon.ico")

#Dificultad que la da la página anterior
d = 1

#Titulo
titulo = tk.Button(text="Minesweeper", font=("Bahnschrift", 32))
titulo.grid(column=0, row=0, columnspan=10*d, rowspan=2*d, sticky="NSWE")

#Tiempo que falta poner
tiempo = tk.Label(text="0:00", font=("Bahnschrift"))
tiempo.grid(column=4*d, row=3*d, columnspan=2*d, sticky="NSWE")

#Lista de botones
LB = []

#Lista de listas con valores binarios para las bombas
LV = [[False for x in range(8*d)] for y in range(10*d)]

bomb = ImageTk.PhotoImage(Image.open(
    r"C:\Users\Samantha\Desktop\Minesweeper\Media\Bomb.png").resize((20, 20)))

i = 0

while i < int(80*(d**2)*0.125*(1+0.2*(d-1))):
    x = randint(0, 8*d-1)
    y = randint(0, 10*d-1)
    if(LV[y][x] is not True):
        LV[y][x] = True
        x1 = -1
        x2 = 2
        if x == 8*d-1:
            x2 = 1
        elif x == 0:
            x1 = 0
        y1 = -1
        y2 = 2
        if y == 10*d-1:
            y2 = 1
        elif y == 0:
            y1 = 0
        for j in range(y1, y2):
            for k in range(x1, x2):
                if LV[y+j][x+k] == False:
                    LV[y+j][x+k] = 0
                if LV[y+j][x+k] is not True:
                    LV[y+j][x+k] += 1
        i += 1


def botonDeBomba(xc, yc):
    LB[yc][xc].configure(bg="red")


def botonSinBombaN(xc, yc):
    LB[yc][xc].configure(bg="white")
    num = tk.Label(LB[yc][xc], text=LV[yc][xc], bg="white").pack()


def botonSinBomba(xc, yc):
    LB[yc][xc].configure(bg="white")
    x1 = -1
    x2 = 2
    if xc == 8*d-1:
        x2 = 1
    elif xc == 0:
        x1 = 0
    y1 = -1
    y2 = 2
    if yc == 10*d-1:
        y2 = 1
    elif yc == 0:
        y1 = 0
    for j in range(y1, y2):
        for k in range(x1, x2):
            if LB[yc+j][xc+k].cget("bg") == "gray":
                if (LV[yc+j][xc+k] is False):
                    botonSinBomba(xc+k, yc+j)
                elif (LV[yc+j][xc+k] is not True):
                    botonSinBombaN(xc+k, yc+j)


for yc in range(10*d):
    L = []
    for xc in range(8*d):
        boton = tk.Frame(bg="gray", highlightbackground="black",
                         highlightthickness=0.5, width=25, height=25)
        if(LV[yc][xc] is True):
            boton.bind("<Button-1>", lambda event, xc=xc,
                       yc=yc: botonDeBomba(xc, yc))
        elif (LV[yc][xc] is not False):
            boton.bind("<Button-1>", lambda event, xc=xc,
                       yc=yc: botonSinBombaN(xc, yc))
        else:
            boton.bind("<Button-1>", lambda event, xc=xc,
                       yc=yc: botonSinBomba(xc, yc))
        boton.grid(column=((xc+1)*d), row=((yc+4)*d), sticky="NSEW")
        L.append(boton)
    LB.append(L)

CantBombas = tk.Label(
    text=int(80*(d**2)*0.125*(1+0.2*(d-1))), font=("Bahnschrift"))
CantBombas.grid(column=4*d, row=14*d, columnspan=2*d, sticky="NSWE")

GreenFlag = ImageTk.PhotoImage(Image.open(
    r"C:\Users\Samantha\Desktop\Minesweeper\Media\GreenFlag.png"))
GreenFlagPhoto = Label(image=GreenFlag)

GrayFlag = ImageTk.PhotoImage(Image.open(
    r"C:\Users\Samantha\Desktop\Minesweeper\Media\GrayFlag.png"))
GrayFlagPhoto = Label(image=GrayFlag)

for y in range(14*d):
    win2.grid_rowconfigure(y, weight=1)

for x in range(10*d):
    win2.grid_columnconfigure(x, weight=1)

win2.mainloop()
