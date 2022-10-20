
from algo.Map import Map


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, item, data):
        self.queue.append({'item': item, 'data': data })

    # for popping an element based on Priority
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


class GBFS(Map):
    def __init__(self, matrix, startPoint, endPoint):
        super().__init__(matrix, startPoint, endPoint)

    def heuristic(self, start, end):
        return abs(start[0] - start[1]) + abs(end[0] - end[1])
    
    def solve(self):
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

                if not self.isInsideMap(nextItem):
                    continue
                    
                if nextItem not in result:
                    pq.insert(nextItem, self.heuristic(nextItem, self.endPoint))
                    result[nextItem] = item
        return self.getPath(result)

