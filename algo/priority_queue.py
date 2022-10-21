class PriorityQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
 
    def insert(self, item, priority):
        self.queue.append({'item': item, 'priority': priority })
    
    def pop(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i]['priority'] > self.queue[max_val]['priority']:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item["item"],item["priority"]
        except IndexError:
            print()
    
