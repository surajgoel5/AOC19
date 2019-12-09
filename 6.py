f=open("input_6.txt")
lines=[l for l in f]



class Node:
    def __init__(self, val):
        self.val = val
        self.dist= 1
        self.br=[]
        
orbs=[]
for l in lines:
    a,b=l.strip().split(')')
    orbs.append([a,b])

ps=[]
for o in orbs:
    ps+=o

ps=list(set(ps))
ps_nodes={}
for p in ps:
    ps_nodes[p]=Node(p)


for o in orbs:
    ps_nodes[o[0]].br.append(ps_nodes[o[1]])
    #ps_nodes[o[1]].dist=ps_nodes[o[0]].dist+1

def distset(val,n):
    for nodes in ps_nodes[val].br:
        nodes.dist=n+1
        distset(nodes.val,n+1)
distset('COM',1)

tot=0
nl=0
nbrn=0
for p in ps:
    n=ps_nodes[p]
    nbr=len(n.br)
    a=n.dist*(n.dist-1)/2
    if nbr==0:
        nl+=1
        tot+=a
        #print(n.dist,a,'+')
    if nbr>1:
        nbrn+=1
        tot-=a
        #print(a,'-')
print(tot)
