import numpy as np
passes=np.arange(156218,652528)
#passes=[121111]
possible=[]
for passy in passes:
    digs=[]
    pa=passy
    for i in range(5,-1,-1):
        p=int(pa/(10**i))
        pa=pa-p*(10**i)
        digs.append(p)
    flag=0
    consec=[]
    for i in range(5):
        if digs[i]==digs[i+1]:
            consec.append(digs[i])
    if len(consec)==0 :
        flag =0
    elif len(consec)==1:
        flag =1
    else:
        cs=[]
        for i in consec:
          cs.append(consec.count(i))
        if 1 in cs:
            flag=1
    if flag:
        if sorted(digs)==digs:
            possible.append(passy)
print(len(possible))        
