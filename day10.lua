local part1,part2=0,0
grid={}
for x in io.lines("data/input10.txt") do
    if #x>0 then
        local row={}
        for i=1,#x do
            table.insert(row,tonumber(string.sub(x,i,i)))
        end
        table.insert(grid,row)
    end
end
W,H=#grid,#grid[1]

function inside(x,y) return x>=1 and x<=W and y>=1 and y<=H end

function grade(x,y,ispart1)
    if ispart1 then
        if seen[300*y+x] then return 0 end
        seen[300*y+x]=1
    end
    if grid[y][x]==9 then return 1 end
    local score=0
    if inside(x-1,y) and grid[y][x-1]==grid[y][x]+1 then score=score+grade(x-1,y,ispart1) end
    if inside(x+1,y) and grid[y][x+1]==grid[y][x]+1 then score=score+grade(x+1,y,ispart1) end
    if inside(x,y-1) and grid[y-1][x]==grid[y][x]+1 then score=score+grade(x,y-1,ispart1) end
    if inside(x,y+1) and grid[y+1][x]==grid[y][x]+1 then score=score+grade(x,y+1,ispart1) end
    return score
end

for y=1,H do
    for x=1,W do
        if grid[y][x]==0 then
            seen={};part1=part1+grade(x,y,true)
            part2=part2+grade(x,y,false)
        end
    end
end
print(part1,part2)