with open("data/input09.txt") as f:
    inp=f.read().strip()

def arith(start,nb):
    return (start+start+nb-1)*nb//2

def solve(inp,ispart2):
    inp+="9"
    res=0
    pos=0
    voids,blocks=[],[]
    for i,x in enumerate(inp.strip()):
        length=int(x)
        if i%2==0: blocks.append([pos,length])
        else: voids.append([pos,length])
        pos+=length
    numbl=len(blocks)-1
    freebl=0
    while numbl>=0:
        pos,sz=blocks[numbl]
        if sz>0:
            nb=1
            if ispart2:
                nb=sz
                freebl=0
                while voids[freebl][1]<sz: freebl+=1
            else:
                while voids[freebl][1]==0: freebl+=1
            blocks[numbl][1]=sz-nb
            if freebl<numbl:
                res+=arith(voids[freebl][0],nb)*numbl
                voids[freebl][0]+=nb
                voids[freebl][1]-=nb
            else:
                res+=arith(pos+sz-nb,nb)*numbl
        else:
            numbl-=1
    return res

part1,part2=solve(inp,False),solve(inp,True)
print(part1,part2)