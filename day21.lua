nk={['7']={0,0},['8']={1,0},['9']={2,0},['4']={0,1},['5']={1,1},['6']={2,1},['1']={0,2},['2']={1,2},['3']={2,2},['0']={1,3},['A']={2,3},['X']={0,3}}
dk={['^']={1,0},['A']={2,0},['<']={0,1},['v']={1,1},['>']={2,1},['X']={0,0}}

function allPaths(A,B,pad)
    local M={}
    local x2,y2=B[1],B[2]
    function dfs(x1,y1,cur)
        if x1==x2 and y1==y2 then
            --print(cur)
            table.insert(M,cur.."A")
            return
        end
        local forb=pad["X"]
        if x2>x1 and (forb[1]~=x1+1 or forb[2]~=y1) then
            dfs(x1+1,y1,cur..">")
        end
        if x2<x1 and (forb[1]~=x1-1 or forb[2]~=y1) then
            dfs(x1-1,y1,cur.."<")
        end
        if y2>y1 and (forb[1]~=x1 or forb[2]~=y1+1) then
            dfs(x1,y1+1,cur.."v")
        end
        if y2<y1 and (forb[1]~=x1 or forb[2]~=y1-1) then
            dfs(x1,y1-1,cur.."^")
        end
    end
    dfs(A[1],A[2],"",pad)
    return M
end

memo={}
function nbKeypresses(code,depth)
    if depth==0 then return #code end
    local h=code.."|"..depth
    if memo[h] then return memo[h] end
    code="A"..code
    local s=0
    for i=1,#code-1 do
        local minimum=1/0
        local a,b=string.sub(code,i,i),string.sub(code,i+1,i+1)
        for _,path in ipairs(allPaths(dk[a],dk[b],dk)) do
            minimum=math.min(minimum,nbKeypresses(path,depth-1))
        end
        s=s+minimum
    end
    memo[h]=s
    return s
end

function solve(code,depth)
    local s=0
    code="A"..code
    local s=0
    for i=1,#code-1 do
        local minimum=1/0
        local a,b=string.sub(code,i,i),string.sub(code,i+1,i+1)
        for _,path in ipairs(allPaths(nk[a],nk[b],nk)) do
            minimum=math.min(minimum,nbKeypresses(path,depth))
        end
        s=s+minimum
    end
    return s    
end

function complexity(string,depth)
    return tonumber(string.sub(string,1,-2))*solve(string,depth)
end

local part1,part2=0,0
for line in io.lines("data/input21.txt") do
    if #line>0 then
        part1=part1+complexity(line,2)
        part2=part2+complexity(line,25)
    end
    
end

print(part1,part2)