import re
with open("data/input13.txt") as f: L=[int(x) for x in re.findall("\d+",f.read())]
machines=[]
for i in range(0,len(L),6):
    machines.append({'A':(L[i],L[i+1]),'B':(L[i+2],L[i+3]),'prize':(L[i+4],L[i+5])})

def det(u,v): return u[0]*v[1]-u[1]*v[0]
def coords(v,u1,u2):
    D,N1,N2=det(u1,u2),det(v,u2),det(u1,v)
    if N1%D==0 and N2%D==0: return (N1//D, N2//D)
    return None
def cost(v):
    if v:return 3*v[0]+v[1]
    return 0
def tr(v): return (v[0]+10**13,v[1]+10**13)

part1=sum(cost(coords(m['prize'],m['A'],m['B'])) for m in machines)
part2=sum(cost(coords(tr(m['prize']),m['A'],m['B'])) for m in machines)
print(part1,part2)