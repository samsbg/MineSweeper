#Nombre: Samantha Bautista
#Proyecto: Minesweeper
#Día de inicio: 30 de agosto de 2020
#Día de conclusión: 

from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from random import randint
import os
from time import sleep

def juego():

    win2 = tk.Tk()
    win2.title("Minesweeper")
    win2.geometry("290x406")
    win2.iconbitmap(os.path.abspath("BombIcon.ico"))

    #Difficulty 1-3 that will be set from another page
    #The size of the grid like the number of bombs are assigned from this
    d = 1
    columnas = 8*d
    renglones = 10*d
    juego.nbombas = int(80*(d**2)*0.125*(1+0.2*(d-1)))

    #Time needs to be researched and applied
    tiempo = tk.Label(text="0:00", font=("Bahnschrift"))
    tiempo.grid(column=4*d, row=3*d, columnspan=2*d, sticky="NSWE")

    CantBombas = tk.Label(text=juego.nbombas, font=("Bahnschrift"))
    CantBombas.grid(column=4*d, row=14*d, columnspan=2*d, sticky="NSWE")

    #List of frames that will turn to matrix
    LB = []

    #Matrix filled with False values
    LV = [[False for x in range(columnas)] for y in range(renglones)]

    labels = [[False for x in range(columnas)] for y in range(renglones)]

    #Saves the flags to be able to use them in other funcions
    images = [[False for x in range(columnas)] for y in range(renglones)]

    #Images bomb and flag are called from the file
    bomb = ImageTk.PhotoImage(Image.open(os.path.abspath("Bomb.png")).resize((18, 18)))
    flag = ImageTk.PhotoImage(Image.open(os.path.abspath("Flag.png")).resize((18,18), Image.ANTIALIAS))

    #Everytime a random coordenate for a bomb is declared, it adds 1 to every cell surrounding it
    #If it is true, false or a number, it's all saved in matrix LV
    #This is possible due to python being able to have lists with elements of different types
    i = 0
    while i < juego.nbombas:
        x = randint(0, columnas-1)
        y = randint(0, renglones-1)
        if(LV[y][x] is not True):
            LV[y][x] = True
            x1 = -1
            x2 = 2
            y1 = -1
            y2 = 2
            if x == columnas-1: x2 = 1
            elif x == 0: x1 = 0
            if y == renglones-1:y2 = 1
            elif y == 0: y1 = 0
            for j in range(y1, y2):
                for k in range(x1, x2):
                    if LV[y+j][x+k] == False:
                        LV[y+j][x+k] = 0
                    if LV[y+j][x+k] is not True:
                        LV[y+j][x+k] += 1
            i += 1

    def regresar():
        print("regresar")
        win2.destroy()
        juego()

    titulo = tk.Button(text="Minesweeper", font=("Bahnschrift", 32), command=regresar)
    titulo.grid(column=0, row=0, columnspan=renglones, rowspan=2*d, sticky="NSWE")

    #Function declaring what happens when a frame with a bomb is chosen
    #Becomes red, bomb label, missing to end game
    def botonDeBomba(xc, yc):
        if images[yc][xc] == False:
            LB[yc][xc].configure(bg="red")
            flagPhoto = tk.Label(LB[yc][xc], image=bomb, bg="red")
            images[yc][xc] = flagPhoto
            flagPhoto.pack()
        else:
            ridFlag(xc, yc)
            
    #Function declaring what happens when a frame with a number is chosen
    #Becomes white and displays number
    def botonSinBombaN(xc, yc):
        if images[yc][xc] == False and labels[yc][xc] == False:
            LB[yc][xc].configure(bg="white")
            labels[yc][xc] = tk.Label(LB[yc][xc], text=LV[yc][xc], bg="white")
            labels[yc][xc].pack()
        else:
            ridFlag(xc, yc)

    #Function declaring what happens when a blank frame is chosen
    #Becomes white and does the same with blank frames surrounding it
    #Process is stopped when it finds and displays numbers
    def botonSinBomba(xc, yc):
        if images[yc][xc] == False:
            LB[yc][xc].configure(bg="white")
            x1 = -1
            y1 = -1
            x2 = 2
            y2 = 2
            if xc == columnas-1: x2 = 1
            elif xc == 0: x1 = 0
            if yc == renglones-1: y2 = 1
            elif yc == 0: y1 = 0
            for j in range(y1, y2):
                for k in range(x1, x2):
                    if LB[yc+j][xc+k].cget("bg") == "gray":
                        if (LV[yc+j][xc+k] is False):
                            botonSinBomba(xc+k, yc+j)
                        elif (LV[yc+j][xc+k] is not True):
                            botonSinBombaN(xc+k, yc+j)      
        else:
            ridFlag(xc, yc)

    #Puts a flag by adding a label with the image on the frame
    #It also decreases the number of bombs displayed at the bottom
    #If the amount of boombs is zero, it runs the zerobombs function
    def putFlag(xc, yc):
        if images[yc][xc] == False:
            images[yc][xc] = tk.Label(LB[yc][xc], image=flag, bg="gray")
            images[yc][xc].pack()
            bindwidgets(images[yc][xc], xc, yc)
            juego.nbombas -= 1
            CantBombas.configure(text=juego.nbombas)
            if juego.nbombas == 0:
                zeroBombs()

    #Deletes a flag by deleting the label with the image on the frame
    #It also increases the number of bombs displayed at the bottom
    #If the amount of boombs is zero, it runs the zerobombs function
    def ridFlag(xc, yc):
        images[yc][xc].pack_forget()
        images[yc][xc] = False
        juego.nbombas += 1
        CantBombas.configure(text=juego.nbombas)
        if juego.nbombas == 0:
            zeroBombs()

    def zeroBombs():
        value = True
        for a in range(renglones):
            for b in range(columnas):
                if LV[a][b] is not True and images[a][b] is not False:
                    value = False
        if value:
            for a in range(renglones):
                for b in range(columnas):

                    if images[a][b] is not False:
                        images[a][b].pack_forget()
                    if labels[a][b] is not False:
                        labels[a][b].pack_forget()

                    if LV[a][b] is True:
                        LB[a][b].configure(background="forest green")
                    else:
                        LB[a][b].configure(background="lime green")
            
            CantBombas.grid_forget()
            botonRegresar = Button(text="Regresar", font=("Bahnschrift"), command=regresar, bg="gray")
            botonRegresar.grid(column=4*d, row=14*d, columnspan=2*d, sticky="NSWE")

    def bindwidgets(wid, xc, yc):
        if(LV[yc][xc] is True):
            wid.bind("<Button-1>", lambda event, xc=xc,
                    yc=yc: botonDeBomba(xc, yc))
        elif (LV[yc][xc] is not False):
            wid.bind("<Button-1>", lambda event, xc=xc,
                    yc=yc: botonSinBombaN(xc, yc))
        else:
            wid.bind("<Button-1>", lambda event, xc=xc,
                    yc=yc: botonSinBomba(xc, yc))
        wid.bind("<Button-3>", lambda event, xc=xc, 
                    yc=yc: putFlag(xc, yc))

    #Creation of frames
    for yc in range(renglones):
        L = []
        for xc in range(columnas):
            boton = tk.Frame(bg="gray", highlightbackground="black",
                            highlightthickness=0.5, width=25, height=25)
            bindwidgets(boton,xc,yc)
            boton.grid(column=((xc+1)*d), row=((yc+4)*d), sticky="NSEW")
            L.append(boton)
        LB.append(L)

    for y in range(14*d):
        win2.grid_rowconfigure(y, weight=1)

    for x in range(renglones):
        win2.grid_columnconfigure(x, weight=1)

    win2.mainloop()

juego()
