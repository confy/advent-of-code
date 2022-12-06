import collections
def check_cipher(text,n):
	last_n=collections.deque(maxlen=n)
	for i,char in enumerate(text):
		last_n.append(char)
		if all((last_n.count(c)<=1 for c in last_n))and len(last_n)==n:return i+1
with open('./2022/06/input.txt')as f:text=f.read()
print(check_cipher(text,4),check_cipher(text,14))