from time import perf_counter
from collections import Counter
tic=perf_counter()
with open("data/input22.txt") as f:
    L=[int(x) for x in f.read().split()]

def derive(secret):
    secret=secret^(64*secret)
    secret=secret%16777216
    secret=secret^(secret//32)
    secret=secret%16777216
    secret=secret^(2048*secret)
    secret=secret%16777216
    return secret

prices=Counter()
part1=0
for m in L:
    seen=set()
    k=5
    a=m
    b=derive(a)
    c=derive(b)
    d=derive(c)
    e=derive(d)
    while k<=2000:
        d1,d2,d3,d4=b%10-a%10,c%10-b%10,d%10-c%10,e%10-d%10
        if (d1,d2,d3,d4) not in seen:
            prices[(d1,d2,d3,d4)]+=e%10
            seen.add((d1,d2,d3,d4))
        a,b,c,d=b,c,d,e
        e=derive(d)
        k+=1
    part1+=e

part2=max(prices.values())
toc=perf_counter()
print(part1,part2,toc-tic)