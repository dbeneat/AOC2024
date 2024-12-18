io.input("data/input18.txt")
local inp=io.read("*all")
local obst={}
local Lobst={}
function hash(x,y) return 100*y+x end
local nobst=0
for x,y in string.gmatch(inp,"(%d+),(%d+)") do
    obst[hash(x,y)]=nobst; table.insert(Lobst,{x,y}); nobst=nobst+1
end

function solveFor(k)
    local W,H=71,71
    local sx,sy,ex,ey=0,0,W-1,H-1
    local Q,seen={{0,sx,sy}},{}
    while #Q>0 do
        local u=table.remove(Q,1)
        local d,x,y=u[1],u[2],u[3]
        if x==ex and y==ey then return d end
        if not seen[hash(x,y)] then
            seen[hash(x,y)]=true
            for _,a in ipairs({{x-1,y},{x+1,y},{x,y-1},{x,y+1}}) do         
                local xx,yy=a[1],a[2]
                local h=hash(xx,yy)
                if xx>=0 and xx<W and yy>=0 and yy<H
                and not(obst[h] and obst[h]<=k) and not seen[h] then
                    table.insert(Q,{d+1,xx,yy})
                end
            end
        end
    end
end

local part1=solveFor(1024)
local left,right=1024,nobst
while right-left>1 do
    local middle=(left+right)//2
    if solveFor(middle) then left=middle else right=middle end
end
local a=Lobst[right+1]
local part2=a[1]..","..a[2]
print(part1,part2)