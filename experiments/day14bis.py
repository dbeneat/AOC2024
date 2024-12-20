import re
import zlib
import matplotlib.pyplot as plt
with open("data/input14.txt") as f:
    pattern="p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    robots=[[int(x) for x in line] for line in re.findall(pattern,f.read())]
W,H=101,103

def complexity(string):
    return len(zlib.compress(string.encode()))

def update(robot,steps):
    x,y,vx,vy=robot
    robot[0]=(x+steps*vx)%W
    robot[1]=(y+steps*vy)%H


for r in robots:
    update(r,100)
a=len([r for r in robots if r[0]<(W-1)//2 and r[1]<(H-1)//2])
b=len([r for r in robots if r[0]<(W-1)//2 and r[1]>(H-1)//2])
c=len([r for r in robots if r[0]>(W-1)//2 and r[1]<(H-1)//2])
d=len([r for r in robots if r[0]>(W-1)//2 and r[1]>(H-1)//2])
part1=a*b*c*d

T=[]
compl=[]
for t in range(100,9000):
    buffer=[[" "]*W for i in range(H)]
    for r in robots:
        x,y,_,_=r
        buffer[y][x]="*"
        update(r,1)
    string=""
    for y in range(H):
        for x in range(W):
            string+=buffer[y][x]
    T.append(t)
    compl.append(complexity(string))

plt.plot(T,compl)
plt.show()

indMin=compl.index(min(compl))
print(T[indMin])