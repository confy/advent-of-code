with open('./2022/03/input.txt')as f:lines=[line.strip()for line in f.readlines()]
shared, scores = [], []
for line in lines:first_half=line[:len(line)//2];second_half=line[len(line)//2:];shared.append({c for c in first_half if c in second_half})
for s in shared:score=sum((ord(c)-ord('A')+27 if c.isupper()else ord(c)-ord('a')+1 for c in s));scores.append(score)
part_1, part_2=sum(scores),0
for i in range(0,len(lines),3):shared={c for c in lines[i]if c in lines[i+1]and c in lines[i+2]};part_2+=sum((ord(c)-ord('A')+27 if c.isupper()else ord(c)-ord('a')+1 for c in shared))
print(part_1,part_2)