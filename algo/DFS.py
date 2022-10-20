class DFS:
    def __init__(self, matrix, startPoint, endPoint):
        self.matrix = matrix
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.border = 'x'
        self.move = {'up':(1, 0),'down':(-1, 0),'right':(0, 1),'left':(0, -1)}


    def getRoute(self):
        opened, stack = [],[]
        parent = dict() 

        parent[self.startPoint] = None
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
                
                if self.__isInsideMap(nextItem):
                    if nextItem not in opened:
                        stack.append(nextItem)
                        parent[nextItem] = item

        return self.__retrievePoint(parent)

    def __isInsideMap(self, point):
        if point[0] >= len(self.matrix) or point[0] < 0:
            return False
        if point[1] >= len(self.matrix[0]) or point[1] < 0:
            return False
        if self.matrix[point[0]][point[1]] == self.border:
            return False
        return True

    def __retrievePoint(self, parent):
        destination = self.endPoint
        retrieve = []

        while destination != self.startPoint:
            retrieve.append(destination)
            destination = parent[destination]

        retrieve.append(self.startPoint)
        retrieve.reverse()
        return retrieve

            

