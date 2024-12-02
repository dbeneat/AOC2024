local part1,part2=0,0
function omit(t,skip)
    local tt={}
    for i,x in ipairs(t) do if i~=skip then table.insert(tt,x) end end
    return tt
end
function ok(tab,skip)
    t=omit(tab,skip)
    for i=1,#t-1 do
        if (t[i+1]-t[i])*(t[2]-t[1])<0 then return false end
        local e=math.abs(t[i+1]-t[i]);if e>3 or e==0 then return false end
    end
    return true
end
for x in io.lines("data/input02.txt") do
    local t={}
    for d in string.gmatch(x, "[^% ]+") do
        table.insert(t,tonumber(d))
    end
    if ok(t) then part1=part1+1 end
    for skip=1,#t do
        if ok(t,skip) then part2=part2+1; break; end
    end
end
print(part1,part2)