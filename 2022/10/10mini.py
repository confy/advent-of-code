with open("./2022/10/input.txt") as f:o=[line.strip()for line in f]
x=1;c=0;t=0;b=0;p=0;l=0
for i in range(240):
    if b>39:b=0;print("")
    if b<=x+1 and b>=x-1:print("#",end="")
    else:print(" ",end="")
    if c in[20,60,100,140,180,220]:t+=(c*x)
    if p==False:
        if o[l]=="noop":c+=1;b+=1;l+=1
        elif o[l][:4]=="addx":p=True;c+=1;b+=1
    elif p==True:c+=1;b+=1;x+=int(o[l][4:]);l+=1;p=False

print(t)