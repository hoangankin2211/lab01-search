from collections import deque
from queue import *
class BFS:
    def __init__(self, matrix, startPoint, endPoint):
        self.matrix = matrix
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.border = 'x'
        self.move = {
                        'up':(1, 0),
                        'down':(-1, 0),
                        'right':(0, 1),
                        'left':(0, -1),
                    } 

    def getRoute(self):
        queue = deque()
        parent = dict()

        count = 0
                
        parent[self.startPoint] = None
        queue.append(self.startPoint)

        while len(queue) > 0:
            currentPoint = queue.popleft()
            count = count + 1
            if currentPoint == self.endPoint:
                break
            for step in self.move:
                newPoint = (currentPoint[0] + self.move[step][0], currentPoint[1] + self.move[step][1])
                if self.__isInsideMap(newPoint):
                    if newPoint not in parent:
                        parent[newPoint] = currentPoint
                        queue.append(newPoint)

        print('count: '+ str(count))

        return self.__retrievePoint(parent)

        

    def __isInsideMap(self, point): ## Kiểm tra xem cái một điểm có đang nằm trong map hay không

        ## Nếu hoành độ của điểm đó lớn hơn chiều ngang hoặc bé hơn không thì trả về False
        if point[0] >= len(self.matrix) or point[0] < 0: 
            return False

        ## Nếu tung độ của điểm đó lớn hơn chiều dọc của hoặc âm thì trả về False
        if point[1] >= len(self.matrix[0]) or point[1] < 0:
            return False

        ## Nếu điểm đó trùng với tường hay biên của bản đồ thì cũng trả về False
        if self.matrix[point[0]][point[1]] == self.border:
            return False
        return True

    def __retrievePoint(self, parent): ## Dò ngược lại đường đi đã đươc lưu nhằm mục đích lấy được danh sách điểm các điểm từ start -> end
        
        ## Khởi tạo một biến đệm để lưu đường đi
        destination = self.endPoint

        ## Một danh sách để lưu lại đường đi
        retrieve = []

        expense  = 0

        ## Truy ngược lại cho đến khi nào tìm được điểm StartPoint
        while destination != self.startPoint:
            retrieve.append(destination)
            destination = parent[destination]
            expense = expense + 1

        retrieve.append(self.startPoint)
        retrieve.reverse()

        print (expense)

        return retrieve,expense
