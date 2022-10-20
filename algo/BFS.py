from queue import *

from algo.Map import *


class BFS:
    def __int__(self, matrix, start, end):
        self.matrix = matrix
        self.startPoint = start
        self.endPoint = end
        self.border = 'x'
        self.move = {'up': (1, 0),'down': (-1, 0),'right':(0, 1),'left': (0, -1)}

    def find(self):
        opened, queue = [], Queue()
        queue.put(self.startPoint)
        trace = {self.startPoint: None}
        while not queue.empty:
            currentPoint = queue.get()
            if currentPoint == self.endPoint:
                break
            for step in self.move:
                newPoint = (currentPoint[0] + self.move[step][0], currentPoint[1] + self.move[step][1])
                if self.__isInsideMap(newPoint) and newPoint not in opened:
                    trace[newPoint] = currentPoint
                    opened.append(newPoint)
                    queue.put(newPoint)
                else:
                    continue

        return self.__getPath(trace)


    def __isInsideMap(self, point):
        if point[0] >= len(self.matrix) or point[0] < 0:
            return False
        if point[1] >= len(self.matrix[0]) or point[1] < 0:
            return False
        if self.matrix[point[0]][point[1]] == self.border:
            return False
        return True

    def __getPath(self, trace):
        current = self.endPoint
        path = []

        while current != self.startPoint:
            path.append(current)
            current = trace[current]

        path.append(self.startPoint)
        path.reverse()
        return path
