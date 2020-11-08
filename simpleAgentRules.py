from agentRules import *
def simpleFeatMove(features,board,player):
     move=features.getBestMove(board,player)
     board[move[0]][move[1]]=player
def parallelSimpleFeatMove(features,boards,player):
     for board in boards:
          move=features.getBestMove(board,player)
          board[move[0]][move[1]]=player

def simpleFeatMoveTrain(features,board,result):
     features.simpleFeatureExtraction(board)
     features.simpleFeatureTraining(board,result)
     
