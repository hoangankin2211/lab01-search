from re import A
from algo.Astar import Astar
from algo.DFS import DFS
from algo.GBFS import GBFS
from algo.UCS import UCS
from handle_file import handleFile
from visualize_map import*
from algo.BFS import *

## Tham khỏa: https://github.com/trhgquan/CS143/tree/main/Lab-01?fbclid=IwAR1z_yTjCKJzulY4QOzL5q5Kb-UbZOsd6yld0a1cojGByE5nhMVilnLzKK4





matrix,bonus,start,end = handleFile('input/point/Map8.txt')

route,expense = Astar(matrix, start, end).getRoute()
print('expense: ' + str(expense))

result = visualize_maze(matrix,bonus,start,end,route)