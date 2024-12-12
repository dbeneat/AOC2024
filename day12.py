from collections import defaultdict
with open("data/input12.txt") as f:
    L=[list(x) for x in f.read().split()]
W,H=len(L),len(L[0])
area=defaultdict(int)
perim=defaultdict(int)
corners=defaultdict(int)

CC=[[0]*W for y in range(len(L))]
seen={}
numcc=0
def dfs(x,y):
    global numcc
    if (x,y) in seen:
        return
    seen[(x,y)]=True
    CC[y][x]=numcc
    if x>0 and L[y][x-1]==L[y][x]: dfs(x-1,y)
    if x<W-1 and L[y][x+1]==L[y][x]: dfs(x+1,y)
    if y>0 and L[y-1][x]==L[y][x]: dfs(x,y-1)
    if y<H-1 and L[y+1][x]==L[y][x]: dfs(x,y+1)

for y in range(H):
    for x in range(W):
        if (x,y) not in seen:
            dfs(x,y)
            numcc+=1

def get(x,y):
    global W,H
    if x<0 or x>=W or y<0 or y>=H:
        return -1
    return CC[y][x]

for y in range(H):
    for x in range(W):
        if (get(x-1,y)!=get(x,y) and get(x,y-1)!=get(x,y)) or (get(x-1,y)==get(x,y) and get(x,y-1)==get(x,y) and get(x,y)!=get(x-1,y-1)): corners[get(x,y)]+=1
        if (get(x-1,y)!=get(x,y) and get(x,y+1)!=get(x,y)) or (get(x-1,y)==get(x,y) and get(x,y+1)==get(x,y) and get(x,y)!=get(x-1,y+1)): corners[get(x,y)]+=1
        if (get(x+1,y)!=get(x,y) and get(x,y-1)!=get(x,y)) or (get(x+1,y)==get(x,y) and get(x,y-1)==get(x,y) and get(x,y)!=get(x+1,y-1)): corners[get(x,y)]+=1
        if (get(x+1,y)!=get(x,y) and get(x,y+1)!=get(x,y)) or (get(x+1,y)==get(x,y) and get(x,y+1)==get(x,y) and get(x,y)!=get(x+1,y+1)): corners[get(x,y)]+=1
        k=4
        if x>0 and CC[y][x-1]==CC[y][x]:k-=2
        if y>0 and CC[y-1][x]==CC[y][x]:k-=2
        area[CC[y][x]]+=1
        perim[CC[y][x]]+=k

         
part1=sum(area[x]*perim[x] for x in area)
part2=sum(area[x]*corners[x] for x in area)
print(part1,part2)