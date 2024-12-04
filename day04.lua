local part1,part2=0,0
L={}
for x in io.lines("data/input04.txt") do
    if #x>0 then 
        local row={}
        for i=1,#x do table.insert(row,string.sub(x,i,i)) end
        table.insert(L,row)
    end
end
function get(i,j) return L[i] and L[i][j] or '' end
function A(a,b,c,d,e,f,g,h) return get(a,b)..get(c,d)..get(e,f)..get(g,h) end
function B(a,b,c,d,e,f) return get(a,b)..get(c,d)..get(e,f) end
for i = 1,#L do
    for j = 1,#L[1] do
        local w,w1,w2
        w=A(i,j,i,j+1,i,j+2,i,j+3); if w=="XMAS" or w=="SAMX" then part1=part1+1 end
        w=A(i,j,i+1,j,i+2,j,i+3,j); if w=="XMAS" or w=="SAMX" then part1=part1+1 end
        w=A(i,j,i+1,j+1,i+2,j+2,i+3,j+3); if w=="XMAS" or w=="SAMX" then part1=part1+1 end
        w=A(i,j+3,i+1,j+2,i+2,j+1,i+3,j); if w=="XMAS" or w=="SAMX" then part1=part1+1 end
        w1,w2=B(i,j,i+1,j+1,i+2,j+2),B(i,j+2,i+1,j+1,i+2,j)
        if(w1=="MAS" or w1=="SAM") and (w2=="MAS" or w2=="SAM") then part2=part2+1 end
    end
end
print(part1,part2)