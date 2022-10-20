from queue import *
class BFS:
    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.start = start
        self.end = end
        self.border = 'x'
        self.move = [(1, 0),(-1, 0),(0, 1),(0, -1)]

    def find(self):
        opened, queue = [], Queue()
        queue.put(self.start)
        opened.append(self.start)
        trace = {self.start: None}
        while queue.not_empty:
            currentPoint = queue.get()
            if currentPoint == self.end:
                break
            for step in self.move:
                newPoint = (currentPoint[0] + step[0], currentPoint[1] + step[1])
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
        current = self.end
        path = []

        while current != self.start:
            print(current)
            path.append(current)
            current = trace[current]

        path.append(self.start)
        path.reverse()
        return path
