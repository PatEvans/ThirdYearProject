#!/usr/bin/python
import tkinter
from tkinter import *
##
from tictactoe import buttonPress
def updateValues(row,col):
    board=buttonPress()

def createDisplay():
   top = tkinter.Tk()
   top.title("Tic-Tac-Toe")
   # Code to add widgets will go here...
   n=5
   title=Label(top,text="Cross To Play")
   title.config(font=("Arial",44))
   title.grid(row=0,columnspan=n)
   for r in range(1,n+1):
      for c in range(0,n):
         tkinter.Button(top, text=" ",command=updateValues(r-1,c), height = 5, width = 10).grid(row=r,column=c)


   top.mainloop()


