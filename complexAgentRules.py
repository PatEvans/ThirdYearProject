from agentRules import *
def complexFeatMove(features,board,player):
   
    max = -1000000
    maxi=-1
    maxj=-1
    for i in range(0,len(board)):
        for j in range(0,len(board)):
             if(board[i][j]==0):
                board[i][j]=player
                currentValue=features.stateEvaluation(board)
                board[i][j]=0
                if(currentValue>max):
                    max=currentValue
                    maxi=i
                    maxj=j
                    
    board[maxi][maxj]=player               
       
def parallelComplexMove(features,boards,player):
    for board in boards:
        max = -1000000
        maxi=-1
        maxj=-1
        for i in range(0,len(board)):
            for j in range(0,len(board)):
                 if(board[i][j]==0):
                    board[i][j]=player
                    currentValue=features.stateEvaluation(board)
                    board[i][j]=0
                    if(currentValue>max):
                        max=currentValue
                        maxi=i
                        maxj=j
                    
        board[maxi][maxj]=player    
	    
               
def complexFeatStateTrain(features,board):
    #3 represents size of convolution to use
    features.complexStateFeatureExtraction(board,3)

def complexFeatEndTrain(features,board,result):
    features.complexFeatureTraining(board,result)
