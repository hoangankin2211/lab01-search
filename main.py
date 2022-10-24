
from genericpath import isdir, isfile
import sys
import getopt
import time
import matplotlib.pyplot as plt

from algo.informed_search.Astar import Astar
from algo.informed_search.GBFS import GBFS

from algo.uninformed_search.DFS import DFS
from algo.uninformed_search.UCS import UCS
from algo.uninformed_search.BFS import BFS

from handle_file import createFileTxt, handleFile,createFolder
from visualize_map import*

from os import times, walk

############# Tham khỏa: 
# https://github.com/trhgquan/CS143/tree/main/Lab-01?fbclid=IwAR1z_yTjCKJzulY4QOzL5q5Kb-UbZOsd6yld0a1cojGByE5nhMVilnLzKK4
# https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/#:~:text=isdir()-,os.,the%20method%20will%20return%20True.



#################################################
## Tiến hành tìm đường đi
def run(file_name_input: str,algorithm : str):
    outputPath = 'output' + file_name_input[file_name_input.find('/'):file_name_input.find('.')] + '/' + algorithm + '/'

    if (not isdir(outputPath)):
        createFolder(outputPath)


    matrix,bonus,start,end = handleFile(file_name_input)

    handleAlgorithm = {
                        'bfs':BFS(matrix,start,end).getRoute(),
                        'dfs':DFS(matrix,start,end).getRoute(),
                        'ucs':UCS(matrix,start,end).getRoute(),
                        'gbfs':GBFS(matrix,start,end).getRoute(),
                        'astar':Astar(matrix,start,end).getRoute(),
                    }

    beginTime = time.time()
    if (algorithm in ['bfs','dfs','ucs']):
        (route,expense),count = handleAlgorithm[algorithm]
    elif (algorithm in ['gbfs','astar']):
        (route1,route2,route3),(expense1,expense2,expense3),(count1,count2,count3) = handleAlgorithm[algorithm]
    else:
        print('ALGORITHM NOT EXISTS')
    endTime = time.time()

    countTime = str(float(endTime)*1000-float(beginTime)*1000)

    if (algorithm == 'bfs' or algorithm == 'dfs' or algorithm == 'ucs'):
        print('NAME OF THE ALGORITHM: '+ str(algorithm))
        print("EXPENSE: "+ str(expense))
        visualize_maze(matrix, bonus, start, end, route).savefig(outputPath + algorithm+'.jpg')
        createFileTxt(outputPath + algorithm+'.txt',expense,count,countTime)
    else:
        print('NAME OF THE ALGORITHM: '+ str(algorithm))
        
        print("EXPENSE 1: "+ str(expense1))
        visualize_maze(matrix, bonus, start, end, route1).savefig(outputPath + algorithm+'_heuristic_1.jpg')
        createFileTxt(outputPath + algorithm+'_heuristic_1.txt',expense1,count1,countTime)
        
        print("EXPENSE 2: "+ str(expense2))
        visualize_maze(matrix, bonus, start, end, route2).savefig(outputPath + algorithm+'_heuristic_2.jpg')
        createFileTxt(outputPath + algorithm+'_heuristic_2.txt',expense2,count2,countTime)
        
        print("EXPENSE 3: "+ str(expense3))
        visualize_maze(matrix, bonus, start, end, route3).savefig(outputPath + algorithm+'_heuristic_3.jpg')
        createFileTxt(outputPath + algorithm+'_heuristic_3.txt',expense3,count3,countTime)

    print('\n')


argv = sys.argv[1:]

try:
    command_line, _ = getopt.getopt(
                            argv, 
                            'input:algo:output:', 
                            ["file_name_input=","algorithm=","file_name_output="])
    
    for (service, command) in command_line:
        if service in ['-input','--file_name_input']:
            file_name_input = command
        elif service in ['--algo','--algorithm']:
            algorithm = command
        elif service in ['-output','--file_name_output']:
            file_name_output = command
        else:
            print("Command Invalid Or Some errors occur. Please check your command line")
            sys.exit(1)

    if len(file_name_input) == 0 or len(file_name_output) == 0 or len(algorithm) == 0:
        sys.exit(2)


except getopt.GetoptError:
    print("Command Invalid Or Some errors occur. Please check your command line")
    sys.exit(1)

if (file_name_input == '*.txt' and algorithm == "*"):
    level__1 = 'input/level__1'
    level__2 = 'input/level__2'
    
    for (_, _, filenames) in walk(level__1):
        for filename in filenames:
            for algo in ['bfs','dfs','ucs','gbfs','astar']:
                run(level__1 + '/' + filename,algo)
    
    for (_, _, filenames) in walk(level__2):
        for filename in filenames:
            for algo in ['gbfs','astar']:
                    run(level__2 + '/' + filename,algo)


elif file_name_input == '*.txt':
    level__1 = 'input/level__1'
    level__2 = 'input/level__2'
    
    for (_, _, filenames) in walk(level__1):
        for filename in filenames:
            run(level__1 + '/' + filename,algorithm)
    
    for (_, _, filenames) in walk(level__2):
        for filename in filenames:
            run(level__2 + '/' + filename,algorithm)

elif algorithm == "*":
    for algo in ['bfs','dfs','ucs','gbfs','astar']:
        run(file_name_input,algo)

else:
    run(file_name_input,algorithm)

plt.close()
    

# Chạy code dưới dạng command-line:

# python main.py --input=<tên file input>.txt --algo=<ten thuật toán> --output=<tên file output>.png 
# Ví dụ: Chạy thuật toán A-Star trên bản đồ sample/01.txt, output ra file 01-astar.png:

# python main.py --input=sample/01.txt --output=01-astar.png --algo=astar
# Chú ý: Để trống option --algo thì chương trình sẽ in ra bản đồ không có đường đi.