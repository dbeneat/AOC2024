from collections import defaultdict
with open("data/input08.txt") as f:
    L=f.read().split()
H,W=len(L),len(L[0])

ant=defaultdict(list)
for y in range(H):
    for x in range(W):
        if L[y][x]!=".":
            ant[L[y][x]].append((x,y))
antinodes={}
for c in ant:
    for (x,y) in ant[c]:
        for (xx,yy) in ant[c]:
            if (x,y)==(xx,yy):
                continue
            dx,dy=xx-x,yy-y
            k=0
            while (0<=xx+k*dx<W) and (0<=yy+k*dy<H):
                a=(xx+k*dx,yy+k*dy)
                if k==1:
                    antinodes[a]=True
                elif a not in antinodes:
                    antinodes[a]=False
                k+=1
part1,part2=len([x for x in antinodes if antinodes[x]]),len(antinodes)
print(part1,part2)