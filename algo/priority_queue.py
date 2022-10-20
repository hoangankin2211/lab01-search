class PriorityQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
 
    def insert(self, item, data):
        self.queue.append({'item': item, 'data': data })
    
    def pop(self):
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
