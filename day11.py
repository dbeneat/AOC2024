from collections import Counter
with open("data/input11.txt") as f:
    inp=f.read()
c=Counter()
for x in inp.split(): c[int(x)]+=1

parts=[]
for k in range(75):
    newc=Counter()
    for x,count in c.items():
        if x==0: newc[1]+=count; continue
        n=len(str(x))
        if n%2==1: newc[2024*x]+=count
        else: newc[x//(10**(n//2))]+=count; newc[x%(10**(n//2))]+=count
    c=newc
    if k==24 or k==74: parts.append(sum(c[x] for x in c))
        
print(parts[0],parts[1])