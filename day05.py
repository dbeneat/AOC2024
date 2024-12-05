from collections import defaultdict
with open("data/input05.txt") as f:
    L,R = f.read().strip().split("\n\n")
L = [[int(y) for y in x.split("|")] for x in L.split("\n")]
R = [[int(x) for x in x.split(",")] for x in R.split("\n")]
rules = defaultdict(list)
for a,b in L:
    rules[a].append(b)

def bsort(L):
    wasordered=True
    ok=False
    while not ok:
        ok=True
        for i in range(len(L)-1):
            x,y=L[i],L[i+1]
            if x in rules[y]:
                ok=False
                wasordered=False
                L[i],L[i+1]=y,x
    return wasordered,L

part1,part2=0,0
for row in R:
    s=len(row)
    wasordered,row=bsort(row)
    if wasordered:
        part1+=row[s//2]
    else:
        part2+=row[s//2]
print(part1,part2)