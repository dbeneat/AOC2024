part1,part2=0,0
ant,antinodes1,antinodes2={},{},{}
H=0
for x in io.lines("data/input08.txt") do
    W=#x
    for i=1,#x do
        local ch=string.sub(x,i,i)
        if ch~="." then
            if ant[ch] then
                table.insert(ant[ch],{i-1,H})
            else
                ant[ch]={{i-1,H}}
            end
        end
    end
    H=H+1
end

function inside(x,y) return x>=0 and x<W and y>=0 and y<H end
for _,L in pairs(ant) do
    for i1,c1 in ipairs(L) do
        for i2,c2 in ipairs(L) do
            if i1~=i2 then
                local x1,y1,x2,y2=c1[1],c1[2],c2[1],c2[2]
                local dx,dy=x2-x1,y2-y1
                local k=0
                while (inside(x2+k*dx,y2+k*dy)) do
                    local a=200*(y2+k*dy)+x2+k*dx
                    if k==1 and not antinodes1[a] then antinodes1[a]=true; part1=part1+1 end
                    if not antinodes2[a] then antinodes2[a]=true; part2=part2+1 end
                    k=k+1
                end
            end
        end
    end
end
print(part1,part2)