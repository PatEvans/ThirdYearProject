class noApproxFeature(object):

    def __init__(self,board):
               self.updatedPatternValues={}
               #simply if pattern
               #appears at any point in history, store in array
               self.currentBoard={}
    def noApproxStateFeatureExtraction(self,board):
        #simply, we can define all possible 2x2 patterns
        #and we can update the value of these along with
       stringBoard=""
       for x in range(0,len(board)):
          for y in range(0,len(board)):

                stringBoard+=str(board[x][y])
            
       self.currentBoard[stringBoard]=1
       


    def noApproxFeatureTraining(self,board,result):
          if(result==1):
               for key in  self.currentBoard:
                   if(key in self.updatedPatternValues):
                        self.updatedPatternValues[key]=self.updatedPatternValues[key]+0.01
                   else:
                         self.updatedPatternValues[key]=0.01
          elif(result==2):
                for key in  self.currentBoard:
                    if(key in self.updatedPatternValues):
                        self.updatedPatternValues[key]=self.updatedPatternValues[key]-0.01
                    else:
                         self.updatedPatternValues[key]=-0.01
          self.currentBoard={}


    def stateEvaluation(self,board):
        self.currentBoard={}
        self.noApproxStateFeatureExtraction(board)
        stateValue=0
        for key in self.currentBoard:
            if(key in self.updatedPatternValues):
                stateValue=self.updatedPatternValues[key]+stateValue
        return stateValue

        
        
