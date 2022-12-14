
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



    def __isInsideMap(self, point): ## Ki???m tra xem c??i m???t ??i???m c?? ??ang n???m trong map hay kh??ng
        ## N???u ho??nh ????? c???a ??i???m ???? l???n h??n chi???u ngang ho???c b?? h??n kh??ng th?? tr??? v??? False
        if point[0] >= len(self.matrix) or point[0] < 0: 
            return False
        ## N???u tung ????? c???a ??i???m ???? l???n h??n chi???u d???c c???a ho???c ??m th?? tr??? v??? False
        if point[1] >= len(self.matrix[0]) or point[1] < 0:
            return False
        ## N???u ??i???m ???? tr??ng v???i t?????ng hay bi??n c???a b???n ????? th?? c??ng tr??? v??? False
        if self.matrix[point[0]][point[1]] == self.border:
            return False
        return True

    def __retrievePoint(self, parent): ## D?? ng?????c l???i ???????ng ??i ???? ??????c l??u nh???m m???c ????ch l???y ???????c danh s??ch ??i???m c??c ??i???m t??? start -> end
        
        ## Kh???i t???o m???t bi???n ?????m ????? l??u ???????ng ??i
        destination = self.endPoint

        ## M???t danh s??ch ????? l??u l???i ???????ng ??i
        retrieve = []

        expense = 0

        ## Truy ng?????c l???i cho ?????n khi n??o t??m ???????c ??i???m StartPoint
        while destination != self.startPoint:
            retrieve.append(destination)
            destination = parent[destination]
            expense = expense + 1

        retrieve.append(self.startPoint)
        retrieve.reverse()
        
        return retrieve,expense

