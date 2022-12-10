with open('./2022/08/input.txt')as f:fields=[line.strip()for line in f.readlines()]
part_1=0;part_2=[]
for (i,line) in enumerate(fields):
	for (j,tree) in enumerate(line):
		if i==0 or i==len(fields)-1 or j==0 or j==len(line)-1:part_1+=1;continue
		east=[int(t)for t in line[j+1:]];west=[int(t)for t in line[:j]];north=[int(l[j])for(k,l)in enumerate(fields)if k<i];south=[int(l[j])for(k,l)in enumerate(fields)if k>i];west.reverse();north.reverse();visible=False;score=1
		for direction in [east,west,north,south]:
			dist=0
			for t in direction:
				if t>=int(tree):dist+=1;break
				dist+=1
			score*=dist
			if not visible and int(tree)>max(direction):part_1+=1
		part_2.append(score)
print(part_1,max(part_2))