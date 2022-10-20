import os
import matplotlib.pyplot as plt

with open('maze_map.txt', 'w') as outfile:
  outfile.write('2\n')
  outfile.write('3 6 -3\n')
  outfile.write('5 14 -1\n')
  outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
  outfile.write('x   x   xx xx        x\n')
  outfile.write('x     x     xxxxxxxxxx\n')
  outfile.write('x x   +xx  xxxx xxx xx\n')
  outfile.write('  x   x x xx   xxxx  x\n')
  outfile.write('x          xx +xx  x x\n')
  outfile.write('xxxxxxx x      xx  x x\n')
  outfile.write('xxxxxxxxx  x x  xx   x\n')
  outfile.write('x          x x Sx x  x\n')
  outfile.write('xxxxx x  x x x     x x\n')
  outfile.write('xxxxxxxxxxxxxxxxxxxxxx')

def visualize_maze(matrix, bonus, start, end, route=None):
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']

    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('v') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('^') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('>')
            else:
                direction.append('<')
        direction.pop(0)
    ax=plt.figure(dpi=100).add_subplot(111)
    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)
    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')
    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')
    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')
    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1],-route[i+1][0],
                        marker=direction[i],color='silver')
    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')
    
    for _, point in enumerate(bonus):
      print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')

def read_file(file_name: str = 'maze.txt'):
  f=open(file_name,'r')
  n_bonus_points = int(next(f)[:-1])
  bonus_points = []
  for i in range(n_bonus_points):
    x, y, reward = map(int, next(f)[:-1].split(' '))
    bonus_points.append((x, y, reward))

  text=f.read()
  matrix=[list(i) for i in text.splitlines()]
  f.close()

  return bonus_points, matrix


bonus_points, matrix = read_file('maze_map.txt')

print(f'The height of the matrix: {len(matrix)}')
print(f'The width of the matrix: {len(matrix[0])}')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='S':
            start=(i,j)

        elif matrix[i][j]==' ':
            if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                end=(i,j)     
        else:
            pass

# visualize_maze(matrix,bonus_points,start,end)