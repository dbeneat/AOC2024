with open("data/input25.txt") as f:
    L=[x.split() for x in f.read().strip().split("\n\n")]

def code(x):
    C=[0]*5
    for w in x:
        for i,c in enumerate(w):
            C[i]+=(w[i]=="#")
    return C

keys,locks=[],[]
for x in L:
    if x[0].startswith("#"):keys.append(code(x))
    else:locks.append(code(x))

part1=0
for kc in keys:
    for lc in locks:
        if all(x+y<=7 for x,y in zip(kc,lc)):part1+=1
print(part1)