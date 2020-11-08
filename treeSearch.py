from monteTree import *
import copy
from neuralFeatures import *
from neuralAgentRules import *
from randAgentRules import *
from random import *
from collections import deque
## start with first state
## self play

def getChildren(parent,player):
    board=parent.board
    if(player==True):
        player=1
    else:
        player=2
    children=[]
    for i in range(0,len(board)):
            for j in range(0,len(board)):
             if(board[i][j]==0):
                board[i][j]=player
                newboard=copy.deepcopy(board)
                board[i][j]=0
                child=Tree(newboard,not parent.player)
                child.parent=parent
                children.append(child)
    return children


def backpropagation(child):
    valueToProp=child.value
    while(child.parent!=None):
        child=child.parent
        if child.player==True:

            
            if(child.value<=valueToProp):
                child.value=valueToProp
            else:
                break
        else:
           
             if(child.value>=valueToProp):
                child.value=valueToProp
             else:
                break

def updateValues(boardsToUpdate,feature):
    singleList = []
    
    for gameState in boardsToUpdate:
            board=copy.deepcopy(gameState.board)
            for z in range(0,len(board)):
                    if(z==0):
                        if(gameState.player):
                            board[z].append(1)
                        else:
                            board[z].append(2)
                    else:
                        board[z].append(0)
            singleList.append(board)

##    print(singleList)   
    prediction=feature.calcValue(singleList)
    
    for i in range(0,len(prediction)):
                boardsToUpdate[i].value=float(prediction[i].item(0))-float(prediction[i].item(1))
                backpropagation(boardsToUpdate[i])
                
                
    

def treeMove(gameTrees,feature,random):
    boardsToUpdate=[]
    for j in range (len(gameTrees)):
        if(randint(0,4)==1):
            gameTrees[j]=gameTrees[j].children[randint(0,len(gameTrees[j].children)-1)]
        else:
            maxIndex=0
        
            if(gameTrees[j].children[0].player==True):
                maxVal=-100000
            else:
                maxVal=10000
            values=[]
            indexes=[]
            for i in range(0,len(gameTrees[j].children)):
                 val=gameTrees[j].children[i].value
                 values.append(val)
                 indexes.append(i)
                 if(gameTrees[j].children[i].player==True):
                     if(val>=maxVal):
                        maxVal=val
                        maxIndex=i
                 else:
                      if(val<=maxVal):
                        maxVal=val
                        maxIndex=i
            maxIndex=choices(indexes,values)[0]
            rand=randint(0,len(gameTrees[j].children)-1)
            if((gameTrees[j].children[maxIndex].player==True and gameTrees[j].children[maxIndex].value==-10000) or (gameTrees[j].children[maxIndex].player==False and gameTrees[j].children[maxIndex].value==10000) ):
##                print("yses")
##                
                if(random==True):
                    boardsToUpdate.append(gameTrees[j].children[rand])
                else:
                    boardsToUpdate.append(gameTrees[j].children[maxIndex])
##                print(rand)
##                print(gameTrees[j].children[rand].board)
##                print()
            if(random):
                gameTrees[j]=gameTrees[j].children[rand]
            else:
                gameTrees[j]=gameTrees[j].children[maxIndex]
    if(len(boardsToUpdate)>0):
        updateValues(boardsToUpdate,feature)
    

def montePlay(feature,board):
    board=[[0 for i in range(len(board))] for j in range(len(board))]
    
    player=True
############
    
    node = Tree(board,player)
    node.value=-100000
               
##########
    noughtsWon=0
    crossWon=0
    gameNum=3000
    finishedGames=[]
    gameTrees=[node for i in range(gameNum)]
    toPlay=[[] for i in range(gameNum)]
    move=0
    while(len(gameTrees)>0):
        for i in range(0,len(gameTrees)):
            node=gameTrees[i]
##            print(node.board)
            if(len(node.children)==0):
               node.children=getChildren(node,node.player)
            for child in node.children:
                if(child.value==[]):
                   if(child.player==True):
                        child.value=-10000
                   else:
                        child.value=10000                 
                    
        if(move==1 or move==0):
             treeMove(gameTrees,feature,True)
        else:
             treeMove(gameTrees,feature,False)
             
        move=move+1
        popped=0
        popIndexes=[]
        index=0
        for game in gameTrees:
            if(terminate(game.board)!=0):
                if(terminate(game.board)==1):
                    crossWon=crossWon+1
                if(terminate(game.board)==2):
                    noughtsWon=noughtsWon+1
                popIndexes.append(index-popped)
                popped=popped+1
            index=index+1
        for i in popIndexes:
            finishedGames.append(gameTrees.pop(i))
    
    for game in finishedGames:
        gamesToTrain=[]
        toPlay=[]
        result = terminate(game.board)
        while(True):
            gamesToTrain.append(copy.deepcopy(game.board))
            if(game.player):  
                toPlay.append(1)
            else:
                toPlay.append(2)
            if(game.parent==None):
                break
            
            game=game.parent
        neuralTrainingGame(feature,gamesToTrain,toPlay,result)
    neuralContinuousTrain(feature)
