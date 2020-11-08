from gameRules import *
from randAgentRules import *
from simpleAgentRules import *
from complexAgentRules import *
from neuralAgentRules import *
from noApproxAgentRules import *
from features import *
from minmax import *
import pickle

def randomTest(feature,board,player):
    crossWon=0
    noughtsWon=0
    #simple feature training
    for x in range(0,10000):
        board = [[0 for i in range(len(board))] for j in range(len(board))]
        while(terminate(board)==0):
             if(player==True):
                randMove(board,1)
             else:
                randMove(board,2)
             player= not player
             simpleFeatMoveTrain(feature,board,terminate(board))
        if(terminate(board)==1):
            crossWon=crossWon+1
        elif(terminate(board)==2):
            noughtsWon=noughtsWon+1

    print(crossWon)
    print(noughtsWon)

def randomComplexTrain(feature,board,player):
    crossWon=0
    noughtsWon=0
    #complex feature training
    for x in range(0,10000):
        board = [[0 for i in range(len(board))] for j in range(len(board))]
        while(terminate(board)==0):
             if(player==True):
                randMove(board,1)
             else:
                randMove(board,2)
             player= not player
             complexFeatStateTrain(feature,board)
        if(terminate(board)==1):
            crossWon=crossWon+1
        elif(terminate(board)==2):
            noughtsWon=noughtsWon+1
        complexFeatEndTrain(feature,board,terminate(board))
    
    print(crossWon)
    print(noughtsWon)

def randomnoApproxTrain(feature,board,player):
    crossWon=0
    noughtsWon=0
    # feature training
    for x in range(0,50000):
        board = [[0 for i in range(len(board))] for j in range(len(board))]
        while(terminate(board)==0):
             if(player==True):
                randMove(board,1)
             else:
                randMove(board,2)
             player= not player
             noApproxFeatStateTrain(feature,board)
        if(terminate(board)==1):
            crossWon=crossWon+1
        elif(terminate(board)==2):
            noughtsWon=noughtsWon+1
        noApproxFeatEndTrain(feature,board,terminate(board))
    
    print(crossWon)
    print(noughtsWon)
    
def randomNeuralTrain(feature,board,player):
    crossWon=0
    noughtsWon=0
    drawWon=0
    for x in range(0,0):
        game=[]
        toPlay=[]
        board = [[0 for i in range(len(board))] for j in range(len(board))]
        game.append(board)
        if(player==True):
                toPlay.append(1)
        else:
                toPlay.append(2)
        while(terminate(board)==0):
            
             if(player==True):
                
                randMove(board,1)
                toPlay.append(2)
             else:
                
                randMove(board,2)
                toPlay.append(1)
             player= not player
             game.append(board)
        if(terminate(board)==1):
            crossWon=crossWon+1
        elif(terminate(board)==2):
            noughtsWon=noughtsWon+1
        elif(terminate(board)==3):
            drawWon=drawWon+1
        print(len(toPlay))
        print(len(game))
        neuralTrainingGame(feature,game,toPlay,terminate(board))
    neuralTrainingEnd(feature)
    
    print(crossWon)
    print(noughtsWon)
    print(drawWon)
    
    
def simpleVRandom(feature,board,player,simplePlayer):
    #0 is empty, 1 is X and 2 is nought
    simpleFeat=Feature(board)
   
    crossWon=0
    noughtsWon=0
    #testing against random player
  
    for x in range(0,10000):
        board = [[0 for i in range(len(board))] for j in range(len(board))]
        while(terminate(board)==0):
            
             if(player==True):
                 if(simplePlayer):
                   simpleFeatMove(feature,board,1)
                 else:
                     randMove(board,1)
             else:
                if(not simplePlayer):
                   simpleFeatMove(feature,board,2)
                else:
                     randMove(board,2)
             player= not player
        if(terminate(board)==1):
            crossWon=crossWon+1
        elif(terminate(board)==2):
            noughtsWon=noughtsWon+1
    
    print(crossWon)
    print(noughtsWon)

def noApproxVRandom(feature,board,player,complexPlayer):
    #0 is empty, 1 is X and 2 is nought

   
    crossWon=0
    noughtsWon=0
    #testing against random player
    for x in range(0,1000):
        board = [[0 for i in range(len(board))] for j in range(len(board))]
        while(terminate(board)==0):
             if(player==True):
                 if(complexPlayer):
                   noApproxFeatMove(feature,board,1)
                 else:
                     randMove(board,1)
             else:
                if(not complexPlayer):
                   noApproxFeatMove(feature,board,2)
                else:
                     randMove(board,2)
             player= not player
        if(terminate(board)==1):
            crossWon=crossWon+1
        elif(terminate(board)==2):
            noughtsWon=noughtsWon+1
    
    print(crossWon)
    print(noughtsWon)
    
def complexVRandom(feature,board,player,complexPlayer):
    #0 is empty, 1 is X and 2 is nought
    simpleFeat=Feature(board)
   
    crossWon=0
    noughtsWon=0
    #testing against random player
    for x in range(0,1000):
        board = [[0 for i in range(len(board))] for j in range(len(board))]
        while(terminate(board)==0):
             if(player==True):
                 if(complexPlayer):
                   complexFeatMove(feature,board,1)
                 else:
                     randMove(board,1)
             else:
                if(not complexPlayer):
                   complexFeatMove(feature,board,2)
                else:
                     randMove(board,2)
             player= not player
        if(terminate(board)==1):
            crossWon=crossWon+1
        elif(terminate(board)==2):
            noughtsWon=noughtsWon+1
    
    print(crossWon)
    print(noughtsWon)

def complexVSimple(complexFeature,simpleFeature,board,player):
    #0 is empty, 1 is X and 2 is nought
    simpleFeat=Feature(board)
   
    crossWon=0
    noughtsWon=0
    #testing against random player
    for x in range(0,1):
        board = [[0 for i in range(len(board))] for j in range(len(board))]
        while(terminate(board)==0):
             if(player==True):
               complexFeatMove(complexFeature,board,1)
             else:
                simpleFeatMove(simpleFeature,board,2)
             player= not player
             printBoard(board)
        if(terminate(board)==1):
            crossWon=crossWon+1
        elif(terminate(board)==2):
            noughtsWon=noughtsWon+1
    
    print(crossWon)
    print(noughtsWon)


def neuralVRandom(feature,board,neuralPlayer):
    #0 is empty, 1 is X and 2 is nought
    player=True
    crossWon=0
    noughtsWon=0
    #testing against random player
    boards=[]
    finished=[]
##  define board array of length n
    games=1000
    for x in range(0,games):
        boards.append([[0 for i in range(len(board))] for j in range(len(board))])
        
    while(len(boards)>0):
##        very parallel approach to playing multiple games
##    must check each move whether each game has been finsihed or not
##        printBoard(boards[0])
        if(player==True):
            if(neuralPlayer):
                neuralFeatMove(feature,boards,1,False)
            else:
                parallelRandMove(boards,1)
        else:
            if(not neuralPlayer):
                neuralFeatMove(feature,boards,2,False)
            else:
                parallelRandMove(boards,2)
        player = not player
        index=0
        popIndexes=[]
        popped=0
        for i in list(boards):
            if(terminate(i)!=0):
##                print("--------")
##                printBoard(i)
##                print("------")
##                print()
                if(terminate(i)==1):
                    crossWon=crossWon+1
                if(terminate(i)==2):
                    noughtsWon=noughtsWon+1
                popIndexes.append(index-popped)
                popped=popped+1
               
            index=index+1
            
            
        for i in popIndexes:
            boards.pop(i)
            
    results=[]
    results.append(crossWon)
    results.append(noughtsWon)
    print(crossWon)
    print(noughtsWon)
    return results

def neuralVneural(feature,currentBest,board,neuralPlayer):
    #0 is empty, 1 is X and 2 is nought
    player=True
    crossWon=0
    noughtsWon=0
    #testing against random player
    boards=[]
    finished=[]
##  define board array of length n
    games=1000
    for x in range(0,games):
        boards.append([[0 for i in range(len(board))] for j in range(len(board))])
    move=0   
    while(len(boards)>0):
##        very parallel approach to playing multiple games
##    must check each move whether each game has been finsihed or not
        rand=randint(0, 4)
        printBoard(boards[0])
        if(player==True):
           if(move==0 or move==1):
                parallelRandMove(boards,1)
           
           else:
                if(neuralPlayer):
                    neuralFeatMove(feature,boards,1,False)
                    #parallelnoApproxMove(feature,boards,1)
                else:
                    #parallelRandMove(boards,1)
                    #parallelSimpleFeatMove(currentBest,boards,1)
                    neuralFeatMove(currentBest,boards,1,False)
                    #minimax(1,boards,True)
                    #parallelnoApproxMove(currentBest,boards,1)
        else:
           if(move==0 or move==1):
                parallelRandMove(boards,2)
           
           else:
                if(not neuralPlayer):
                    neuralFeatMove(feature,boards,2,False)
                    #parallelnoApproxMove(feature,boards,2)
                else:
                    #parallelRandMove(boards,2)
                    #parallelSimpleFeatMove(currentBest,boards,2)
                    #minimax(1,boards,False)
                    neuralFeatMove(currentBest,boards,2,False)
                    #parallelnoApproxMove(currentBest,boards,2)
                    #parallelSimpleFeatMove(currentBest,boards,2)
        player = not player
        move=move+1
        index=0
        popIndexes=[]
        popped=0
        for i in list(boards):
            if(terminate(i)!=0):
##                print("--------")
##                printBoard(i)
##                print("------")
##                print()
                if(terminate(i)==1):
                    crossWon=crossWon+1
                if(terminate(i)==2):
                    noughtsWon=noughtsWon+1
                popIndexes.append(index-popped)
                popped=popped+1
               
            index=index+1
            
            
        for i in popIndexes:
            boards.pop(i)
            
    results=[]
    results.append(crossWon)
    results.append(noughtsWon)
    print(crossWon)
    print(noughtsWon)
    return results


def neuralVminimax(feature,board,neuralPlayer):
    #0 is empty, 1 is X and 2 is nought
    player=True
    crossWon=0
    noughtsWon=0
    #testing against random player
    boards=[]
    finished=[]
##  define board array of length n
    games=200
    for x in range(0,games):
        boards.append([[0 for i in range(len(board))] for j in range(len(board))])
    move=0   
    while(len(boards)>0):
##        very parallel approach to playing multiple games
##    must check each move whether each game has been finsihed or not
        rand=randint(0, 4)
##        printBoard(boards[0])
        if(player==True):
           if(move==0 or move==1):
                parallelRandMove(boards,1)
           
           else:
                if(neuralPlayer):
                    #parallelRandMove(boards,1)
                    neuralFeatMove(feature,boards,1,False)
                    #parallelSimpleFeatMove(feature,boards,1)
                else:
                    minimax(2,boards,True)
        else:
           if(move==0 or move==1):
                parallelRandMove(boards,2)
           
           else:
                if(not neuralPlayer):
                     #parallelRandMove(boards,2)
                    neuralFeatMove(feature,boards,2,False)
                    #parallelSimpleFeatMove(feature,boards,2)
                else:
                    minimax(2,boards,False)
        player = not player
        move=move+1
        index=0
        popIndexes=[]
        popped=0
        for i in list(boards):
            if(terminate(i)!=0):
##                print("--------")
##                printBoard(i)
##                print("------")
##                print()
                if(terminate(i)==1):
                    crossWon=crossWon+1
                if(terminate(i)==2):
                    noughtsWon=noughtsWon+1
                popIndexes.append(index-popped)
                popped=popped+1
               
            index=index+1
            
            
        for i in popIndexes:
            boards.pop(i)
            
    results=[]
    results.append(crossWon)
    results.append(noughtsWon)
    print(crossWon)
    print(noughtsWon)
    return results

def neuralVminmaxTrain(feature,board,player):
    #0 is empty, 1 is X and 2 is nought
   
    crossWon=0
    noughtsWon=0
    boards=[]
    finished=[]
    
    gameNum=1000
    gamesGoing=[i for i in range(gameNum)]
    games=[[] for i in range(gameNum)]

    toPlay=[[] for i in range(gameNum)]
    
    for x in range(0,gameNum):
        boards.append([[0 for i in range(len(board))] for j in range(len(board))])
        games[x].append([[0 for i in range(len(board))] for j in range(len(board))])
        toPlay[x].append(1)
    while(len(boards)>0):
        rand=randint(0, 4)
        if(player==True):
##            printBoard(boards[0])
            if(len(games[0])==0 or len(games[0])==1):
                parallelRandMove(boards,1)
               
            elif(rand==5):
##                parallelRandMove(boards,1)
                neuralFeatMove(feature,boards,1,True) 
##                neuralFeatMove(feature,boards,1,True) 
            else:
##                parallelRandMove(boards,1)
##                neuralFeatMove(feature,boards,1,True) 
                 boards=minimax(2,boards,True)
        else:
            if(len(games[0])==0 or len(games[0])==1):
                parallelRandMove(boards,2)
                
               
            elif(rand==5):
##                parallelRandMove(boards,2)
                neuralFeatMove(feature,boards,2,True) 
##                neuralFeatMove(feature,boards,2,True) 
            else:
                boards=minimax(2,boards,False)
        for i in range(0,len(gamesGoing)):
            board=copy.deepcopy(boards[i])
            games[gamesGoing[i]].append(board)
            if(player==True):
                toPlay[gamesGoing[i]].append(2)
            else:
                toPlay[gamesGoing[i]].append(1)
            
        player = not player
        index=0
        popIndexes=[]
        popped=0
        for i in list(boards):
            if(terminate(i)!=0):
                if(terminate(i)==1):
                    crossWon=crossWon+1
                if(terminate(i)==2):
                    noughtsWon=noughtsWon+1
                popIndexes.append(index-popped)
                popped=popped+1
               
            index=index+1
            
        for i in popIndexes:
            boards.pop(i)
            gamesGoing.pop(i)
##    print(games)
    point=0
    for game in games:
##     appendthe last state 10 more times
       lastGame=game[len(game)-1]
       lastPlayer=toPlay[point][len(toPlay[point])-1]
       for i in range(0,0):
           game.append(lastGame)
           toPlay[point].append(lastPlayer)
       
       neuralTrainingGame(feature,game,toPlay[point],terminate(game[len(game)-1]))
##       neuralTrainingGame(feature,game,terminate(game[len(game)-1]))
       point=point+1
    neuralContinuousTrain(feature)
    print(crossWon)
    print(noughtsWon)

def neuralVneuralTrain(feature,board,player):
    #0 is empty, 1 is X and 2 is nought
   
    crossWon=0
    noughtsWon=0
    boards=[]
    finished=[]
    
    gameNum=2000
    gamesGoing=[i for i in range(gameNum)]
    games=[[] for i in range(gameNum)]

    toPlay=[[] for i in range(gameNum)]
    
    for x in range(0,gameNum):
        boards.append([[0 for i in range(len(board))] for j in range(len(board))])
        games[x].append([[0 for i in range(len(board))] for j in range(len(board))])
        toPlay[x].append(1)
    while(len(boards)>0):
        rand=randint(0, 4)
        if(player==True):
            printBoard(boards[0])
            if(len(games[0])==0 or len(games[0])==1):
                parallelRandMove(boards,1)
               
            elif(rand==5):
                parallelRandMove(boards,1)
##                 minimax(2,boards,True)
##                neuralFeatMove(feature,boards,1,True) 
            else:
                 parallelRandMove(boards,1)
##                neuralFeatMove(feature,boards,1,True) 
        else:
            if(len(games[0])==0 or len(games[0])==1):
                parallelRandMove(boards,2)
               
            elif(rand==5):
                parallelRandMove(boards,2)
##                neuralFeatMove(feature,boards,2,True) 
            else:
                parallelRandMove(boards,2)
##                neuralFeatMove(feature,boards,2,True) 
        for i in range(0,len(gamesGoing)):
            board=copy.deepcopy(boards[i])
            games[gamesGoing[i]].append(board)
            if(player==True):
                toPlay[gamesGoing[i]].append(2)
            else:
                toPlay[gamesGoing[i]].append(1)
            
        player = not player
        index=0
        popIndexes=[]
        popped=0
        for i in list(boards):
            if(terminate(i)!=0):
                if(terminate(i)==1):
                    crossWon=crossWon+1
                if(terminate(i)==2):
                    noughtsWon=noughtsWon+1
                popIndexes.append(index-popped)
                popped=popped+1
               
            index=index+1
            
        for i in popIndexes:
            boards.pop(i)
            gamesGoing.pop(i)
##    print(games)
    point=0
    for game in games:
##     appendthe last state 10 more times
       lastGame=game[len(game)-1]
       lastPlayer=toPlay[point][len(toPlay[point])-1]
       for i in range(0,0):
           game.append(lastGame)
           toPlay[point].append(lastPlayer)
       
       neuralTrainingGame(feature,game,toPlay[point],terminate(game[len(game)-1]))
##       neuralTrainingGame(feature,game,terminate(game[len(game)-1]))
       point=point+1
    neuralContinuousTrain(feature)
    print(crossWon)
    print(noughtsWon)
    
def neuralVneuraloldTrain(feature,board,player):
    #0 is empty, 1 is X and 2 is nought
   
    crossWon=0
    noughtsWon=0
    boards=[]
    finished=[]
    
    gameNum=1000
    gamesGoing=[i for i in range(gameNum)]
    games=[[] for i in range(gameNum)]
    
    for x in range(0,gameNum):
        boards.append([[0 for i in range(len(board))] for j in range(len(board))])
        
    while(len(boards)>0):
        rand=randint(0, 4)
        if(player==True):
            if(len(games[0])==0 or len(games[0])==1):
                parallelRandMove(boards,1)
               
            elif(rand==1):
                parallelRandMove(boards,1)
##                neuralFeatMove(feature,boards,1,True) 
            else:
                neuralFeatMove(feature,boards,1,True)
        else:
            if(len(games[0])==0 or len(games[0])==1):
                parallelRandMove(boards,2)
               
            elif(rand==1):
                parallelRandMove(boards,2)
##                neuralFeatMove(feature,boards,2,True) 
            else:
                neuralFeatMove(feature,boards,2,True)
        for i in range(0,len(gamesGoing)):
            board=copy.deepcopy(boards[i])
            games[gamesGoing[i]].append(board)
        player = not player
        index=0
        popIndexes=[]
        popped=0
        for i in list(boards):
            if(terminate(i)!=0):
                if(terminate(i)==1):
                    crossWon=crossWon+1
                if(terminate(i)==2):
                    noughtsWon=noughtsWon+1
                popIndexes.append(index-popped)
                popped=popped+1
               
            index=index+1
            
        for i in popIndexes:
            boards.pop(i)
            gamesGoing.pop(i)
    for game in games:
      
       neuralTrainingGame(feature,game,terminate(game[len(game)-1]))

    neuralContinuousTrain(feature)
    print(crossWon)
    print(noughtsWon)

