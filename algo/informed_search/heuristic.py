from math import sqrt

## Xét điểm đó có gần đích hơn hay không
def heuristic1(point,endPoint): 
    return sqrt(pow(point[0] - endPoint[0],2) + pow(point[1] - endPoint[1],2))

## Xét theo tỉ lệ (khoảng cách điểm kết thúc đến điểm hiện tại) và (khoảng cách giữa điểm bắt đầu đến điểm hiện tại) 
## => Điểm nào có tỉ lệ nhỏ hơn thì chọn
def heuristic2(point,startPoint,endPoint):  
    current2end = sqrt(pow(point[0] - endPoint[0],2) + pow(point[1] - endPoint[1],2))
    current2start = sqrt(pow(point[0] - startPoint[0],2) + pow(point[1] - startPoint[1],2))
    if (current2start==0):
        return 0
    return float(current2end)/float(current2start)

## Xét theo tổng hoành độ và tung độ  
def heuristic3(point,endPoint): 
    return abs(point[0] - endPoint[0]) + abs(point[1] - endPoint[1])