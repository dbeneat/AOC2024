io.input("data/input17.txt")
local inp=io.read("*all")
local A,B,C,pr=string.match(inp,"Register A: (%d+)\nRegister B: (%d+)\nRegister C: (%d+)\n\nProgram: (.+)")
A,B,C=tonumber(A),tonumber(B),tonumber(C)
local prog={}
for a in string.gmatch(pr,"(%d+)") do
    table.insert(prog,tonumber(a))
end

function execute(A,B,C)
    local ip,output=0,0
    while ip<#prog do
        local op1,op2=prog[ip+1],prog[ip+2] --because of 1-based indexing
        local comb
        if op2<=3 then comb=op2
        elseif op2==4 then comb=A
        elseif op2==5 then comb=B
        elseif op2==6 then comb=C end
        if op1==0 then A=A//(1<<comb) end
        if op1==1 then B=op2~B end
        if op1==2 then B=comb%8 end
        if op1==3 and A~=0 then ip=op2-2 end
        if op1==4 then B=B~C end
        if op1==5 then output=output*10+comb%8 end
        if op1==6 then B=A//(1<<comb) end
        if op1==7 then C=A//(1<<comb) end
        ip=ip+2
    end
    return output
end

local part1=execute(A,B,C)

function searchDigit(pos,start,step)
    if pos<0 then return start end
    for i=0,7 do
        local A,B,C=start+i*step,0,0
        local output=execute(A,B,C)
        local digit=tonumber(string.sub(tostring(output),pos+1,pos+1))
        if digit==prog[pos+1] then
            local s=searchDigit(pos-1,start+i*step,step//8)
            if s then return s end
        end
    end
end
local start=1<<3*(#prog-1)
local blocksize=start
local part2=searchDigit(#prog-1,start,blocksize)
print(part1,part2)