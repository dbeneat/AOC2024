local part1,part2=0,0
local G={}
local H,W=0,0
for x in io.lines("data/input12.txt") do
    if #x>0 then
        table.insert(G,x);H=H+1
    end
end
W=#G[1]
local numcc=0
local CC={}
function dfs(x,y)
    local code=W*y+x
    if CC[code] then return end
    CC[code]=numcc
    local h=string.sub(G[y],x,x)
    if x>1 and h==string.sub(G[y],x-1,x-1) then dfs(x-1,y) end
    if x<W and h==string.sub(G[y],x+1,x+1) then dfs(x+1,y) end
    if y>1 and h==string.sub(G[y-1],x,x) then dfs(x,y-1) end
    if y<H and h==string.sub(G[y+1],x,x) then dfs(x,y+1) end
end
for y=1,H do
    for x=1,W do
        if not CC[y*W+x] then dfs(x,y); numcc=numcc+1; end
    end
end

function get(x,y) local code=y*W+x; return CC[code] end
local area,perim,corners={},{},{}
for y=1,H do
    for x=1,W do
        for _,dx in ipairs({-1,1}) do
            for _,dy in ipairs({-1,1}) do
                local a,b,c,d=get(x,y),get(x+dx,y),get(x,y+dy),get(x+dx,y+dy)
                if (a~=b and a~=c) or (a==b and a==c and a~=d)then
                    corners[a]=corners[a] and corners[a]+1 or 1
                end
            end
        end
        local a,b,c=get(x,y),get(x-1,y),get(x,y-1)
        local k=4
        if a==b then k=k-2 end
        if a==c then k=k-2 end
        area[a]=area[a] and area[a]+1 or 1
        perim[a]=perim[a] and perim[a]+k or k
    end
end

for k,v in pairs(area) do
    part1=part1+area[k]*perim[k]
    part2=part2+area[k]*corners[k]
end
print(part1,part2)