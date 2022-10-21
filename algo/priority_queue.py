from tokenize import Double


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
 
    def insert(self, item, priority):
        self.queue.append({'item': item, 'priority': priority })
    
    def pop(self):
        try:
            min_val = 0
            for i in range(len(self.queue)):
                if float(self.queue[i]['priority']) < float(self.queue[min_val]['priority']):
                    min_val = i
            item = self.queue[min_val]
            del self.queue[min_val]
            return item["item"],item["priority"]
        except IndexError:
            print()
    
