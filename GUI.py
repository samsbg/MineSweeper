# Nombre: Samantha Bautista
# Proyecto: Minesweeper
# Día de inicio: 30 de agosto de 2020
# Día de conclusión: 

from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from random import randint
import os


win2 = tk.Tk()

win2.title("Minesweeper")
win2.geometry("290x406")
win2.iconbitmap(os.path.abspath("BombIcon.ico"))

#Difficulty 1-3 that will be set from another page
#The size of the grid like the number of bombs are assigned from this
d = 1

titulo = tk.Button(text="Minesweeper", font=("Bahnschrift", 32))
titulo.grid(column=0, row=0, columnspan=10*d, rowspan=2*d, sticky="NSWE")

#Time needs to be researched and applied
tiempo = tk.Label(text="0:00", font=("Bahnschrift"))
tiempo.grid(column=4*d, row=3*d, columnspan=2*d, sticky="NSWE")

#List of frames that will turn to matrix
LB = []

#Matrix filled with False values
LV = [[False for x in range(8*d)] for y in range(10*d)]

#Images bomb and flag are called from the file
bomb = ImageTk.PhotoImage(Image.open(
    os.path.abspath("Bomb.png")).resize((20, 20)))
flag = ImageTk.PhotoImage(Image.open(
    os.path.abspath("Flag.png")).resize((18,18), Image.ANTIALIAS))

i = 0

#Everytime a random coordenate for a bomb is declared, it adds 1 to every cell surrounding it
#If it is true, false or a number, it's all saved in matrix LV
#This is possible due to python being able to have lists with elements of different types
while i < int(80*(d**2)*0.125*(1+0.2*(d-1))):
    x = randint(0, 8*d-1)
    y = randint(0, 10*d-1)
    if(LV[y][x] is not True):
        LV[y][x] = True
        x1 = -1
        x2 = 2
        y1 = -1
        y2 = 2
        if x == 8*d-1: x2 = 1
        elif x == 0: x1 = 0
        if y == 10*d-1: y2 = 1
        elif y == 0: y1 = 0
        for j in range(y1, y2):
            for k in range(x1, x2):
                if LV[y+j][x+k] == False:
                    LV[y+j][x+k] = 0
                if LV[y+j][x+k] is not True:
                    LV[y+j][x+k] += 1
        i += 1

#Function declaring what happens when a frame with a bomb is chosen
#Becomes red and coming soon, coming soon a bomb label :)
def botonDeBomba(xc, yc):
    if images[yc][xc] != False:
        images[yc][xc].pack_forget()
        images[yc][xc] = False
    else:
        LB[yc][xc].configure(bg="red")

#Function declaring what happens when a frame with a number is chosen
#Becomes white and displays number
def botonSinBombaN(xc, yc):
    if images[yc][xc] != False:
        images[yc][xc].pack_forget()
        images[yc][xc] = False
    else:
        LB[yc][xc].configure(bg="white")
        num = tk.Label(LB[yc][xc], text=LV[yc][xc], bg="white").pack()

#Function declaring what happens when a blank frame is chosen
#Becomes white and does the same with blank frames surrounding it
#Process is stopped when it finds and displays numbers
def botonSinBomba(xc, yc):
    if images[yc][xc] != False:
        images[yc][xc].pack_forget()
        images[yc][xc] = False
    else:
        LB[yc][xc].configure(bg="white")
        x1 = -1
        y1 = -1
        x2 = 2
        y2 = 2
        if xc == 8*d-1: x2 = 1
        elif xc == 0: x1 = 0
        if yc == 10*d-1: y2 = 1
        elif yc == 0: y1 = 0
        for j in range(y1, y2):
            for k in range(x1, x2):
                if LB[yc+j][xc+k].cget("bg") == "gray":
                    if (LV[yc+j][xc+k] is False): botonSinBomba(xc+k, yc+j)
                    elif (LV[yc+j][xc+k] is not True): botonSinBombaN(xc+k, yc+j)

#Saves de flags to be able to use them in other funcions
images = [[False for x in range(8*d)] for y in range(10*d)]

def putFlag(xc, yc):
    if images[yc][xc] == False:
        flagPhoto = Label(LB[yc][xc], image=flag, bg="gray")
        images[yc][xc]=flagPhoto
        flagPhoto.pack()
        bindwidgets(flagPhoto, xc, yc)


def bindwidgets(wid, xc, yc):
    if(LV[yc][xc] is True):
        wid.bind("<Button-1>", lambda event, xc=xc, yc=yc: botonDeBomba(xc, yc))
    elif (LV[yc][xc] is not False):
        wid.bind("<Button-1>", lambda event, xc=xc, yc=yc: botonSinBombaN(xc, yc))
    else:
        wid.bind("<Button-1>", lambda event, xc=xc, yc=yc: botonSinBomba(xc, yc))
    wid.bind("<Button-3>", lambda event, xc=xc, yc=yc: putFlag(xc, yc))

for yc in range(10*d):
    L = []
    for xc in range(8*d):
        boton = tk.Frame(bg="gray", highlightbackground="black",
                         highlightthickness=0.5, width=25, height=25)
        bindwidgets(boton,xc,yc)
        boton.grid(column=((xc+1)*d), row=((yc+4)*d), sticky="NSEW")
        L.append(boton)
    LB.append(L)

CantBombas = tk.Label(
    text=int(80*(d**2)*0.125*(1+0.2*(d-1))), font=("Bahnschrift"))
CantBombas.grid(column=4*d, row=14*d, columnspan=2*d, sticky="NSWE")

for y in range(14*d):
    win2.grid_rowconfigure(y, weight=1)

for x in range(10*d):
    win2.grid_columnconfigure(x, weight=1)

win2.mainloop()
