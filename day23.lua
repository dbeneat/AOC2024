local part1,part2=0,""
local adj={}
local computers={}
local seen={}
for line in io.lines("data/input23.txt") do
    if #line>0 then
        local a,b=string.sub(line,1,2),string.sub(line,4,5)
        if adj[a] then adj[a][b]=true else adj[a]={[b]=true} end
        if adj[b] then adj[b][a]=true else adj[b]={[a]=true} end
        if not seen[a] then seen[a]=true; table.insert(computers,a) end
        if not seen[b] then seen[b]=true; table.insert(computers,b) end
    end
end

for i=1,#computers do
    local a=computers[i]
    for j=i+1,#computers do
        local b=computers[j]
        if not adj[a][b] then goto skip_outer end
        for k=j+1,#computers do
            local c=computers[k]
            if not adj[a][c] or not adj[b][c] then goto skip_inner end
            if string.sub(a,1,1)=="t" or string.sub(b,1,1)=="t" or string.sub(c,1,1)=="t" then
                part1=part1+1 
            end
            ::skip_inner::
        end
    ::skip_outer::    
    end 
end

function empty(tab)
    local n=0
    for _,_ in pairs(tab) do
        n=n+1
        break
    end
    return n==0
end

function maximumClique(edges,adj)
    local maxCl
    local maxSz=0
    function BronKerbosch(R,rsize,P,X)
        if empty(P) and empty(X) then
            if rsize>maxSz then
                maxSz=rsize
                maxCl={}
                for x,_ in pairs(R) do table.insert(maxCl,x) end
            end
        end
        for v,_ in pairs(P) do
            local rs=rsize
            local R1={}
            for x,_ in pairs(R) do R1[x]=true end
            R1[v]=true
            rs=rs+1
            local P1={}
            for x,_ in pairs(P) do 
                if adj[v][x] then P1[x]=true end
            end
            local X1={}
            for x,_ in pairs(X) do 
                if adj[v][x] then X1[x]=true end 
            end        
            BronKerbosch(R1,rs,P1,X1)
            P[v]=nil
            X[v]=true
        end
    end
    local R={}
    local P={}
    for _,x in ipairs(computers) do P[x]=true end
    local X={}
    BronKerbosch(R,0,P,X)
    return maxCl
end

maxCl=maximumClique(computers,adj)
table.sort(maxCl)
for _,x in pairs(maxCl) do part2=part2..x.."," end
print(part1,string.sub(part2,1,-2))