from tkinter import *
import random

def nextTurn(row,column):
    global players

    if buttons[row][column]['text']==""and checkWinner() is False:
        if players==player[0]:
            buttons[row][column]['text']=players

            if checkWinner() is False:
                players=player[1]
                label.config(text=(player[1]+" turn"))

            if checkWinner() is True:
                label.config(text=(players[0]+" Youve won!"))

            if checkWinner()=="tie":
                label.config(text=(" it is a tie"))

        else:
            buttons[row][column]['text'] = players

            if checkWinner() is False:
                players = player[0]
                label.config(text=(player[0] + " turn"))

            if checkWinner() is True:
                label.config(text=(players[1] + " Youve won!"))

            if checkWinner() == "tie":
                label.config(text=(" it is a tie"))

def checkWinner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!="":
            return True

    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text']!="":
            return True

    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
            return True

    if buttons[2][0]['text']==buttons[1][1]['text']==buttons[0][2]['text']!="":
            return True

    if emptySpaces() is False:
        return "tie"

    else:
        return False


def emptySpaces():
    spaces=9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                spaces-=1

    if spaces==0:
        return False

    else:
        return True

def newGame():
    global players

    label.config(text=players+" your turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

window=Tk()
window.title("tic tac toe")
player=["X","O"]
players=random.choice(player)
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]

label=Label(text=players+" turn", font=("impact",40))
label.pack()

resetButton=Button(text="Reset", font=("impact",30), command=newGame)
resetButton.pack()

frame=Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame, height=2,width=4,font=("impact",30),text="",
                                    command=lambda row=row,column=column: nextTurn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()