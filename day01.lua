local part1=0; local part2=0
local A={}; local B={}
io.input("data/input01.txt")
while io.read(0) do
    table.insert(A,io.read("*number"))
    table.insert(B,io.read("*number"))
end
table.sort(A); table.sort(B)
for i=1,#A do
    part1=part1+math.abs(A[i]-B[i])
    for j=1,#B do
        if A[i]==B[j] then part2=part2+A[i] end
    end
end
print(part1,part2)