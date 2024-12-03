from time import perf_counter
from os import system
import subprocess

N=3 #Number of days so far
totalTime = {}

print("----- Python solutions -----")
tic = perf_counter()
for i in range(1,N+1):
    a=subprocess.run(f"python day{i:02}.py",capture_output=True,encoding="UTF-8")
    print([int(x) for x in a.stdout.split()])
toc=perf_counter()
totalTime["Python"] = toc-tic


print("----- Lua solutions -----")
tic = perf_counter()
for i in range(1,N+1):
    a=subprocess.run(f"lua day{i:02}.lua",capture_output=True,encoding="UTF-8")
    print([int(x) for x in a.stdout.split()])
toc=perf_counter()
totalTime["Lua"] = toc-tic

print("----- C solutions -----")
tic = perf_counter()
for i in range(1,N+1):
    subprocess.run(f"gcc day{i:02}.c -o build/day{i:02}.exe")
toc1=perf_counter()
for i in range(1,N+1):
    a=subprocess.run(f"build/day{i:02}.exe",capture_output=True,encoding="UTF-8")
    print([int(x) for x in a.stdout.split()])
toc2=perf_counter()
totalTime["C (including compilation)"] = toc2-tic
totalTime["C (execution only)"] = toc2-toc1

print(f"\nTotal time for days 1..{N}:")
for x in totalTime:
    print(x.ljust(30,"."),round(totalTime[x],3),"s")