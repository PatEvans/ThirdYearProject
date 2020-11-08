from gameRules import *
from randAgentRules import *
import copy
def children(board,player):
    children=[]
   
    for i in range(0,len(board)):
            for j in range(0,len(board)):
             if(board[i][j]==0):
                if(player==True):
                    board[i][j]=1
                else:
                    board[i][j]=2
                newboard=copy.deepcopy(board)
                children.append(newboard)
                board[i][j]=0
    
    return children


def minimax(depth,boards, player) :
    
    printBoard(boards[0])
    print()
    for i in range (len(boards)):
       
            x=minmaxFunc(depth,boards[i],player)
            value=x[0]
            newBoard=x[1]
            #print(value)
            #print(x[2])
##            printBoard(x[1])
            if(x[2]==True):
                if(player==True):
                     randMove(boards[i],1)
                elif(player==False):
                     randMove(boards[i],2)
            else:
                for t in range(0,len(boards[i])):
                    for y in range(0,len(boards[i])):
                        if(boards[i][t][y]!=newBoard[t][y]):
                            boards[i][t][y]=newBoard[t][y]

    return boards     

def minmaxFunc(depth,board,player):
    
            result=terminate(board)
            
            if (result!=0):
                if(result==1):
                    return [1]
                elif(result==2):
                    return [-1]
                else:
                    return [0]
            if(depth==0):
                return [0]
            if (player==True):
                value=-1000
                childs=children(board,player)
                oldVal=-1000
                values=[]
                for child in childs:
                
                  
                    current=minmaxFunc(depth-1,child, not player)
                    
                    value = max(value,current[0] )
                   
                    values.append(current[0])
                    if(value>oldVal):
##                        print("yes")
                        
                        board=child
                        
                        oldVal=value
##                
##                print(board)
                #print(value)
                return [value,board,all(x==values[0] for x in values)]
            else:
                value = +10000
                oldVal=+1000
                childs=children(board,player)
                values=[]
#                print(childs)
                for child in childs:
                  
                  
                    current=minmaxFunc(depth-1,child, not player)
                    
                    value = min(value,current[0] )
                   
                    values.append(current[0])
                    if(value<oldVal):
##                        print("yes")
                        
                        board=child
                        
                        oldVal=value
                #print(values)
                return [value,board,all(x==values[0] for x in values)]
