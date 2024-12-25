local part1=0
local keys,locks={},{}
local n=0
local r={0,0,0,0,0}
for line in io.lines("data/input25.txt") do
    if #line>0 then
        for i=1,5 do
            if string.sub(line,i,i)=="#" then
                r[i]=r[i]+1
            end
        end
        n=n+1
    end
    if n==7 then
        n=0
        if string.sub(line,1,1)=="#" then
            table.insert(locks,r)
        else
            table.insert(keys,r)
        end
        r={0,0,0,0,0}
    end
end
for _,kc in ipairs(keys) do
    for _,lc in pairs(locks) do
        for i=1,5 do
            if kc[i]+lc[i]>7 then goto skip end
        end
        part1=part1+1
        ::skip::
    end
end
print(part1)