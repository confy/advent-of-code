from operator import itemgetter
with open('./2022/12/input.txt')as f:data=f.read().splitlines()
grid={}
queue=[]
for (y,line) in enumerate(data):
	for (x,char) in enumerate(line):
		if char=='S':grid[(x,y)]=['a',None]
		elif char=='E':grid[(x,y)]=['z',None];queue.append([(x,y),0])
		else:grid[(x,y)]=[char,None]
grid[queue[0][0]][1]=0
while True:
	queue.sort(key=itemgetter(1));cell=queue.pop(0)
	for i in {(cell[0][0]+1,cell[0][1]),(cell[0][0],cell[0][1]+1),(cell[0][0]-1,cell[0][1]),(cell[0][0],cell[0][1]-1)}:
		if i in grid and grid[i][1]is None and ord(grid[i][0])>=ord(grid[cell[0]][0])-1:
			if grid[i][0]=='a':print(cell[1]+1);exit()
			grid[i][1]=cell[1]+1;queue.append([i,cell[1]+1])