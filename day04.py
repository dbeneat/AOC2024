part1,part2=0,0
with open("data/input04.txt") as f:
    L=[list(x) for x in f.read().strip().split("\n")]
r,c=len(L),len(L[0])
H=("".join(L[i][j+k] for k in range(4)) for i in range(r) for j in range(c-3))
V=("".join(L[i+k][j] for k in range(4)) for i in range(r-3) for j in range(c))
D1=("".join(L[i+k][j+k] for k in range(4)) for i in range(r-3) for j in range(c-3))
D2=("".join(L[i+k][j+3-k] for k in range(4)) for i in range(r-3) for j in range(c-3))
part1+=sum(w=="XMAS" or w=="SAMX" for w in H)
part1+=sum(w=="XMAS" or w=="SAMX" for w in V)
part1+=sum(w=="XMAS" or w=="SAMX" for w in D1)
part1+=sum(w=="XMAS" or w=="SAMX" for w in D2)
for i in range(r-2):
    for j in range(c-2):
        w1="".join([L[i+k][j+k] for k in range(3)])
        w2="".join([L[i+k][j+2-k] for k in range(3)])
        if (w1=="MAS"or w1=="SAM") and (w2=="MAS" or w2=="SAM"): part2+=1
print(part1,part2)