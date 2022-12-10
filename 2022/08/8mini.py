with open('./2022/08/input.txt')as f:fields=[line.strip()for line in f.readlines()]
part_1, part_2=0,[]
for (i,line) in enumerate(fields):
	for (j,tree) in enumerate(line):
		if i==0 or i==len(fields)-1 or j==0 or j==len(line)-1:part_1+=1;continue
		east=[int(t)for t in line[j+1:]];west=[int(t)for t in line[:j]][::-1];north=[int(l[j])for(k,l)in enumerate(fields)if k<i][::-1];south=[int(l[j])for(k,l)in enumerate(fields)if k>i];visible=False;score=1
		for direction in [east,west,north,south]:
			dist=0
			for t in direction:
				dist+=1
				if t>=int(tree):break
			score*=dist
			if not visible and int(tree)>max(direction):part_1+=1
		part_2.append(score)
print(part_1,max(part_2))