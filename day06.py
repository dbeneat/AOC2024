with open("data/input06.txt") as f:
    L=f.read().split()
W,H=len(L),len(L[0])

dist=[[min(abs(x),abs(W-1-x),abs(y),abs(H-1-y)) for x in range(W)] for y in range(H)]
for y in range(H):
    for x in range(H):
        if L[y][x]=="^": start=(x,y)
        for k in range(H):
            if L[y][k]=="#":
                dist[y][x]=min(dist[y][x],abs(k-x)-1)
            if L[k][x]=="#":
                dist[y][x]=min(dist[y][x],abs(k-y)-1)

d=((0,-1),(1,0),(0,1),(-1,0))
def walk(obstx,obsty):
    h=0
    x,y=start
    seenpos,seenstates = set(),set()
    seenpos.add((x,y))
    seenstates.add((x,y,h))
    while True:
        dx,dy=d[h]
        if obstx and x!=obstx and y!=obsty: 
            k=dist[y][x]
            while k>=1:          #Raymarching!
                x+=k*dx; y+=k*dy
                k=dist[y][x]
        nx,ny=x+dx,y+dy
        if nx<0 or nx>=W or ny<0 or ny>=H:
            return seenpos,False
        if L[ny][nx]=="#" or (nx==obstx and ny==obsty):
            h=(h+1)%4
        else:
            x,y=nx,ny
            if not obstx:seenpos.add((x,y)) #in part 2, we do not use seenpos
            if (x,y,h) in seenstates:
                return seenpos,True
            seenstates.add((x,y,h))

seen,_=walk(None,None)
part1=len(seen)
part2=sum(walk(x,y)[1] for x,y in seen if (x,y)!=start)
print(part1,part2)