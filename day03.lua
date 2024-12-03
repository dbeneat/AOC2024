local part1,part2=0,0
io.input("data/input03.txt")
inp=io.read("*all")
local ok=true
for i=1,#inp do
    if string.sub(inp,i,i+3)=="do()" then ok=true
    elseif string.sub(inp,i,i+6)=="don't()" then ok=false
    else _,_,a,b=string.find(inp,"^mul%((%d+),(%d+)%)",i)
        if a and b then
            local r=tonumber(a)*tonumber(b)
            part1=part1+r; if ok then part2=part2+r end
        end
    end   
end
print(part1,part2)