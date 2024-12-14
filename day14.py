import re
with open("data/input14.txt") as f:
    pattern="p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    robots=[[int(x) for x in line] for line in re.findall(pattern,f.read())]
W,H=101,103

def update(robot,steps):
    x,y,vx,vy=robot
    robot[0]=(x+steps*vx)%W
    robot[1]=(y+steps*vy)%H

for i in range(100):
    LH,LV=[0]*W,[0]*H
    Hok,Vok=False,False
    for r in robots:
        if LH[r[0]]>20:
            Hok=True
        else:
            LH[r[0]]+=1
        if LV[r[1]]>20:
            Vok=True
        else:
            LV[r[1]]+=1
        update(r,1)
    if Hok:Hresidue=i
    if Vok:Vresidue=i
    
a=len([r for r in robots if r[0]<(W-1)//2 and r[1]<(H-1)//2])
b=len([r for r in robots if r[0]<(W-1)//2 and r[1]>(H-1)//2])
c=len([r for r in robots if r[0]>(W-1)//2 and r[1]<(H-1)//2])
d=len([r for r in robots if r[0]>(W-1)//2 and r[1]>(H-1)//2])
part1=a*b*c*d
for k in range(W*H):
    if k%W==Hresidue and k%H==Vresidue:
        part2=k;break
print(part1,part2)