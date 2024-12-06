with open("data/input06.txt") as f:
    L=f.read().split()
W,H=len(L),len(L[0])
obst=set()
for y in range(H):
    for x in range(W):
        if L[y][x]=="#": obst.add((x,y))
        if L[y][x]=="^": start=(x,y)

d=((0,-1),(1,0),(0,1),(-1,0))
def walk(obstx,obsty):
    h=0
    pos=[start[0],start[1]]
    seenstates,seenpos = set(),set()
    seenstates.add((pos[0],pos[1],h))
    while True:
        x,y=pos
        if x<0 or x>=W or y<0 or y>=H:
            return seenpos,False
        seenpos.add((x,y))
        dx,dy=d[h]
        if (x+dx,y+dy) in obst or (x+dx==obstx and y+dy==obsty):
            h=(h+1)%4
        else:
            pos[0]+=dx;pos[1]+=dy
            state=(pos[0],pos[1],h)
            if state in seenstates:
                return seenpos,True
            seenstates.add(state)
            
seen,_=walk(None,None)
part1=len(seen)
part2=sum(walk(x,y)[1] for x,y in seen if (x,y)!=start)