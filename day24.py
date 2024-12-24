from time import perf_counter
tic=perf_counter()

with open("data/input24.txt") as f:
    A,B=f.read().strip().split("\n\n")
start={}
for u in A.split("\n"):
    a,b=u.split(":")
    start[a]=int(b)
gates={}
for u in B.split("\n"):
    M=u.split()
    gates[M[4]]=[M[1],M[0],M[2]]

def interpret(letter,wires):
    output=[]
    for w in wires:
        if w[0]==letter:
            output.append((w,wires[w]))
    rep="".join(str(x[1]) for x in reversed(sorted(output)))
    return int(rep,2)

def compute():
    wires=start.copy()
    Q=[]
    for g in gates:
        Q.append(g)
    iter=5000
    while Q:
        g=Q.pop()
        h=gates[g]
        if h[1] in wires and h[2] in wires:
            if h[0]=="AND": wires[g]=wires[h[1]]&wires[h[2]]
            if h[0]=="OR": wires[g]=wires[h[1]]|wires[h[2]]
            if h[0]=="XOR":  wires[g]=wires[h[1]]^wires[h[2]]
        else:
            Q=[g]+Q
        iter-=1
        if iter==0: return None
    return wires

def fitness():
    bitpattern=0
    a=21541211    
    for _ in range(30):
        for x in start:
            a=(a*16807)%(2**31-1)
            start[x]=a%2
        x,y=interpret("x",start),interpret("y",start)
        z=x+y
        zobs=interpret("z",compute())
        bitpattern|=(z^zobs)
    return bin(bitpattern).count("1")
            
            
def searchSwap(excl):
    iter=0
    swa,swb=None,None
    fit=fitness()
    G=list(gates)
    for i in range(len(G)):
        a=G[i]
        if a in excl: continue
        if i%50==0:print(i)
        for j in range(i+1,len(G)):
            b=G[j]
            if b in excl: continue
            gates[a],gates[b]=gates[b],gates[a]
            comp=compute()
            if comp:
                newfit=fitness()
                if newfit<fit:
                    swa,swb=a,b
                    fit=newfit
            gates[a],gates[b]=gates[b],gates[a]
            iter+=1
    excl.add(swa)
    excl.add(swb)
    gates[swa],gates[swb]=gates[swb],gates[swa]
    print(fit,swa,swb)
    return swa,swb


x,y=interpret("x",start),interpret("y",start)
z=x+y
calcz=interpret("z",compute())
part1=interpret("z",compute())
excl=set()
searchSwap(excl)
searchSwap(excl)
searchSwap(excl)
searchSwap(excl)

part2=",".join(sorted(excl))
toc=perf_counter()
print(part1,part2,toc-tic)