io.input("data/input09.txt")
inp=io.read("*all")
inp=string.gsub(inp, "\n", "")

function arith(start,nb) return (2*start+nb-1)*nb//2 end

function solve(inp,ispart2)
    inp=inp.."9"
    local res,pos=0,0
    local voids,blocks={},{}
    for i=1,#inp do
        local length=tonumber(string.sub(inp,i,i))
        if i%2==1 then --Lua 1-indexing reverses parity!
            table.insert(blocks,{pos,length})
        else
            table.insert(voids,{pos,length})
        end
        pos=pos+length
    end
    local numbl,freebl=#blocks,1
    while numbl>=1 do 
        local pos,sz=blocks[numbl][1],blocks[numbl][2]
        if sz>0 then
            local nb=1
            if ispart2 then
                nb=sz
                freebl=1
                while voids[freebl][2]<sz do freebl=freebl+1 end
            else
                while voids[freebl][2]==0 do freebl=freebl+1 end
            end 
            blocks[numbl][2]=sz-nb
            if freebl<numbl then
                res=res+arith(voids[freebl][1],nb)*(numbl-1)
                voids[freebl][1]=voids[freebl][1]+nb
                voids[freebl][2]=voids[freebl][2]-nb
            else
                res=res+arith(pos+sz-nb,nb)*(numbl-1)
            end
        else
            numbl=numbl-1
        end
    end
    return res
end

local part1,part2=solve(inp,false),solve(inp,true)
print(part1,part2)