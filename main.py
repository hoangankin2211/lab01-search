from algo.GBFS import GBFS
from visualize_map import*

from algo.BFS import *


bonus, matrix = read_file( 'maze_map.txt')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='S':
            start=(i,j)

        elif matrix[i][j]==' ':
            if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                end=(i,j)
            
        else:
            pass

print(start)
print(end)

route =GBFS(matrix, start, end).solve()
visualize_maze(matrix,bonus,start,end,route)