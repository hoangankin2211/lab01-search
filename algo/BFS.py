from queue import *

from algo.Map import *


class BFS(Map):
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
                newPoint = (currentPoint[0] + step[0], currentPoint[1] + step[1])
                if self.isInsideMap(newPoint) and newPoint not in opened:
                    trace[newPoint] = currentPoint
                    opened.append(newPoint)
                    queue.put(newPoint)
                else:
                    continue

        return self.getPath(trace)
