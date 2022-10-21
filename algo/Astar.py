
from math import sqrt
from algo.priority_queue import PriorityQueue

def calculateDistance(start, end):
    return sqrt( pow(abs(start[0] - end[0]),2) + pow(abs(start[1] - end[1]),2) )

class Astar:
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
        if (current2start==0):
            return 0
        return float(current2end)/float(current2start)

    ## Xét theo tổng hoành độ và tung độ  
    def heuristic3(self, point): 
        return abs(point[0] - self.endPoint[0]) + abs(point[1] - self.endPoint[1])


    def getRoute(self):

        waitingQueue = PriorityQueue() 
        parent = dict()
        distance = dict()

        waitingQueue.insert(self.startPoint,0)
        parent[self.startPoint] = None
        distance[self.startPoint] = 0

        count = 0

        while waitingQueue.isEmpty != True:
            currentPoint,priority = waitingQueue.pop()
            count = count + 1
            if currentPoint == self.endPoint:
                break
            
            if priority > distance[currentPoint]:
                continue
            
            for step in self.move:
                
                nextPoint = (currentPoint[0] + self.move[step][0], currentPoint[1]+ self.move[step][1])

                if self.__isInsideMap(nextPoint):
                    nextPointDistance = float(distance[currentPoint]) + float(calculateDistance(currentPoint,nextPoint)) + float(self.heuristic2(nextPoint))
                    
                    if (nextPoint not in distance) or  (distance[nextPoint] > nextPointDistance): ## Nếu (chưa được mở) hoặc (nếu đã mở mà khoảng cách mới bé hơn)   
                        waitingQueue.insert(nextPoint,nextPointDistance) ##Thêm lại vào danh sách kề
                        parent[nextPoint] = currentPoint        ##Lưu lại đường đi
                        distance[nextPoint] = nextPointDistance ##Lưu lại khoảng cách từ điểm mới đến vị trí bắt đầu

        print('count' + str(count))

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

