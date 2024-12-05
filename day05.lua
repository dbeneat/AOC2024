local part1,part2=0,0
order={}
for i=1,100 do
    order[i]={}
    for j=1,100 do
        order[i][j]=0
    end
end
function cmp(a,b) return order[a][b] end
function bsort(t)
    local ok=false
    local wassorted=true
    while not ok do
        ok=true
        for i=1,#t-1 do
            local a,b=t[i],t[i+1]
            if order[b][a]==1 then t[i],t[i+1]=b,a; ok=false; wassorted=false; end
        end
    end
    return wassorted
end

for x in io.lines("data/input05.txt") do
    if #x==5 then
        local a=tonumber(string.sub(x,1,2))
        local b=tonumber(string.sub(x,4,5))
        order[a][b]=1
    elseif #x>0 then
        load("t={"..x.."}")()
        wassorted=bsort(t)
        if wassorted then part1=part1+t[(#t)//2+1]
        else part2=part2+t[#t//2+1] end
    end
end
print(part1,part2)