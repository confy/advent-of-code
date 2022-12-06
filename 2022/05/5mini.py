import copy,re,collections
with open('./2022/05/input.txt')as f:raw_stack,raw_moves=f.read().split('\n\n')
stacks_p1=collections.defaultdict(list)
for row in reversed(raw_stack.split('\n')[:-1]):
	for (stack,crate) in enumerate(row[1::4],start=1):
		if crate!=' ':stacks_p1[stack].append(crate)
stacks_p2=copy.deepcopy(stacks_p1)
moves=[tuple(map(int,re.findall('\\d+',line)))for line in raw_moves.split('\n')]
for move in moves:
	for i in range(move[0]):stacks_p1[move[2]].append(stacks_p1[move[1]].pop())
	stacks_p2[move[2]].extend(stacks_p2[move[1]][-move[0]:]);del stacks_p2[move[1]][-move[0]:]
print(''.join([stack[-1]for stack in stacks_p1.values()]),''.join([stack[-1]for stack in stacks_p2.values()]))