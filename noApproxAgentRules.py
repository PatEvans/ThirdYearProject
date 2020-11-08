from agentRules import *
def noApproxFeatMove(features,board,player):
   
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
       
def parallelnoApproxMove(features,boards,player):
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
	    
               
def noApproxFeatStateTrain(features,board):
    #3 represents size of convolution to use
    features.noApproxStateFeatureExtraction(board)

def noApproxFeatEndTrain(features,board,result):
    features.noApproxFeatureTraining(board,result)
