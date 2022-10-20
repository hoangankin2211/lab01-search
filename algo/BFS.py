from collections import deque
from queue import *
class BFS:
    def __init__(self, matrix, startPoint, endPoint):
        self.matrix = matrix
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.border = 'x'
        self.move = {'up':(1, 0),'down':(-1, 0),'right':(0, 1),'left':(0, -1)}

    def getRoute(self):
        opened = []
        queue = Queue()
        parent = dict()
                
        queue.put(self.startPoint)
        opened.append(self.startPoint)
        parent[self.startPoint] = None
        
        while queue.not_empty:
            currentPoint = queue.get()
            if currentPoint == self.endPoint:
                break
            for step in self.move:
                newPoint = (currentPoint[0] + self.move[step][0], currentPoint[1] + self.move[step][1])
                if self.__isInsideMap(newPoint) and newPoint not in opened:
                    parent[newPoint] = currentPoint
                    opened.append(newPoint)
                    queue.put(newPoint)
                else:
                    continue

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
