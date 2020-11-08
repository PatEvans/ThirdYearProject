from agentRules import *
from gameRules import *
import numpy as np
from tensorflow.keras.models import load_model
from random import choices
import copy
def getChildren(board,player):
    
    children=[]
    for i in range(0,len(board)):
            for j in range(0,len(board[i])):
             if(board[i][j]==0):
                if (player==2):
                    board[i][j]=1
                if (player==1):
                    board[i][j]=2
                newboard=copy.deepcopy(board)
                for z in range(0,len(newboard)):
                    if(z==0):
                        newboard[z].append(player)
                    else:
                        newboard[z].append(0)
                board[i][j]=0
                children.append(newboard)
    if(children==[]):
       newboard=copy.deepcopy(board)
       for z in range(0,len(newboard)):
                    if(z==0):
                        newboard[z].append(player)
                    else:
                        newboard[z].append(0)
       children.append(newboard)
    return children
def neuralFeatMove(feature,boards,player,randomness):
    maxVal=-10000000
    maxi=[-1 for i in range(len(boards))]
    maxj=[-1 for i in range(len(boards))]
    gameBoards=[[] for i in range(len(boards))]
    iindexes=[[] for i in range(len(boards))]
    jindexes=[[] for i in range(len(boards))]
    for x in range(0,len(boards)):
        for i in range(0,len(boards[x])):
            for j in range(0,len(boards[x])):
             if(boards[x][i][j]==0):
                boards[x][i][j]=player

##                newboard=[copy.deepcopy(boards[x]),player]
                
                
                
                newboard=copy.deepcopy(boards[x])
               
##                printBoard(newboard)
                
                gameBoards[x].append(newboard)
                iindexes[x].append(i)
                jindexes[x].append(j)
                boards[x][i][j]=0
##  we have array of size [n][n]
##  need to convert to one big n dimensional array
##  in order to do this we need to 'remember' the
##  number of games for each board

##   convert to 1d array to be passed into nn
 
    singleList = []
    indexList=[]
    boardReference=[[] for i in range(len(boards))]
    #print(gameBoards)
    #print()
    for count in range(len( gameBoards)):
        totalBoards=[]
        gameLen=0
        for boardNum in range (len(gameBoards[count])):
            #print(gameBoards[count])
            children=getChildren(gameBoards[count][boardNum], player)
            for child in children:
                singleList.append(child)
                gameLen=gameLen+1
            boardReference[count].append(len(children))  
        indexList.append(gameLen)
    #print(singleList)
    #print(boardReference)
    #print(singleList)
    prediction=feature.calcValue(singleList)
    #print(singleList)
    index=0
    totalIndex=0
    finalPrediction=[[] for i in range(len(boards))]
   
    for i in range(0,len(indexList)):
        for index in range(0,indexList[i]):
                finalPrediction[i].append(prediction[totalIndex])
                totalIndex=totalIndex+1   
        index=0

    
##    print("yes")
##    print(finalPrediction[0])
##    print()
##  item 0 is probability that X will win
##  item 1 is probabilty that O will win
    game=0
    if(randomness==False):
        for x in finalPrediction:
                index=0
                maxIndex=-10000
                minVal=10000
                #print(x)
                counter=0
                tempBoardList=[]
                if(player==1):
                    for i in range(len(boardReference[game])):
                        maxVal=-100000
                        #print(gameBoards[game][i])
                        for j in range(boardReference[game][i]):
                            
                          theValue=finalPrediction[game][counter]
                          
                          val=float(theValue.item(1))-float(theValue.item(0))
                          #print( str(theValue.item(0))+" "+str(theValue.item(0)) )
                          if(val>maxVal):
                              maxVal=val
                          counter=counter+1
                        #print()
                        #print(maxVal)
                        if(maxVal<minVal):
                            minVal=maxVal
                            maxIndex=i
                        #print()
                        
##                    val=-float(y.item(0))
                        
                else:
                    for i in range(len(boardReference[game])):
                        maxVal=-100000
                        #print(gameBoards[game][i])
                        for j in range(boardReference[game][i]):
                          theValue=finalPrediction[game][counter]
                          
                          val=float(theValue.item(0))-float(theValue.item(1))
                          #print( str(theValue.item(0))+" "+str(theValue.item(0)) )
                          if(val>maxVal):
                              maxVal=val
                          counter=counter+1
                        #print()
                        #print(maxVal)
                        if(maxVal<minVal):
                            minVal=maxVal
                            maxIndex=i
                        #print()
                        
##                    val=-float(y.item(0))
                
                #print(maxIndex)
                #print(gameBoards[game][maxIndex])
                for i in range(len(boards[game])):
                    for j in range(len(boards[game])):
                       if(boards[game][i][j]!=gameBoards[game][maxIndex][i][j]):
                           
                           if(gameBoards[game][maxIndex][i][j]==1):
                               boards[game][i][j]=1
                           elif(gameBoards[game][maxIndex][i][j]==2):
                               
                                boards[game][i][j]=2
                #print(boards[game])
                index=index+1
                game=game+1
                maxVal=-10000000
    else:
      
       for x in finalPrediction:
           
            values=[]
            index=0
            indexes=[]
            for y in x:
                if(player==1):
                    values.append(float(y.item(0))-float(y.item(1)))
##                     values.append(float(y.item(0)))

                else:
                    values.append(float(y.item(1))-float(y.item(0)))
##                     values.append(-float(y.item(0)))

                indexes.append(index)
                index=index+1
            
            minVal=min(values)
           
            for i in range(0,len(values)):
                values[i]=((values[i]-minVal)**3)*100000
#                values[i]=((values[i]-minVal))
##            print(values)
            index=choices(indexes,values)[0]
           
            maxi[game]=iindexes[game][index]
            maxj[game]=jindexes[game][index]
             
                
            game=game+1
            maxVal=-10000000 
    #for game in range(0,len(boards)):
    #    boards[game][maxi[game]][maxj[game]]=player
       

def neuralTrainingGame(feature,game,player,result):
    result=result-1
##    if(result==0):
##        result=100
##    elif (result==1):
##        result=-100
##    else:
##        result=0
    index=0
    
  
    for x in game:
        for i in range(0,len(x)):
            if(i==0):
                x[i].append(player[index])
            else:
                x[i].append(0)
        feature.addTrainingData(x,result)

##        printBoard(x)
##        print(player[index])
##        print(result)
        index=index+1

def neuralTrainingEnd(feature):
        feature.prepareXY()
        feature.createModel()
        

def neuralTest(feature,board):
        y=feature.calcValue(board)
        #print(y)
        #print(y.argmax(axis=-1))


def neuralContinuousTrain(feature):
     feature.prepareXY()
     feature.model.fit(feature.x,feature.y,batch_size=256,epochs=5,validation_split=0.1,shuffle=True,use_multiprocessing=True,workers=8,verbose=0)
     feature.training_data=[]
     feature.x=[]
##     feature.w=[]
     feature.y=[]
def loadModel(feature,name):
   feature.model=load_model(name)
  
