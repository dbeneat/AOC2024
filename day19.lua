local part1,part2,i=0,0,0
local towels,mem={},{}

function nbsolutions(pattern)
    if #pattern==0 then return 1 end
    if mem[pattern] then return mem[pattern] end
    local n=0
    for _,x in ipairs(towels) do
        if string.sub(pattern,1,#x)==x then
            n=n+nbsolutions(string.sub(pattern,#x+1))
        end
    end
    mem[pattern]=n
    return n
end

for line in io.lines("data/input19.txt") do
    if i==0 then
        for x in string.gmatch(line,"%a+") do table.insert(towels,x) end
    elseif #line>0 then
        local nb=nbsolutions(line)
        part1,part2=part1+(nb>0 and 1 or 0),part2+nb
    end
    i=i+1
end
print(part1,part2)