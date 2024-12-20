from collections import defaultdict
with open("data/input20.txt") as f:
    G=[list(x) for x in f.read().strip().split("\n")]
H,W=len(G),len(G[0])
sx,sy,ex,ey=0,0,0,0
for y in range(1,W-1):
    for x in range(1,W-1):
        if G[y][x]=="S":sx,sy=x,y
        if G[y][x]=="E":ex,ey=x,y

def distMap(start,end):
    sx,sy=start
    ex,ey=end
    Q=[(0,sx,sy)]
    seen=set()
    dist=defaultdict(lambda:999999)
    dist[(sx,sy)]=0
    while Q:
        u=Q.pop(0)
        d,x,y=u
        if (x,y) in seen:continue
        dist[(x,y)]=d
        if (x,y)==(ex,ey):
            return dist
        seen.add((x,y))        
        if x>0 and G[y][x-1]!='#':Q.append((d+1,x-1,y))
        if x<W-1 and G[y][x+1]!='#':Q.append((d+1,x+1,y))
        if y>0 and G[y-1][x]!='#':Q.append((d+1,x,y-1))
        if y<H-1 and G[y+1][x]!='#':Q.append((d+1,x,y+1))

dist1=distMap((sx,sy),(ex,ey))
dist2=distMap((ex,ey),(sx,sy))
D=dist1[(ex,ey)]

part1,part2=0,0
for x in range(1,W-1):
    for y in range(1,H-1):
        if G[y][x]=="#":continue
        d1=dist1[(x,y)]
        for xx in range(max(1,x-20),min(W-1,x+21)):
            for yy in range(max(1,y-20),min(H-1,y+21)):
                if G[yy][xx]=="#":continue
                d2=dist2[(xx,yy)]
                d3=abs(x-xx)+abs(y-yy)
                if d3<=20:
                    d=d1+d2+d3
                    if d3==2 and d<=D-100: part1+=1
                    if d<=D-100: part2+=1
print(part1,part2)