with open("data/input15.txt") as f:
    A,B=f.read().strip().split("\n\n")
A=A.split("\n")
H,W=len(A),len(A[0])

walls,boxes=set(),set()
px,py=0,0
for y in range(H):
    for x in range(W):
        ch=A[y][x]
        if ch=="#": walls.add((x,y))
        if ch=="O": boxes.add((x,y))
        if ch=="@": px,py=x,y

def go(dx,dy):
    global px,py
    nx,ny=px+dx,py+dy
    if (nx,ny) in walls: return
    if (nx,ny) not in boxes: px,py=nx,ny; return
    a,b=nx,ny
    while (a,b) in boxes: a,b=a+dx,b+dy
    if (a,b) in walls: return
    boxes.remove((nx,ny))
    boxes.add((a,b))
    px,py=nx,ny
            
for code in B:
    if code=="<": go(-1,0)
    if code==">": go(1,0)
    if code=="^": go(0,-1)
    if code=="v": go(0,1)
    
part1=sum(100*y+x for (x,y) in boxes)

def canpush(x,y,dx,dy,L):
    nx,ny=x+dx,y+dy
    if (nx,ny) in walls: return False
    if (nx,ny) in boxes and (nx,ny) not in L:
        L.add((nx,ny)); return canpush(nx,ny,dx,dy,L) and canpush(nx+1,ny,dx,dy,L)
    if (nx-1,ny) in boxes and (nx-1,ny) not in L:
        L.add((nx-1,ny)); return canpush(nx,ny,dx,dy,L) and canpush(nx-1,ny,dx,dy,L)
    return True

def trypush(x,y,dx,dy):
    L=set()
    if canpush(x,y,dx,dy,L):
        for (x,y) in L: boxes.remove((x,y))
        for (x,y) in L: boxes.add((x+dx,y+dy))
        return True
    return False

walls,boxes=set(),set()
for y in range(H):
    for x in range(W):
        ch=A[y][x]
        if ch=="#": walls.add((2*x,y));walls.add((2*x+1,y))
        if ch=="O": boxes.add((2*x,y))
        if ch=="@": px,py=2*x,y
for code in B:
        if code=="<" and trypush(px,py,-1,0):px-=1
        if code==">" and trypush(px,py,1,0):px+=1
        if code=="^" and trypush(px,py,0,-1):py-=1
        if code=="v" and trypush(px,py,0,1):py+=1

part2=sum(100*y+x for (x,y) in boxes)
print(part1,part2)