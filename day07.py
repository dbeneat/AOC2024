def toint(string):
    if len(string)==0:
        return 0
    return int(string)

def correct(res,L,ispart2):
    if len(L)==1: return L[0]==res
    k,r=len(str(L[-1])),str(res)
    return (ispart2 and int(r[-k:])==L[-1] and correct(toint(r[:-k]),L[:-1],ispart2))\
            or(res%L[-1]==0 and correct(res//L[-1],L[:-1],ispart2))\
            or(res>=L[-1] and correct(res-L[-1],L[:-1],ispart2))

part1,part2=0,0
with open("data/input07.txt") as f:
    for line in (x for x in f if x.strip()):
        L,R=line.split(":")
        L,R=int(L),[int(x) for x in R.split()]
        if correct(L,R,False): part1+=L
        if correct(L,R,True): part2+=L
    print(part1,part2)