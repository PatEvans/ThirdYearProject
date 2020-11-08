
def terminate(board):
    #check horizontal
    for x in board:
        horizontal=""
        for y in x:
            horizontal+=str(y)
        if("1111" in horizontal):
            return 1
        elif("2222" in horizontal):
            return 2

    #check vertical
    for i in range(0,len(board)):
        vertical=""
        for j in range(0,len(board)):
            vertical+=str(board[j][i])
        if("1111" in vertical):
            return 1
        elif("2222" in vertical):
            return 2

    #check one diagonal
    for i in range(0,2*len(board)-1):
        j=0
        diagonal=""
        while True:
            if(i-j <len(board) and j<len(board)):
                diagonal+=str(board[j][i-j]) 
                
            
            if(j==i or (i-j)<0):
                break
            j=j+1
        if("1111" in diagonal):
            return 1
        elif("2222" in diagonal):
            return 2
    
     #check other diagonal
    for i in range(0,2*len(board)-1):
        j=0
        otherDiagonal=""
        while True:
            if(i-j <len(board) and j<len(board)):
                otherDiagonal+=str(board[j][(len(board)-1)-(i-j)]) 
            
            if(j==i or (i-j)<0):
                break
            j=j+1
        if("1111" in otherDiagonal):
            return 1
        elif("2222" in otherDiagonal):
            return 2
        
      

    #check if full
    notFull=False
    for x in board:
        horizontal=""
        for y in x:
            horizontal+=str(y)
        if("0" in horizontal):
            notFull=True
    if(notFull==False):
        return 3
    return 0

def printBoard(board):
    for x in board:
        for y in x:
            if(y==1):
                print ("X", " ", end="")
            elif(y==2):
                print("O", " ", end="")
            else:
               print("_", " ", end="")
        print("")
        
    
def makeMove(xMove,yMove,board,player):
    if(board[xMove][yMove]!=0):
        return False
    else:
        if(player==True):
            board[xMove][yMove]=1
        else:
            board[xMove][yMove]=2




def terminateThree(board):
    #check horizontal
    for x in board:
        horizontal=""
        for y in x:
            horizontal+=str(y)
        if("111" in horizontal):
            return 1
        elif("222" in horizontal):
            return 2

    #check vertical
    for i in range(0,len(board)):
        vertical=""
        for j in range(0,len(board)):
            vertical+=str(board[j][i])
        if("111" in vertical):
            return 1
        elif("222" in vertical):
            return 2

    #check one diagonal
    for i in range(0,2*len(board)-1):
        j=0
        diagonal=""
        while True:
            if(i-j <len(board) and j<len(board)):
                diagonal+=str(board[j][i-j]) 
                
            
            if(j==i or (i-j)<0):
                break
            j=j+1
        if("111" in diagonal):
            return 1
        elif("222" in diagonal):
            return 2
    
     #check other diagonal
    for i in range(0,2*len(board)-1):
        j=0
        otherDiagonal=""
        while True:
            if(i-j <len(board) and j<len(board)):
                otherDiagonal+=str(board[j][(len(board)-1)-(i-j)]) 
            
            if(j==i or (i-j)<0):
                break
            j=j+1
        if("111" in otherDiagonal):
            return 1
        elif("222" in otherDiagonal):
            return 2
        
      

    #check if full
    notFull=False
    for x in board:
        horizontal=""
        for y in x:
            horizontal+=str(y)
        if("0" in horizontal):
            notFull=True
    if(notFull==False):
        return 3
    return 0
