
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
 
    def insert(self, item, data):
        self.queue.append({'item': item, 'data': data })

    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i]['data'] > self.queue[max_val]['data']:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item['item']
        except IndexError:
            print()


class GBFS:
    def __init__(self, matrix, startPoint, endPoint):
        self.matrix = matrix
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.border = 'x'
        self.move = {'up':(1, 0),'down':(-1, 0),'right':(0, 1),'left':(0, -1)}


    def heuristic(self, start, end):
        return abs(start[0] - start[1]) + abs(end[0] - end[1])
    
    def getRoute(self):
        pq = PriorityQueue()
        pq.insert(self.startPoint, 0)

        result = dict()
        result[self.startPoint] = None

        while not pq.isEmpty():
            item = pq.delete()
            print(item) 
            if item == self.endPoint:
                break
            for step in self.move:
                nextItem = (item[0] + self.move[step][0], item[1]+ self.move[step][1])

                if not self.__isInsideMap(nextItem):
                    continue
                    
                if nextItem not in result:
                    pq.insert(nextItem, self.heuristic(nextItem, self.endPoint))
                    result[nextItem] = item
        return self.__retrievePoint(result)

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

