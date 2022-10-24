import os
def createFileTxt(filename:str,expense,count,time:str):
    file = open(filename,"w+")
    file.write(str(expense))
    file.write('\n'+str(count))
    file.write('\n'+str(time))
    file.close()
    
def createFolder(folderName:str):
    os.makedirs(folderName)

def read_file(file_name):
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

def handleFile(filename):
    bonus, matrix = read_file(filename)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)
            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
            else:
                pass

    return matrix,bonus,start,end

    