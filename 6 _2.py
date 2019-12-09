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

def distset(val,n):
    for nodes in ps_nodes[val].br:
        nodes.dist=n+1
        distset(nodes.val,n+1)
distset('COM',1)


def getmap(node):
    retmap=[]
    while node.val!='COM':
        for p in ps:
            thisnode=ps_nodes[p]
            if node in thisnode.br:
                 node=thisnode
                 retmap.append(node.val)
    return(retmap)


youmap=getmap(ps_nodes['YOU'])
sanmap=getmap(ps_nodes['SAN'])

count=0
for a in youmap:
    if a in sanmap:
       count+=1 

print(ps_nodes['YOU'].dist+ps_nodes['SAN'].dist-2*count -2)
