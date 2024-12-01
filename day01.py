with open("data/input01.txt") as f:
    inp=f.read()
L=[[int(a) for a in x.split()] for x in inp.strip().split("\n")]
A=[int(x[0]) for x in L]
B=[int(x[1]) for x in L]
part1=sum(abs(x-y) for x,y in zip(sorted(A),sorted(B)))
part2=sum(x*sum(x==y for y in B) for x in A)
print(part1,part2)