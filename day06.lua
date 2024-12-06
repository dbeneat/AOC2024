local part1,part2=0,0
W,H,startx,starty=0,0,0,0
grid={}
for line in io.lines("data/input06.txt") do
    H=H+1
    table.insert(grid,{})
    for i=1,#line do
        local ch = string.sub(line,i,i)
        table.insert(grid[H],ch)
        if ch=="^" then startx,starty=i,H end
    end
end
W=H
function walk()
    local x,y=startx,starty
    local h,dx,dy=0,0,-1
    seenpos={[200*y+x]=1}
    seenstates={[4*(200*y+x)+h]=1}
    while true do
        local nx,ny=x+dx,y+dy
        if nx<1 or nx>W or ny<1 or ny>H then return false end
        if grid[ny][nx]=="#" then
            dx,dy=-dy,dx
            h=(h+1)%4
        else
            x,y=nx,ny
            seenpos[200*y+x]=1
            if seenstates[4*(200*y+x)+h] then
                return true
            else
                seenstates[4*(200*y+x)+h]=1
            end
        end
    end
end

walk()
for _,k in pairs(seenpos) do
    part1=part1+1
    grid[_//200][_%200]="#"
    if walk(false) then part2=part2+1 end
    grid[_//200][_%200]="."
end
print(part1,part2)