with open("data/input02.txt") as f:
    L=[[int(a) for a in x.split()] for x in f.readlines()]
def ok(x,skip):
    xx=[x for i,x in enumerate(x) if i!=skip]
    d=[b-a for a,b in zip(xx[:-1],xx[1:])]
    return all(1<=k<=3 for k in d) or all(-3<=k<=-1 for k in d)
part1=sum(ok(x,None) for x in L)
part2=sum(any(ok(x,skip) for skip in range(len(x))) for x in L)
print(part1,part2)