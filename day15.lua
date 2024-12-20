local part1,part2=0,0
local walls,boxes,walls2,boxes2={},{},{},{}
local prog=""

function hash(x,y) return 100*y+x end
local px,py,W,H=0,0,0,0
for line in io.lines("data/input15.txt") do
    if string.sub(line,1,1)=="#" then
        W=#line
        H=H+1
        for i=1,#line do
            local ch=string.sub(line,i,i)
            if ch=="#" then
                walls[hash(i-1,H-1)]=1
                walls2[hash(2*(i-1),H-1)]=1
                walls2[hash(2*(i-1)+1,H-1)]=1
            end
            if ch=="O" then
                boxes[hash(i-1,H-1)]=1
                boxes2[hash(2*(i-1),H-1)]=1
            end
            if ch=="@" then px,py=i-1,H-1;ppx,ppy=2*(i-1),H-1 end
        end
    else
        prog=prog..line
    end
end

function go(dx,dy)
    local nx,ny=px+dx,py+dy
    local h=hash(nx,ny)
    if walls[h] then return end
    if not boxes[h] then px,py=nx,ny; return end
    local a,b=nx,ny
    while boxes[hash(a,b)] do a,b=a+dx,b+dy end
    if walls[hash(a,b)] then return end
    boxes[h]=nil
    boxes[hash(a,b)]=1
    px,py=nx,ny
end

function canpush(x,y,dx,dy,L)
    local nx,ny=x+dx,y+dy
    local h=hash(nx,ny)
    if walls[h] then return false end
    if boxes[h] and not L[h] then
        L[h]=1
        return canpush(nx,ny,dx,dy,L) and canpush(nx+1,ny,dx,dy,L)
    end
    local hh=hash(nx-1,ny)
    if boxes[hh] and not L[hh] then
        L[hh]=1
        return canpush(nx,ny,dx,dy,L) and canpush(nx-1,ny,dx,dy,L)
    end
    return true
end

function trypush(x,y,dx,dy)
    local L={}
    if canpush(x,y,dx,dy,L) then
        for h,_ in pairs(L) do boxes[h]=nil end
        for h,_ in pairs(L) do
            local xx,yy=h%100,h//100
            boxes[hash(xx+dx,yy+dy)]=1 
        end
        return true
    end
    return false
end

for i=1,#prog do
    local c=string.sub(prog,i,i)
    if c=="<" then go(-1,0) end
    if c==">" then go(1,0) end
    if c=="^" then go(0,-1) end
    if c=="v" then go(0,1) end
end

for h,_ in pairs(boxes) do
    part1=part1+h
end

walls,boxes=walls2,boxes2
px,py=ppx,ppy

for i=1,#prog do
    local c=string.sub(prog,i,i)
    if c=="<" and trypush(px,py,-1,0) then px=px-1 end
    if c==">" and trypush(px,py,1,0) then px=px+1 end
    if c=="^" and trypush(px,py,0,-1) then py=py-1 end
    if c=="v" and trypush(px,py,0,1) then py=py+1 end
end
for h,_ in pairs(boxes) do
    part2=part2+h
end
print(part1,part2)