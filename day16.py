from heapq import *
from collections import defaultdict

with open("data/input16.txt") as f:
    G=[list(x) for x in f.read().strip().split("\n")]
H,W=len(G),len(G[0])
sx,sy,ex,ey=0,0,0,0
for y in range(H):
    for x in range(W):
        if G[y][x]=="S": sx,sy=x,y
        if G[y][x]=="E": ex,ey=x,y

def neigh(x,y,h):
    nei = []
    for hh in {'L':['L','U','D'],'R':['R','U','D'],'U':['U','L','R'],'D':['D','L','R']}[h]:
        dx,dy={'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)}[hh]
        nx,ny=x+dx,y+dy
        if G[ny][nx]!="#":
            nei.append((nx,ny,hh))
    return nei

seen = set()
dist=defaultdict(lambda:999999)
dist[(sx,sy,'R')]=0
Q = []
for y in range(H):
    for x in range(W):
        for h in ['L','R','D','U']:
            if G[y][x]=="#":
                continue
            if (x,y,h)==(sx,sy,'R'):heappush(Q,(0,(x,y,'R')))
            else: heappush(Q,(999999,(x,y,h)))
pred=defaultdict(list)               
while Q:
    d,u = heappop(Q)
    x,y,h=u
    if (x,y)==(ex,ey):
        break
    if (x,y,h) in seen:
        continue
    seen.add((x,y,h))
    for xx,yy,hh in neigh(x,y,h):
        if (xx,yy,hh) not in seen:
            if hh==h:
                deltaD=1
            else:
                deltaD=1001
            newdist = d+deltaD
            if newdist<=dist[(xx,yy,hh)]:
                dist[(xx,yy,hh)]=newdist
                heappush(Q,(newdist,(xx,yy,hh)))
                pred[(xx,yy,hh)].append((x,y,h))

def explore(x,y,h):
    G[y][x]='O'
    for xx,yy,hh in pred[(x,y,h)]:
        explore(xx,yy,hh)
            
best=min(dist[(ex,ey,h)] for h in ['L','R','U','D'])
for h in ['L','R','U','D']:
    if dist[(ex,ey,h)]==best:
        explore(ex,ey,h)

part1,part2=best,sum(line.count("O") for line in G)
print(part1,part2)