class Feature(object):
    
    def __init__(self,board):
        self.stateLocations=[[0 for i in range(len(board))] for j in range(len(board))]
        self.updatedValues=[[0 for i in range(len(board))] for j in range(len(board))]

    def simpleFeatureExtraction(self,board):
         for i in range(0,len(board)):
             for j in range(0,len(board)):
                if(board[i][j]==1):
                    self.stateLocations[i][j]=1

    def simpleFeatureTraining(self,board,result):
           if(result==1):
               for i in range(0,len(board)):
                 for j in range(0,len(board)):
                    if(self.stateLocations[i][j]==1):
                        self.updatedValues[i][j]=self.updatedValues[i][j]+0.01
           elif(result==2):
                for i in range(0,len(board)):
                  for j in range(0,len(board)):
                    if(self.stateLocations[i][j]==1):
                        self.updatedValues[i][j]=self.updatedValues[i][j]-0.01
           self.stateLocations=[[0 for i in range(len(board))] for j in range(len(board))]

    def getBestMove(self,board,player):
        maxi=-1
        maxj=-1
        maxVal=-10000000
        for i in range(0,len(board)):
                  for j in range(0,len(board)):
                      
                        if(board[i][j]==0 and self.updatedValues[i][j]>maxVal):
                            maxi=i
                            maxj=j
                            maxVal=self.updatedValues[i][j]

        return [maxi,maxj]
        
                
               

        
