function correct(res,L,Lsize,ispart2)
    if Lsize==1 then return res==L[1] end
    local last,r=tostring(L[Lsize]),tostring(res)
    return (ispart2 and string.sub(r,-#last)==last 
            and correct(tonumber("0"..string.sub(r,1,-#last-1)),L,Lsize-1,ispart2)
            )
    or (res>=L[Lsize] and correct(res-L[Lsize],L,Lsize-1,ispart2))
    or (res%L[Lsize]==0 and correct(res//L[Lsize],L,Lsize-1,ispart2))

end

local part1,part2=0,0
for line in io.lines("data/input07.txt") do
    local i=string.find(line, ":")
    local left,right = string.sub(line,1,i-1),string.sub(line,i+1)
    local res=tonumber(left)
    local L,Lsize = {},0
    for x in string.gmatch(right,"[^% ]+") do
        Lsize=Lsize+1
        table.insert(L,tonumber(x))
    end
    if correct(res,L,Lsize,false) then part1=part1+res end
    if correct(res,L,Lsize,true) then part2=part2+res end
end
print(part1,part2)