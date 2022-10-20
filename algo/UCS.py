from collections import deque
from queue import *
class UCS:
    def __init__(self, matrix, startPoint, endPoint):
        self.matrix = matrix
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.border = 'x'
        self.move = {'up':(1, 0),'down':(-1, 0),'right':(0, 1),'left':(0, -1)}

    def getRoute(self):
        opened = []
        listAdjacent = PriorityQueue()
        parent = dict()
        distance = dict()

        opened.append(self.startPoint)
        listAdjacent.put([0,self.startPoint])
        
        while listAdjacent.not_empty:
            currentPoint = listAdjacent.get()
            if currentPoint == self.endPoint:
                break



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
