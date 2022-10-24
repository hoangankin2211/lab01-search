import matplotlib.pyplot as plt


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
    plt.text(end[1],-end[0],'EXIT',color='red', horizontalalignment='center', verticalalignment='center')
    plt.xticks([])
    plt.yticks([])


    # plt.show() 

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')
    
    for _, point in enumerate(bonus):
      print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')

    return plt

