from compimg import *
size=15000
f=open("input_3.txt")

lines=[line for line in f]
paths=[]
for line in lines:
    paths.append(line.strip().split(','))



bases=[]

for path1 in paths:
    loc=[0,0]

    base=[]
    for p in path1:
        newloc=loc.copy()
        if p[0]=='R':
            newloc[1]=loc[1]+int(p[1:])
            base+=[(loc[0],i) for i in range(loc[1],newloc[1])]
        if p[0]=='L':
            newloc[1]=loc[1]-int(p[1:])
            base+=[(loc[0],i) for i in range(loc[1],newloc[1],-1)]
        if p[0]=='U':
            newloc[0]=loc[0]+int(p[1:])
            base+=[(i,loc[1]) for i in range(loc[0],newloc[0])]
        if p[0]=='D':
            newloc[0]=loc[0]-int(p[1:])
            base+=[(i,loc[1]) for i in range(loc[0],newloc[0],-1)]
        loc=newloc.copy()
    bases.append(base)
for idx1 in range(len(bases[0])):
    el=bases[0][idx1]
    try :
        idx=bases[1].index(el)
        print(idx, bases[1][idx],abs(bases[1][idx][0])+abs(bases[1][idx][1]))
        print(idx,idx1,idx+idx1)
    except:
        pass
