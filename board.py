import logging
import math
import sys

class Board(object):
    '''
    Represents the current board state.

    self.grid  : 2D list storing the tiles at their respective locations. 
    self.goal  : dictionary maps tiles to 2-tuples representing goal locations.
                 = { 0 : (0,0) , 1 : (1,0) , ... }
    self.space : 2-tuple representing the location of the empty tile.
    '''

    def __init__(self, grid):

        self.grid = grid
        self.goal = { i : ( (i-1) // len(self.grid), (i-1) % len(self.grid)) 
                for i in range(1, len(grid)**2) }

        self.goal[0] = (2,2)

        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == 0:
                    self.space = i,j

    def md(self):
        ''' Returns Manhattan Distance. '''
        dist = 0
        for i in (range(len(self.grid)**2)):
            x, y = i % len(self.grid), i // len(self.grid)

            v = self.grid[x][y]

            # skip the space
            if v == 0:
                continue

            offset_x = abs( x - self.goal[v][0] )
            offset_y = abs( y - self.goal[v][1] )

            dist += offset_x + offset_y 

        return dist

    def available_moves(self):
        '''
        Returns a list of 2-tuples where the empty tile can move. 
        '''
        moves = []
        x,y   = self.space

        if x > 0:
            moves.append( (x-1, y) )
        if x < len(self.grid) - 1:
            moves.append( (x+1, y) )
        if y > 0:
            moves.append( (x, y-1) )
        if y < len(self.grid) - 1:
            moves.append( (x, y+1) )

        return moves

    def move(self, loc):
        '''
        Switch the locations of self.space and loc. 
        '''
        x, y = loc
        i, j = self.space

        self.grid[i][j] = self.grid[x][y]
        self.grid[x][y] = 0

        self.space = x,y

    def __str__(self):
        ans = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                ans += str(self.grid[i][j]) 
                if (j != len(self.grid)-1):
                  ans += ' '

            ans = ans.replace('0', ' ')
            ans += '\n'

        return ans
