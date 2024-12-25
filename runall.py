from os.path import exists
from time import perf_counter
import subprocess


N=25
chrono={}
totPy,totLua,totC=0,0,0

print("----- Python solutions -----")

for i in range(1,N+1):
    fname=f"day{i:02}.py"
    if exists(fname) and i!=24:
        tic = perf_counter()
        a=subprocess.run(f"python {fname}",capture_output=True,encoding="UTF-8")   
        toc=perf_counter()
        chrono[("py",i)]=round(toc-tic,3)
        totPy+=toc-tic
        print(a.stdout)
    else:
        chrono[("py",i)]="Missing"

print("----- Lua solutions -----")

for i in range(1,N+1):
    fname=f"day{i:02}.lua"
    if exists(fname):
        tic = perf_counter()
        a=subprocess.run(f"lua {fname}",capture_output=True,encoding="UTF-8")
        toc=perf_counter()
        chrono[("lua",i)]=round(toc-tic,3)
        totLua+=toc-tic
        print(a.stdout)
    else:
        chrono[("lua",i)]="Missing"

print("----- C solutions -----")

for i in range(1,N+1):
    fname=f"day{i:02}.c"
    if exists(fname):
        subprocess.run(f"gcc {fname} -o build/day{i:02}.exe")
for i in range(1,N+1):
    fname=f"build/day{i:02}.exe"
    if exists(fname):
        tic = perf_counter()
        a=subprocess.run(f"{fname}",capture_output=True,encoding="UTF-8")
        toc=perf_counter()
        chrono[("c",i)]=round(toc-tic,3)
        totC+=toc-tic
        print(a.stdout)
    else:
        chrono[("c",i)]="Missing"




print("Execution times (in sec)")
print()
headers="       |  Python  |  Lua     |  C       "

print(headers)
sz=[len(x) for x in headers.split("|")]
print("+".join(["-"*s for s in sz]))
for i in range(1,N+1):
    row=f"Day {i}".ljust(sz[0]," ")
    row+="|"+f" {chrono[('py',i)]}".ljust(sz[1]," ")
    row+="|"+f" {chrono[('lua',i)]}".ljust(sz[2]," ")
    row+="|"+f" {chrono[('c',i)]}".ljust(sz[3]," ")
    print(row)
print("+".join(["-"*s for s in sz]))
row="Total".ljust(sz[0]," ")
row+="|"+f" {round(totPy,3)}".ljust(sz[1]," ")
row+="|"+f" {round(totLua,3)}".ljust(sz[2]," ")
row+="|"+f" {round(totC,3)}".ljust(sz[3]," ")
print(row)