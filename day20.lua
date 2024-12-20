local part1,part2=0,0
local G={}
local sx,sy,W,H=0,0,0,0
for line in io.lines("data/input20.txt") do
    if #line>0 then
        H=H+1
        local row={}
        for i=1,#line do
            local ch=string.sub(line,i,i)
            table.insert(row,ch)
            if ch=="S" then sx,sy=i,H end
            if ch=="E" then ex,ey=i,H end
        end
        table.insert(G,row)
    end
end
W=#G[1]

function hash(x,y) return 150*y+x end

function distMap(sx,sy,ex,ey)
    local dist={}
    local x,y=sx,sy 
    local d=0  
    while true do
        dist[hash(x,y)]=d
        if x==ex and y==ey then return dist end
        d=d+1
        if x>1 and G[y][x-1]~="#" and not dist[hash(x-1,y)] then x=x-1
        elseif x<W and G[y][x+1]~="#" and not dist[hash(x+1,y)] then x=x+1
        elseif y>1 and G[y-1][x]~="#" and not dist[hash(x,y-1)] then y=y-1
        elseif y<H and G[y+1][x]~="#" and not dist[hash(x,y+1)] then y=y+1; end 
    end
end

local dist1=distMap(sx,sy,ex,ey)
local dist2=distMap(ex,ey,sx,sy)
local D=dist1[hash(ex,ey)]
for y=2,H-1 do
    for x=2,W-1 do
        if G[y][x]=="#" then goto skip_outer end
            local d1=dist1[hash(x,y)]
            for yy=math.max(2,y-20),math.min(H-1,y+20) do
                for xx=math.max(2,x-20),math.min(W-1,x+20) do             
                    if G[yy][xx]=="#" then goto skip_inner end
                        local d2=dist2[hash(xx,yy)]
                        local d3=math.abs(x-xx)+math.abs(y-yy)
                        if d3<=20 then
                            local d=d1+d2+d3
                            if d3==2 and d<=D-100 then part1=part1+1 end
                            if d<=D-100 then part2=part2+1 end
                        end
                    ::skip_inner::
                end
            end
        ::skip_outer::
    end
end
print(part1,part2)