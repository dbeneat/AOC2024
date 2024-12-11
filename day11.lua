local part1,part2=0,0
io.input("data/input11.txt")
local inp=io.read("*all")
function add(t,ind,count) t[ind]=t[ind] and t[ind]+count or count end
function total(t) local r=0; for _,v in pairs(t) do r=r+v end return r end
local c={}; for x in string.gmatch(inp, "[^% ]+") do add(c,tonumber(x),1) end

for k=1,75 do
    local newc={}
    for x,count in pairs(c) do
        if x==0 then add(newc,1,count)
        else
            local n=#tostring(x)
            if n%2==1 then add(newc,2024*x,count)
            else local k=math.floor(10^(n//2))
                add(newc,x//k,count)
                add(newc,x%k,count)
            end
        end
    end
    c=newc
    if k==25 then part1=total(c) elseif k==75 then part2=total(c) end
end

print(part1,part2)