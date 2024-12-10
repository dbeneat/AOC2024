with open("data/input10.txt") as f:
    L=[[int(a) for a in list(x)] for x in f.read().strip().split("\n")]
H,W=len(L),len(L[0])

def score(x,y,seen):
    if seen!=None:
        if (x,y) in seen: return 0
        seen.add((x,y))
    if L[y][x]==9: return 1
    total=0
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if x+dx<0 or x+dx>=W or y+dy<0 or y+dy>=H: continue
        if L[y+dy][x+dx]==L[y][x]+1: total+=score(x+dx,y+dy,seen)
    return total  

part1,part2=0,0
for y in range(H):
    for x in range(W):
        if L[y][x]==0:
            part1+=score(x,y,set()); part2+=score(x,y,None)
print(part1,part2)