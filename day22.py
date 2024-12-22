from time import perf_counter
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

def nest(f,x,n):
    seen=set()
    k=0
    while k<n:
        x=f(x)
        if x not in seen:
            seen.add(x)
            k+=1
    return x

def nestList(f,x,n):
    L=[(x,None)]
    seen=set()
    k=0
    while k<n:
        y=f(x)
        if y not in seen:
            seen.add(y)
            L.append((y,y%10-x%10))
            x=y
            k+=1
    return L

def all4tuples(lst):
    A=set()
    n=len(lst)
    for i in range(1,n-3):
        u=(lst[i][1],lst[i+1][1],lst[i+2][1],lst[i+3][1])
        if u not in A: A.add(u)
    return A

def buy(dic,towatch):
    if towatch in dic:return dic[towatch]
    return 0

def getPrices(lst):
    d={}
    n=len(lst)
    for i in range(1,n-3):
        u=(lst[i][1],lst[i+1][1],lst[i+2][1],lst[i+3][1])
        if u not in d: d[u]=lst[i+3][0]%10
    return d    

allPrices=[getPrices(nestList(derive,x,2000)) for x in L]
tuples=set()
for x in L:
    tuples|=all4tuples(nestList(derive,x,2000))


def F(towatch):
    return sum([buy(dic,towatch) for dic in allPrices])

part1=sum([nest(derive,x,2000) for x in L])
part2=max(F(towatch) for towatch in tuples)
toc=perf_counter()
print(part1,part2,toc-tic)