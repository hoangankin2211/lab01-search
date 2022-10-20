from algo.Map import *

class DFS(Map):
    def __init__(self, matrix, startPoint, endPoint):
        super().__init__(matrix, startPoint, endPoint)
    def solve(self):
        opened, stack = [],[]
        result = dict() 

        result[self.startPoint] = None
        opened.append(self.startPoint)
        stack.append(self.startPoint)

        while len(stack) > 0:
            item = stack[-1]
            opened.append(item)
            stack.pop()
            if item == self.endPoint:
                break
            for step in self.move:
                nextItem = (item[0] + self.move[step][0], item[1]+ self.move[step][1])
                
                if self.isInsideMap(nextItem):
                    if nextItem not in opened:
                        stack.append(nextItem)
                        result[nextItem] = item

        return self.getPath(result)

            

