local part1,part2=0,0
local W,H=101,103
local Robots={}
io.input("data/input14.txt")
local inp=io.read("*all")
for x,y,vx,vy in string.gmatch(inp,"p=(%d+),(%d+) v=(%-?%d+),(%-?%d+)") do
    table.insert(Robots,{tonumber(x),tonumber(y),tonumber(vx),tonumber(vy)})
end

function update(r)
    local x,y,vx,vy=r[1],r[2],r[3],r[4]
    r[1]=(x+vx)%W
    r[2]=(y+vy)%H
end
local Hresidue,Vresidue=0,0
for i=0,99 do
    local LH,LV={},{}
    local Hok,Vok=false,false
    for _,r in ipairs(Robots) do
        if LH[r[1]] and LH[r[1]]>20 then
            Hok=true
        else
            LH[r[1]]= LH[r[1]] and LH[r[1]]+1 or 1
        end
        if LV[r[2]] and LV[r[2]]>20 then
            Vok=true
        else
            LV[r[2]]= LV[r[2]] and LV[r[2]]+1 or 1
        end
        update(r)
        if Hok then Hresidue=i end
        if Vok then Vresidue=i end
    end
end

local a,b,c,d=0,0,0,0
for _,r in ipairs(Robots) do
    if r[1]<(W-1)/2 and r[2]<(H-1)/2 then a=a+1 end
    if r[1]<(W-1)/2 and r[2]>(H-1)/2 then b=b+1 end
    if r[1]>(W-1)/2 and r[2]<(H-1)/2 then c=c+1 end
    if r[1]>(W-1)/2 and r[2]>(H-1)/2 then d=d+1 end
end
part1=a*b*c*d
for k=1,W*H do
    if k%W==Hresidue and k%H==Vresidue then
        part2=k;break
    end
end
print(part1,part2)