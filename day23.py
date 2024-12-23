from collections import defaultdict
import networkx as nx
with open("data/input23.txt") as f:
    L=[x.split("-") for x in f.read().split()]

adj=defaultdict(list)
computers=set()
for a,b in L:
    adj[a].append(b)
    adj[b].append(a)
    computers.add(a)
    computers.add(b)
    
computers=list(computers)
part1=0
for i in range(len(computers)):
    a=computers[i]
    for j in range(i+1,len(computers)):
        b=computers[j]
        if b not in adj[a]:continue
        for k in range(j+1,len(computers)):
            c=computers[k]
            if c not in adj[a] or c not in adj[b]:continue
            if a[0]=="t" or b[0]=="t" or c[0]=="t":part1+=1
G = nx.Graph()
for a,b in L:
    G.add_edge(a,b)
clique=max(nx.find_cliques(G), key=len)
part2=",".join(sorted(clique))

print(part1,part2)