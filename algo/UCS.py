
from dis import dis
from algo.priority_queue import PriorityQueue

def cost(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])
class UCS:
    def __init__(self, matrix, startPoint, endPoint):
        self.matrix = matrix
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.border = 'x'
        self.move = {'up':(1, 0),'down':(-1, 0),'right':(0, 1),'left':(0, -1)}

    def getRoute(self):
        listAdjacent = PriorityQueue()
        parent = dict()
        distance = dict()

        listAdjacent.insert(self.startPoint,0)
        parent[self.startPoint] = None

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                distance[(i, j)] = float("inf")

        distance[self.startPoint] = 0
        while not listAdjacent.isEmpty:
            currentPoint,priority = listAdjacent.pop()
            if currentPoint == self.endPoint:
                break
            if priority > distance[currentPoint]:
                continue
            for step in self.move:
                nextPoint = (currentPoint[0] + self.move[step][0], currentPoint[1]+ self.move[step][1])
                if self.__isInsideMap(nextPoint):
                    costTemp = cost(currentPoint, self.endPoint)
                    nextPointDistance = distance[currentPoint] + costTemp
                    if distance[nextPoint] <= nextPointDistance:
                        continue   
                    listAdjacent.insert(nextPoint,nextPointDistance)
                    parent[nextPoint] = currentPoint
                    distance[nextPoint] = nextPointDistance
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
