local part1,part2=0,0

function derive(secret)
    secret=secret~(64*secret)
    secret=secret%16777216
    secret=secret~(secret//32)
    secret=secret%16777216
    secret=secret~(2048*secret)
    secret=secret%16777216
    return secret
end

function hash(a,b,c,d)
    return (((""..a)..b)..c)..d
end

local prices={}
for line in io.lines("data/input22.txt") do
    if #line==0 then break end
    local m=tonumber(line)
    local seen={}
    local k=4
    local a=m
    local b=derive(a)
    local c=derive(b)
    local d=derive(c)
    local e
    while k<=2000 do
        e=derive(d)
        local d1,d2,d3,d4=b%10-a%10,c%10-b%10,d%10-c%10,e%10-d%10
        local h=hash(d1,d2,d3,d4)
        if not seen[h] then
            prices[h]=prices[h] and prices[h]+e%10 or e%10
            part2=math.max(part2,prices[h])
            seen[h]=true
        end
        a,b,c,d=b,c,d,e
        k=k+1
    end
    part1=part1+e
end
print(part1,part2)