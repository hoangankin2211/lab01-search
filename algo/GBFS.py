
from math import sqrt
from algo.priority_queue import PriorityQueue

class GBFS:
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


    ## Xét điểm đó có gần đích hơn hay không
    def heuristic1(self, point): 
        return sqrt(pow(point[0] - self.endPoint[0],2) + pow(point[1] - self.endPoint[1],2))

    ## Xét theo tỉ lệ (khoảng cách điểm kết thúc đến điểm hiện tại) và (khoảng cách giữa điểm bắt đầu đến điểm hiện tại) 
    ## => Điểm nào có tỉ lệ nhỏ hơn thì chọn
    def heuristic2(self, point):  
        current2end = sqrt(pow(point[0] - self.endPoint[0],2) + pow(point[1] - self.endPoint[1],2))
        current2start = sqrt(pow(point[0] - self.startPoint[0],2) + pow(point[1] - self.startPoint[1],2))
        return float(current2end)/float(current2start)

    ## Xét theo tổng hoành độ và tung độ  
    def heuristic3(self, point): 
        return abs(point[0] - self.endPoint[0]) + abs(point[1] - self.endPoint[1])

    
    def getRoute(self):
        waitingQueue = PriorityQueue()
        waitingQueue.insert(self.startPoint, 0)

        count = 0

        parent = dict()
        parent[self.startPoint] = None

        while not waitingQueue.isEmpty():
            currentPoint,_ = waitingQueue.pop()
            count = count + 1
            if currentPoint == self.endPoint:
                break
            for step in self.move:
                nextCurrentPoint = (currentPoint[0] + self.move[step][0], currentPoint[1]+ self.move[step][1])

                if not self.__isInsideMap(nextCurrentPoint):
                    continue
                    
                if nextCurrentPoint not in parent:
                    waitingQueue.insert(nextCurrentPoint, self.heuristic3(nextCurrentPoint))
                    parent[nextCurrentPoint] = currentPoint

        print('count'+ str(count))
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

        expense = 0

        ## Truy ngược lại cho đến khi nào tìm được điểm StartPoint
        while destination != self.startPoint:
            retrieve.append(destination)
            destination = parent[destination]
            expense = expense + 1

        retrieve.append(self.startPoint)
        retrieve.reverse()
        
        return retrieve,expense

