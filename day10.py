with open("data/input10.txt") as f:
    L=[[int(a) for a in list(x)] for x in f.read().strip().split("\n")]
H,W=len(L),len(L[0])

def grade(x,y,seen,memo):
    seen.add((x,y))
    if L[y][x]==9: memo[(x,y)]=1; return 1,1
    score,rating=0,0
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if x+dx<0 or x+dx>=W or y+dy<0 or y+dy>=H: continue
        if L[y+dy][x+dx]==L[y][x]+1:
            notseen=(x+dx,y+dy) not in seen
            sc,r=grade(x+dx,y+dy,seen,memo)
            rating+=r
            if notseen: score+=sc
    if (x,y) in memo:
        return score,memo[(x,y)]
    else:
        memo[(x,y)]=rating
        return score,rating  

part1,part2=0,0
for y in range(H):
    for x in range(W):
        if L[y][x]==0:
            score,rating=grade(x,y,set(),{})
            part1+=score
            part2+=rating
print(part1,part2)