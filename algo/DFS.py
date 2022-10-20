from algo.Map import *

class DFS:
    def __init__(self, start, end , matrix):
        super().__init__(start, end, matrix)
    def solve(self):
        opened, stack = [],[]
        result = dict() 

        result[self.start] = None
        result.append(self.start)
        stack.append(self.start)

        while len(stack) > 0:
            