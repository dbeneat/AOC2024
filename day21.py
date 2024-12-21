with open("data/input21.txt") as f:
    L=f.read().split()
nk={'7':(0,0),'8':(1,0),'9':(2,0),'4':(0,1),'5':(1,1),'6':(2,1),'1':(0,2),'2':(1,2),'3':(2,2),'0':(1,3),'A':(2,3),'X':(0,3)}
dk={'^':(1,0),'A':(2,0),'<':(0,1),'v':(1,1),'>':(2,1),'X':(0,0)}

def allPaths(A,B,pad):
    M=[]
    def F(A,B,L,pad):
        if A==B:
            M.extend(L)
            return M
        x1,y1=A
        x2,y2=B
        if x2>x1 and pad["X"]!=(x1+1,y1):
            F((x1+1,y1),B,[x+">" for x in L],pad)
        if x2<x1 and pad["X"]!=(x1-1,y1):
            F((x1-1,y1),B,[x+"<" for x in L],pad)
        if y2>y1 and pad["X"]!=(x1,y1+1):
            F((x1,y1+1),B,[x+"v" for x in L],pad)
        if y2<y1 and pad["X"]!=(x1,y1-1):
            F((x1,y1-1),B,[x+"^" for x in L],pad)
        return M
    return [x+"A" for x in F(A,B,[""],pad)]

memo={}
def nbKeypresses(code,depth):
    if depth==0: return len(code)
    h=(code,depth)
    if h in memo:
        return memo[h]
    s=0
    code="A"+code
    for i in range(len(code)-1):
        s+=min(nbKeypresses(path,depth-1) for path in allPaths(dk[code[i]],dk[code[i+1]],dk))
    memo[h]=s
    return s

def solve(code,depth):
    s=0
    code="A"+code
    for i in range(len(code)-1):
        s+=min(nbKeypresses(path,depth) for path in allPaths(nk[code[i]],nk[code[i+1]],nk))
    return s

def complexity(string,depth):
    return int(string[:-1])*solve(string,depth)

part1=sum(complexity(x,2) for x in L)
part2=sum(complexity(x,25) for x in L)
print(part1,part2)