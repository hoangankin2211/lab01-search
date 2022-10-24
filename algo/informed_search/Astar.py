
from math import sqrt
from algo.informed_search.heuristic import heuristic1,heuristic2,heuristic3

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

    def solve(self,heuristic):

        count = 0

        waitingQueue = PriorityQueue() 
        parent = dict()
        distance = dict()

        waitingQueue.insert(self.startPoint,0)
        parent[self.startPoint] = None
        distance[self.startPoint] = 0


        while waitingQueue.isEmpty != True:
            currentPoint,priority = waitingQueue.pop()
            if currentPoint == self.endPoint:
                break
            
            if priority > distance[currentPoint]:
                continue
            
            for step in self.move:
                nextPoint = (currentPoint[0] + self.move[step][0], currentPoint[1]+ self.move[step][1])
                if self.__isInsideMap(nextPoint):
                    count = count + 1
                    if (heuristic == 'heuristic1'):
                        nextPointDistance = float(distance[currentPoint]) + float(calculateDistance(currentPoint,nextPoint)) + float(heuristic1(nextPoint,self.endPoint))
                    elif (heuristic == 'heuristic2'):
                        nextPointDistance = float(distance[currentPoint]) + float(calculateDistance(currentPoint,nextPoint)) + float(heuristic2(nextPoint,self.startPoint,self.endPoint))   
                    else:
                        nextPointDistance = float(distance[currentPoint]) + float(calculateDistance(currentPoint,nextPoint)) + float(heuristic3(nextPoint,self.endPoint))
                    
                    if (nextPoint not in distance) or  (distance[nextPoint] > nextPointDistance): ## Nếu (chưa được mở) hoặc (nếu đã mở mà khoảng cách mới bé hơn)   
                        waitingQueue.insert(nextPoint,nextPointDistance) ##Thêm lại vào danh sách kề
                        parent[nextPoint] = currentPoint        ##Lưu lại đường đi
                        distance[nextPoint] = nextPointDistance ##Lưu lại khoảng cách từ điểm mới đến vị trí bắt đầu


        return self.__retrievePoint(parent),count



    def getRoute(self):
        (route1,expense1),count1 = self.solve("heuristic1")
        (route2,expense2),count2 = self.solve("heuristic2")
        (route3,expense3),count3 = self.solve("heuristic3")

        return (route1,route2,route3),(expense1,expense2,expense3),(count1,count2,count3)



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


        return retrieve,expense

