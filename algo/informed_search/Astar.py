
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
                    
                    if (nextPoint not in distance) or  (distance[nextPoint] > nextPointDistance): ## N???u (ch??a ???????c m???) ho???c (n???u ???? m??? m?? kho???ng c??ch m???i b?? h??n)   
                        waitingQueue.insert(nextPoint,nextPointDistance) ##Th??m l???i v??o danh s??ch k???
                        parent[nextPoint] = currentPoint        ##L??u l???i ???????ng ??i
                        distance[nextPoint] = nextPointDistance ##L??u l???i kho???ng c??ch t??? ??i???m m???i ?????n v??? tr?? b???t ?????u


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

        expense  = 0

        ## Truy ng?????c l???i cho ?????n khi n??o t??m ???????c ??i???m StartPoint
        while destination != self.startPoint:
            retrieve.append(destination)
            destination = parent[destination]
            expense = expense + 1

        retrieve.append(self.startPoint)
        retrieve.reverse()


        return retrieve,expense

