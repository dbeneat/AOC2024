from heapq import *
from collections import defaultdict
with open("data/input18.txt") as f:
    L=f.read().strip().split("\n")
obst=defaultdict(lambda:999999)
for i,line in enumerate(L):
    x,y=[int(k) for k in line.split(",")] 
    obst[(x,y)]=i

def solveFor(k):
    W,H=71,71
    sx,sy,ex,ey=0,0,W-1,H-1
    seen = set()
    dist=defaultdict(lambda:999999)
    dist[(sx,sy)]=0
    Q = []
    for y in range(H):
        for x in range(W):
                if (x,y)==(sx,sy): heappush(Q,(0,(x,y)))
                else: heappush(Q,(999999,(x,y)))
    while Q:
        d,u = heappop(Q)
        x,y=u
        if (x,y)==(ex,ey):
            break
        if (x,y) in seen:
            continue
        seen.add((x,y))
        for xx,yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if xx<0 or xx>=W or yy<0 or yy>=H: continue
            if obst[(xx,yy)]<=k: continue
            if (xx,yy) not in seen:
                newdist = d+1
                if newdist<=dist[(xx,yy)]:
                    dist[(xx,yy)]=newdist
                    heappush(Q,(newdist,(xx,yy)))
    return dist[(ex,ey)]

part1=solveFor(1024)

left,right=1024,len(L)-1
while right-left>1:
    middle=(left+right)//2
    if solveFor(middle)==999999:
        right=middle
    else:
        left=middle
part2=L[right]

print(part1,part2)