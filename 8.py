import numpy as np
import matplotlib.pyplot as plt
f=open("input_8.txt")
lines=[l for l in f]
data=[int(a) for a in lines[0].strip()]

data=(np.array(data))
h=6
w=25
layers=data.reshape(( int(len(data)/(h*w)),h*w ))

counts=np.array([[l.tolist().count(0),l.tolist().count(1),l.tolist().count(2)] for l in layers])

print(counts[counts[:,0].argmin()])
img=[]
for i in range(h*w):
    li=layers[:,i].tolist()
    if 1 not in li:
        a=0
    elif 0 not in li:
        a=1
    elif li.index(0)<li.index(1):
        a=0
    else:
        a=1
    img.append(a)
img=np.array(img)
plt.imshow(img.reshape((h,w)))
plt.show()
