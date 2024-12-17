with open("data/input17.txt") as f:
    reg,prog=f.read().strip().split("\n\n")
reg=reg.split()
reg=[int(reg[2]),int(reg[5]),int(reg[8])]
prog=[int(k) for k in prog[9:].split(",")]

def combo(n,reg):
    if 0<=n<=3:
        return n
    if 4<=n<=6:
        return reg[n-4]
    if n==7:
        print("erreur")

def execute(prog,reg):
    output=[]
    ip=0
    while ip<len(prog):
        #print("...reg", reg)
        op1,op2=prog[ip],prog[ip+1]
        comb=combo(op2,reg)
        if op1==0:
            num,denom=reg[0],2**comb
            reg[0]=num//denom
            ip+=2
        if op1==1:
            reg[1]=op2^reg[1]
            ip+=2
        if op1==2:
            reg[1]=comb%8
            ip+=2
        if op1==3:
            if reg[0]!=0:
                ip=op2
            else:
                ip+=2
        if op1==4:
            reg[1]=reg[1]^reg[2]
            ip+=2
        if op1==5:
            output.append(comb%8)
            ip+=2
        if op1==6:
            num,denom=reg[0],2**comb
            reg[1]=num//denom
            ip+=2
        if op1==7:
            num,denom=reg[0],2**comb
            reg[2]=num//denom
            ip+=2
    return output

part1=execute(prog,reg)

def searchDigit(digitpos,start, stepsize):
    if digitpos<0:
        return start
    for i in range(8):
        reg[0]=start+i*stepsize
        reg[1]=0
        reg[2]=0
        output=execute(prog,reg)
        if output[digitpos]==prog[digitpos]:
            s=searchDigit(digitpos-1,start+i*stepsize,stepsize//8)
            if s: return s
 
start=8**(len(prog)-1)
blocksize=8**(len(prog)-1)
part2=searchDigit(len(prog)-1,start,blocksize)

print(part1,part2)