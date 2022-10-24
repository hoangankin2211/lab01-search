
from math import sqrt
from algo.priority_queue import PriorityQueue
from algo.informed_search.heuristic import heuristic1,heuristic2,heuristic3

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

    def solve(self,heuristic):
        count = 0
        waitingQueue = PriorityQueue()
        waitingQueue.insert(self.startPoint, 0)


        parent = dict()
        parent[self.startPoint] = None

        while not waitingQueue.isEmpty():
            currentPoint,_ = waitingQueue.pop()
            if currentPoint == self.endPoint:
                break
            for step in self.move:
                nextCurrentPoint = (currentPoint[0] + self.move[step][0], currentPoint[1]+ self.move[step][1])
                if not self.__isInsideMap(nextCurrentPoint):
                    continue
                
                if nextCurrentPoint not in parent:
                    count = count + 1
                    if (heuristic == 'heuristic1'):
                        waitingQueue.insert(nextCurrentPoint, heuristic1(nextCurrentPoint,self.endPoint))
                    elif (heuristic == 'heuristic2'):
                        waitingQueue.insert(nextCurrentPoint, heuristic2(nextCurrentPoint,self.startPoint,self.endPoint))
                    else:
                        waitingQueue.insert(nextCurrentPoint, heuristic3(nextCurrentPoint,self.endPoint))

                    parent[nextCurrentPoint] = currentPoint

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

        expense = 0

        ## Truy ngược lại cho đến khi nào tìm được điểm StartPoint
        while destination != self.startPoint:
            retrieve.append(destination)
            destination = parent[destination]
            expense = expense + 1

        retrieve.append(self.startPoint)
        retrieve.reverse()
        
        return retrieve,expense

