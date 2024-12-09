from heapq import *
from time import perf_counter
tic=perf_counter()
with open("data/input09.txt") as f:
    inp=f.read().strip()

def arith(start,nb):
    return (start+start+nb-1)*nb//2

def firstBeforePos(voids,pos,sz):
    ibest=None
    best=pos
    for i in range(sz,10):
        if voids[i] and voids[i][0][0]<best:
            ibest=i
            best=voids[i][0][0]
    return ibest

def solve(inp,ispart2):
    res=0
    pos=0
    voids,blocks=[[] for k in range(10)],[]
    for i,x in enumerate(inp.strip()):
        length=int(x)
        if i%2==0: blocks.append([pos,length])
        else: heappush(voids[length],(pos,length))
        pos+=length
    numbl=len(blocks)-1
    freebl=0
    while numbl>=0:
        pos,sz=blocks[numbl]
        if sz>0:
            nb=1
            if ispart2:
                nb=sz
            i=firstBeforePos(voids,pos,nb)           
            blocks[numbl][1]=sz-nb
            if i:
                freebl,blsz=heappop(voids[i])
                heappush(voids[blsz-nb],(freebl+nb,blsz-nb))
                res+=arith(freebl,nb)*numbl
            else:
                res+=arith(pos+sz-nb,nb)*numbl
        else:
            numbl-=1
    return res

part1,part2=solve(inp,False),solve(inp,True)
print(part1,part2)