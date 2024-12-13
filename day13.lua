local part1,part2=0,0
io.input("data/input13.txt")
local inp=io.read("*all")
function cost(a,b,c,d,e,f)
    local N1,N2,D=e*d-f*c,a*f-b*e,a*d-b*c
    if N1%D==0 and N2%D==0 then return 3*N1//D+N2//D end
    return 0
end
local B=math.floor(10^13)
for a,b,c,d,e,f in string.gmatch(inp,"(%d+).-(%d+).-(%d+).-(%d+).-(%d+).-(%d+)") do
    a,b,c,d,e,f=tonumber(a),tonumber(b),tonumber(c),tonumber(d),tonumber(e),tonumber(f)
    --print(a,b,c,d,e,f)
    part1=part1+cost(a,b,c,d,e,f)
    part2=part2+cost(a,b,c,d,e+B,f+B)
end
print(part1,part2)