import sys
from board import Board
from queue import PriorityQueue
from state import State

class PuzzleSolver(object):
    ''' Wrapper to handle file IO and apply an A* search '''

    def __init__(self):
        self.frontier = PriorityQueue()
        self.grid = []

        for i in range(3):
            row = input()
            row = [int(i) for i in row.split()]
            self.grid.append(row)

        # Simple error checking
        for row in self.grid:
            if len(row) != 3:
                sys.exit('Input invalid. Board must be 3x3')
            for n in row:
                if n < 0 or n > 8:
                    sys.exit('Board can only contain 0-8')

    def solve(self):
        # Keep track of all visited board states
        # Checking if an element is in a python set is O(1)
        visited = set() 

        # Add the initial board state to the pq
        b = Board(self.grid)
        self.frontier.put(State(board = b, m = 0, parent = None))

        # A* search
        while self.frontier:
            node = self.frontier.get()
            hashable_board = tuple((tuple(i) for i in node.board.grid))
            visited.add(hashable_board)

            # Check for goal state
            if node.board.md() == 0:
                self.print_solution(node)
                print('Solution found using {} moves!'.format(node.m))
                break

            for child in node.branch():
                hashable_board = tuple((tuple(i) for i in child.board.grid))
                if hashable_board not in visited:
                    self.frontier.put(child)

    def print_solution(self, node):
        if (node.parent):
            self.print_solution(node.parent)
        print (node.board)



if __name__ == '__main__':

    if len(sys.argv) != 1:
        sys.exit('Usage: python3 main.py < input-file.txt')

    p = PuzzleSolver().solve()


