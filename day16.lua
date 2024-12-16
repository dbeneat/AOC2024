local part1,part2=0,0
local G={}
local sx,sy,W,H=0,0,0,0
for line in io.lines("data/input16.txt") do
    if #line>0 then
        H=H+1
        local row={}
        for i=1,#line do
            local ch=string.sub(line,i,i)
            table.insert(row,ch)
            if ch=="S" then sx,sy=i,H end
        end
        table.insert(G,row)
    end
end
W=#G[1]

function hash(x,y,h)
    return 4*(W*(y-1)+x-1)+h
end

local Q={{0,sx,sy,0}}
local seen={}
local dist={}
for y=1,H do
    for x=1,W do
        for h=0,3 do
            dist[hash(x,y,h)]=999999
        end
    end
end

local headings={{0,1,0},{1,0,1},{2,-1,0},{3,0,-1}}
local pred={}
while #Q>0 do
    local best,ibest=999999,1
    for i=1,#Q do
        local u=Q[i]
        if u[1]<best then best=u[1];ibest=i end
    end
    local u=table.remove(Q,ibest)
    local d,x,y,h=u[1],u[2],u[3],u[4]
    if G[y][x]=='E' then part1=dist[hash(x,y,h)];endstate=hash(x,y,h);break end
    if not seen[hash(x,y,h)] then
        seen[hash(x,y,h)]=true
        for _,H in ipairs(headings) do
            local hh,dx,dy=H[1],H[2],H[3]
            if G[y+dy][x+dx]~='#' and not seen[hash(x+dx,y+dy,hh)] then
                local deltaD = h==hh and 1 or 1001
                local newD=d+deltaD
                if dist[hash(x+dx,y+dy,hh)]>=newD then
                    dist[hash(x+dx,y+dy,hh)]=newD
                    table.insert(Q,{newD,x+dx,y+dy,hh})
                    local h1,h2=hash(x+dx,y+dy,hh),hash(x,y,h)
                    if pred[h1] then table.insert(pred[h1],h2) else pred[h1]={h2} end
                end
            end
        end
    end
end

tiles={}
function count(h)
    tiles[h//4]=true
    if not pred[h] then return end
    for _,hh in ipairs(pred[h]) do count(hh) end
end
for i=0,3 do
    count(4*(endstate//4)+i)
end
for _ in pairs(tiles) do part2=part2+1 end
print(part1,part2)