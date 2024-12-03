import re
part1,part2=0,0
mul=lambda x,y:x*y
with open("data/input03.txt") as f:
    ok=True
    for x in re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)",f.read()):
        if x=="do()": ok=True
        elif x=="don't()": ok=False
        else:
            res=eval(x); part1+=res
            if ok: part2+=res
    print(part1,part2)