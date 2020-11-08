from collections import deque
class Tree(object):
    def __init__(self,board,player):
            self.board=board
            self.value=[]
            self.children=[]
            self.parent=None
            self.player=player
        
