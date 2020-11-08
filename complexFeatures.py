class ComplexFeature(object):

    def __init__(self,board):
               self.updatedPatternValues={}
               #simply if pattern
               #appears at any point in history, store in array
               self.patternHistory={}
    def complexStateFeatureExtraction(self,board,convSize):
        #simply, we can define all possible 2x2 patterns
        #and we can update the value of these along with
       stringBoard=""
       for x in range(0,len(board)-(convSize-1)):
          for y in range(0,len(board)-(convSize-1)):
            stringBoard=""
            for i in range(0,convSize):
               for j in range(0,convSize):
                   stringBoard+=str(board[x+i][y+j])
            
            self.patternHistory[stringBoard]=1
       


    def complexFeatureTraining(self,board,result):
          if(result==1):
               for key in  self.patternHistory:
                   if(key in self.updatedPatternValues):
                        self.updatedPatternValues[key]=self.updatedPatternValues[key]+0.01
                   else:
                         self.updatedPatternValues[key]=0.01
          elif(result==2):
                for key in  self.patternHistory:
                    if(key in self.updatedPatternValues):
                        self.updatedPatternValues[key]=self.updatedPatternValues[key]-0.01
                    else:
                         self.updatedPatternValues[key]=-0.01
          self.patternHistory={}


    def stateEvaluation(self,board):
        self.patternHistory={}
        self.complexStateFeatureExtraction(board,2)
        stateValue=0
        for key in self.patternHistory:
            if(key in self.updatedPatternValues):
                stateValue=self.updatedPatternValues[key]+stateValue
        return stateValue

        
        
