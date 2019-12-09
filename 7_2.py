import numpy as np
import threading
code=[3,8,1001,8,10,8,105,1,0,0,21,42,55,76,89,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,4,9,99,3,9,102,3,9,9,101,5,9,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,1001,9,5,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

inputs=[[],[],[],[],[]]
lock=threading.Lock()
def intcode(code,instream,outstream):
    i=0
    
    output=[]
    while True:
        #print(i)
        pm3=int(code[i]/10000)
        pm2=int((code[i]-pm3*10000)/1000)
        pm1=int((code[i]-pm2*1000-pm3*10000)/100)
        op=code[i]-pm3*10000-pm2*1000-pm1*100

        if op==99:
            break
        elif op==3:
            while len(inputs[instream])==0:
                pass
            lock.acquire()
            #print(instream,inputs)
            ipt=inputs[instream].pop(0)
            lock.release()
            if pm1==0:
                code[code[i+1]]=ipt
            else:
                code[i+1]=ipt          
            i+=2

        elif op==4:
            lock.acquire()
            #inputs[outstream].append(ph[outstream])
            if pm1==0:
                inputs[outstream]+=[code[code[i+1]]]
            else:
               inputs[outstream]+=[code[i+1]]
            lock.release()
            i+=2
        
        else:
            if pm2==1:
                p2=code[i+2]
            else:
                p2=code[code[i+2]]
            if pm1==1:
                p1=code[i+1]
            else:
                p1=code[code[i+1]]

                
            if op==1:
               #print(p1,p2) 
               code[code[i+3]]=p1+p2
               
               i+=4
            elif op==2:
               code[code[i+3]]=p1*p2
               i+=4
            elif op==5:
                if p1!=0:
                    i=p2
                    #print("op5", i, pm2)
                else:
                    i+=3
            elif op==6:
                if p1==0:
                    i=p2
                else:
                    i+=3
            elif op==7:
                if p1<p2:
                     code[code[i+3]]=1
                else:
                    code[code[i+3]]=0
                i+=4
            elif op==8:
                if p1==p2:
                     code[code[i+3]]=1
                else:
                    code[code[i+3]]=0
                i+=4
            else:
                print("error")
                break
            
    

def getout(ph):
    out=0
    while True:
        for i in range(5):
            out=intcode(code,[ph[i],out])[0]
            print(out)
    return out

def simulateAmp(ph):
    amps=[]
    global inputs
    inputs=[[],[],[],[],[]]
    [inputs[i].append(ph[i]) for i in range(5)]
    inputs[0].append(0)
    print(inputs)
    for i in range(5):
        amps.append(threading.Thread(target=intcode, args=(code.copy(),i,(i+1)%5)))
        amps[i].start()
    for a in amps:
        a.join()
    #print(inputs)
    return(inputs[0][0])
#ph=[5,6,7,8,9]
#ph=[9,8,7,6,5]
#inputs=[[9,0],[8],[7],[6],[5]]
#(simulateAmp(ph))

#while True:
#    print(inputs)
phases=range(5,10)
outs=[]
for i in phases:
    for j in phases:
        for k in phases:
            for l in phases:
                for m in phases:
                    ph=[i,j,k,l,m]
                    rep=list(set(ph))
                    if len(rep)==5:
                        outs.append([simulateAmp(ph),ph])
outs=np.array(outs)
print(outs[np.argmax(outs[:,0])][0])
