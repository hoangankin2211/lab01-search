from re import A
from algo.Astar import Astar
from algo.DFS import DFS
from algo.GBFS import GBFS
from algo.UCS import UCS
from handle_file import handleFile
from visualize_map import*
from algo.BFS import *


matrix,bonus,start,end = handleFile('input/point/Map8.txt')

route,expense = Astar(matrix, start, end).getRoute()
print('expense: ' + str(expense))

result = visualize_maze(matrix,bonus,start,end,route)