f=open("input_1.txt")

lines=[line for line in f]
finalmass=0

for l in lines:
    n=int(l.strip())
    mass=int(n/3)-2
    totm=0
    newm=mass
    while newm>0:
        totm+=newm
        newm=int(newm/3)-2
    finalmass+=totm
    
print(finalmass)


