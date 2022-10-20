
# class Map:
#     def __init__(self, matrix, startPoint, endPoint):
#         self.matrix = matrix
#         self.startPoint = startPoint
#         self.endPoint = endPoint
#         self.border = 'x'
#         self.move = {'up': (1, 0),'down': (-1, 0),'right':(0, 1),'left': (0, -1)}

#     def isInsideMap(self, point):
#         if point[0] >= len(self.matrix) or point[0] < 0:
#             return False
#         if point[1] >= len(self.matrix[0]) or point[1] < 0:
#             return False
#         if self.matrix[point[0]][point[1]] == self.border:
#             return False
#         return True

#     def getPath(self, trace):
#         current = self.endPoint
#         path = []

#         while current != self.startPoint:
#             path.append(current)
#             current = trace[current]

#         path.append(self.startPoint)
#         path.reverse()

#         return path