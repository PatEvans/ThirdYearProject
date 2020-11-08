from gameRules import *
from features import *
from complexFeatures import *
from noApproxFeatures import *
from neuralFeatures import *
from agentRules import *
from randAgentRules import *
from simpleAgentRules import *
from complexAgentRules import *
from noApproxAgentRules import *
from neuralAgentRules import *
from testAgents import *
from minmax import *
from treeSearch import *
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import json
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

n = 4

board = [[0 for i in range(n)] for j in range(n)]
player = 1
simpleFeat=Feature(board)
complexFeat=ComplexFeature(board)
noApproxFeat=noApproxFeature(board)
neuralFeat=NeuralFeature()
neuralFeatOther=NeuralFeature()

firstNeural=NeuralFeature()
secondNeural=NeuralFeature()
#randomTest(simpleFeat,board,player)
#simpleVRandom(simpleFeat,board,player,True)
#simpleVRandom(simpleFeat,board,player,False)

#complex featuresw
#difference is that instead of simply taking the end state
#as the sole input for feature extraction, we decided to
#analyse each individual position based upon 'patterns' we see
#in the state which are applied in a convolutional way i.e. we
# check all possible 3x3 patterns in the nxn grid and see if this pattern
#appears and the outcome.

#randomComplexTrain(complexFeat,board,player)

#randomnoApproxTrain(noApproxFeat,board,player)
'''
noApproxVRandom(noApproxFeat,board,player,True)
noApproxVRandom(noApproxFeat,board,player,False)
'''
#complexVRandom(complexFeat,board,player,True)
#complexVRandom(complexFeat,board,player,False)
#complexVSimple(complexFeat,simpleFeat,board,player)

#randomNeuralTrain(neuralFeat,board,player);
##montePlay(neuralFeat,board)
##exit()

#loadModel(neuralFeat,'model.currentMonte')
#loadModel(neuralFeatOther,'model.currentBestminmaxrand')
#neuralVneural(neuralFeat,neuralFeatOther,board,True)
#neuralVneural(neuralFeat,neuralFeatOther,board,False)
crossWon=0
noughtsWon=0
'''
neuralVminimax(neuralFeat,board,True)
neuralVminimax(neuralFeat,board,False)
##

crossRandTestResults=[[],[]]
noughtsRandTestResults=[[],[]]

##neuralFeat.model.save("model.currentBest")
####test=[ [[0 for i in range(n)] for j in range(n)],1]
##testArray=[]
##for i in range(0,100):
##    neuralFeat.addTrainingData(test,1)



##montePlay(neuralFeat,board)
##exit()

crossResult=neuralVminimax(neuralFeat,board,True)
noughtsResult=neuralVminimax(neuralFeat,board,False)


crossRandTestResults[0].append(crossResult[0])
crossRandTestResults[1].append(crossResult[1])
noughtsRandTestResults[0].append(noughtsResult[0])
noughtsRandTestResults[1].append(noughtsResult[1])
print("------")
print()
print()
for i in range(0,0):
    print(i)
    print()
##    if(i%2==0):
    neuralVminmaxTrain(neuralFeat,board,player)
##    else:
##    neuralVneuralTrain(neuralFeat,board,player)
##    neuralVneuralTrain(neuralFeat,board,player)
##    montePlay(neuralFeat,board)
    print("<prev best>")
    loadModel(neuralFeatOther,'model.currentBestminmaxrand')
    crossResult=neuralVneural(neuralFeat,neuralFeatOther,board,True)
    noughtsResult=neuralVneural(neuralFeat,neuralFeatOther,board,False)

    if((crossResult[0]>crossResult[1]) or (noughtsResult[0]<noughtsResult[1])):

            print("yes")
            neuralFeat.model.save("model.currentBestminmaxrand")
#    else:
##         loadModel(neuralFeat,'model.currentBest')

    print("<rand>")
    crossResult=neuralVRandom(neuralFeat,board,True)
    noughtsResult=neuralVRandom(neuralFeat,board,False)
    crossRandTestResults[0].append(crossResult[0])
    crossRandTestResults[1].append(crossResult[1])
    noughtsRandTestResults[0].append(noughtsResult[0])
    noughtsRandTestResults[1].append(noughtsResult[1])
    print("</rand>")
    print()
    print()

print(crossRandTestResults)
print(noughtsRandTestResults)
with open('crossrand.txt','w') as filehandle:
    json.dump(crossRandTestResults,filehandle)
with open('noughtsrand.txt','w') as filehandle:
    json.dump(noughtsRandTestResults,filehandle)
neuralFeat.model.save("model.neural")
'''



##########Gui display functions

from functools import partial
def updateScreen(btn_text):
    for i in range(n):
            for j in range(n):
                if(board[i][j]==1):
                    btn_text[i][j].set("X")
                elif(board[i][j]==2):
                    btn_text[i][j].set("O")
def checkEnd(top,board):
        if(terminate(board)==1):
             messagebox.showinfo("Game Over", "Crosses Wins",parent=top)
             top.destroy()

        elif(terminate(board)==2):
             messagebox.showinfo("Game Over", "Noughts Wins",parent=top)
             top.destroy()
        elif(terminate(board)==3):
             messagebox.showinfo("Game Over", "Draw",parent=top)
             top.destroy()
def buttonPress(row,col,players,btn_text,titletext,top):
        if(players[0]==0):
              if(str(titletext.get())=="Cross to Move"):
                  xMove=row
                  yMove=col
                  makeMove(xMove,yMove,board,True)

                  titletext.set("Noughts to Move")
                  updateScreen(btn_text)
                  top.update()
                  checkEnd(top,board)
                  if(players[1]==0):
                      return
        elif(players[0]==1):
            if(str(titletext.get())=="Cross to Move"):
              simpleFeatMove(simpleFeat,board,1)
              titletext.set("Noughts to Move")
              updateScreen(btn_text)
              top.update()
              checkEnd(top,board)
              if(players[1]!=0):
                buttonPress(-1,-1,players,btn_text,titletext,top)
                checkEnd(top,board)
              return
        elif(players[0]==2):
            if(str(titletext.get())=="Cross to Move"):
              complexFeatMove(complexFeat,board,1)
              titletext.set("Noughts to Move")
              updateScreen(btn_text)
              top.update()
              checkEnd(top,board)
              if(players[1]!=0):
                buttonPress(-1,-1,players,btn_text,titletext,top)
                checkEnd(top,board)
              return
        elif(players[0]==3 or players[0]==4 or players[0]==5):
            if(str(titletext.get())=="Cross to Move"):
              neuralFeatMove(firstNeural,[board],1,False)
              titletext.set("Noughts to Move")
              updateScreen(btn_text)
              top.update()
              checkEnd(top,board)
              if(players[1]!=0):
                buttonPress(-1,-1,players,btn_text,titletext,top)
                checkEnd(top,board)
              return
        top.update()
        updateScreen(btn_text)

        checkEnd(top,board)


        if(players[1]==0):
              if(titletext.get()=="Noughts to Move"):
                  xMove=row
                  yMove=col
                  makeMove(xMove,yMove,board,False)
                  titletext.set("Cross to Move")
                  updateScreen(btn_text)
                  top.update()
                  checkEnd(top,board)
                  if(players[0]!=0):
                    print('yes')
                    buttonPress(-1,-1,players,btn_text,titletext,top)
                    checkEnd(top,board)
                  return
        elif(players[1]==1):
              simpleFeatMove(simpleFeat,board,2)
              titletext.set("Cross to Move")
              updateScreen(btn_text)
              top.update()
              checkEnd(top,board)
              if(players[0]!=0):
                    print('yes')
                    buttonPress(-1,-1,players,btn_text,titletext,top)
                    checkEnd(top,board)
              return
        elif(players[1]==2):
              complexFeatMove(complexFeat,board,2)

              titletext.set("Cross to Move")
              updateScreen(btn_text)
              top.update()
              checkEnd(top,board)
              if(players[0]!=0):
                    print('yes')
                    buttonPress(-1,-1,players,btn_text,titletext,top)
                    checkEnd(top,board)
              return
        elif(players[1]==3 or players[1]==4 or players[1]==5):
            neuralFeatMove(secondNeural,[board],2,False)
            #minimax(2,[board],False)
            titletext.set("Cross to Move")
            updateScreen(btn_text)
            top.update()
            checkEnd(top,board)
            if(players[0]!=0):
                    print('yes')
                    buttonPress(-1,-1,players,btn_text,titletext,top)
                    checkEnd(top,board)
            return
        updateScreen(btn_text)
        top.update()

        checkEnd(top,board)





def createDisplay(players):
   top = tkinter.Tk()
   top.title("Tic-Tac-Toe")
   # Code to add widgets will go here...
   n=4
   titletext=StringVar()
   titletext.set("Cross to Move")
   title=Label(top,textvariable=titletext)
   title.config(font=("Arial",44))
   title.grid(row=0,columnspan=n)
   btn_text = [[StringVar() for i in range(n)] for j in range(n)]
   for r in range(1,n+1):
      for c in range(0,n):

         btn_text[r-1][c].set(" ")
         action_with_arg = partial(buttonPress, r-1,c,players,btn_text,titletext,top)
         btn=Button(top, textvariable=btn_text[r-1][c],command=action_with_arg, height = 1, width = 3)
         btn.grid(row=r,column=c)
         btn['font']=font.Font(size=60)

   if(players[0]!=0):
       buttonPress(-1,-1,players,btn_text,titletext,top)
   top.mainloop()

def playButton(top,players):

    if(players[0]==-1 or players[1]==-1):
        messagebox.showinfo("Warning", "Please Enter Valid Player Values",parent=top)
    else:


        if(players[0]==1 or players[1]==1):
            randomTest(simpleFeat,board,True)
        if(players[0]==2 or players[1]==2):
            randomComplexTrain(complexFeat,board,True)
        if(players[0]==3):
            loadModel(firstNeural,'model.currentBestrand')
        if(players[0]==4):
            loadModel(firstNeural,'model.currentBestneural')
        if(players[0]==5):
            loadModel(firstNeural,'model.currentBestminmaxrand')

        if(players[1]==3):
            loadModel(secondNeural,'model.currentBestrand')
        if(players[1]==4):
            loadModel(secondNeural,'model.currentBestneural')
        if(players[1]==5):
            loadModel(secondNeural,'model.currentBestrand')
        top.destroy()
        createDisplay(players)



def menuScreen():
    players=[-1,-1]
    top=tkinter.Tk()
    top.title("Option Menu")
                      # Add a grid
    mainframe = Frame(top)
    mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)
    firstVar=StringVar(top)
    choices=["You","Simple Features","Complex Features","Randomly Trained NN","NN Led Weighted Moves Trained NN","Supervised Trained NN"]
    firstVar.set("Enter Option Here")
    popupMenu=OptionMenu(mainframe,firstVar,*choices)
    Label(mainframe,text="Choose which player for Crosses").grid(row=1,column=1)
    popupMenu.grid(row=2,column=1)
    def change_first_dropdown(*args):
        player=firstVar.get()
        if(player=="You"):
            players[0]=0
        elif(player=="Simple Features"):
            players[0]=1
        elif(player=="Complex Features"):
            players[0]=2
        elif(player=="Randomly Trained NN"):
            players[0]=3
        elif(player=="NN Led Weighted Moves Trained NN"):
            players[0]=4
        elif(player=="Supervised Trained NN"):
            players[0]=5
    firstVar.trace('w',change_first_dropdown)

    secondVar=StringVar(top)
    secondVar.set("Enter Option Here")
    secondMenu=OptionMenu(mainframe,secondVar,*choices)
    Label(mainframe,text="Choose which player for Noughts").grid(row=3,column=1)
    secondMenu.grid(row=4,column=1)
    def change_second_dropdown(*args):
        player=secondVar.get()
        if(player=="You"):
            players[1]=0
        elif(player=="Simple Features"):
            players[1]=1
        elif(player=="Complex Features"):
            players[1]=2
        elif(player=="Randomly Trained NN"):
            players[1]=3
        elif(player=="NN Led Weighted Moves Trained NN"):
            players[1]=4
        elif(player=="Supervised Trained NN"):
            players[1]=5
    secondVar.trace('w',change_second_dropdown)

    action_with_arg = partial(playButton,top, players)
    btn=Button(mainframe, text="Play",command=action_with_arg, height = 1, width = 3)
    btn.grid(row=5,column=1)
    top.mainloop()


############## end of gui functions


##neuralFeat.model.summary()
menuScreen()
#
while(terminate(board)==0):
    if(player==False):
        print("Player 1 input move:")
        xMove=int(input())
        yMove=int(input())
        makeMove(xMove,yMove,board,player)


    else:
        print("Player 2 input move:")
        if(agentType==1):
            randMove(board)
        elif(agentType==2):
            simpleFeatMove(feature,board)
        elif(agentType==4):
            neuralFeatMove(neuralFeat,[board],1,False)
#              board=minimax(2,[board],False)[0]

    printBoard(board)
    player= not player

if(terminate(board)==1):
    print("Cross won")
elif(terminate(board)==2):
    print("Noughts won")
else:
    print("draw")
