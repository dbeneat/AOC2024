import re
with open("data/input14.txt") as f:
    pattern="p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    robots=[[int(x) for x in line] for line in re.findall(pattern,f.read())]
W,H=101,103

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

for t in range(100,10000):
    buffer=[[" "]*W for i in range(H)]
    for r in robots:
        x,y,_,_=r
        buffer[y][x]="*"
        update(r,1)
    c=False
    for y in range(H):
        c=c or "*********" in "".join(buffer[y])
    if c:
        print("time=",t)
        for line in buffer:
            print("".join(line))
        part2=t
        break

print(part1,part2)