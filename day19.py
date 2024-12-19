with open("data/input19.txt") as f:
    A,B=f.read().strip().split("\n\n")
A,B=[x.strip() for x in A.split(",")],B.split()

mem={}
def nbsolutions(pattern):
    if pattern=="":
        return 1
    if pattern in mem: return mem[pattern]
    n=0
    for w in A:
        k=len(w)
        if pattern[:k]==w: n+=nbsolutions(pattern[k:])
    mem[pattern]=n
    return n

S=[nbsolutions(x) for x in B]
part1=sum(x!=0 for x in S)
part2=sum(S)
print(part1,part2)