from copy import deepcopy

class State(object):
    '''
    Represent a node in the search tree. 

    self.board  : Board object
    self.m      : # moves to reach this State
    self.parent : Previous State object 
    '''

    def __init__(self, board, m, parent):
        self.board  = board
        self.m      = m
        self.parent = parent

    def branch(self):
        ''' Returns a list of possible children from this state. '''
        branches = []
        for m in self.board.available_moves():
            b = deepcopy(self.board)
            b.move(m)
            branches.append(State(b, self.m+1, self))

        return branches

    def __lt__(self, other):
        return self.board.md() + self.m < other.board.md() + other.m

