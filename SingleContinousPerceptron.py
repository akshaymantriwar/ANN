#DESIRE ON OR OPERATION #ACTIVATION FUNCTION-->BIPOLAR SIGMOID
import numpy as np
import math
from operator import add
emax=0.0001
x1=[0,0]
x2=[0,1]
x3=[1,0]
x4=[1,1]
y=[[0,0,1],[0,1,1],[1,0,1],[1,1,1]]
d=[-1,1,1,1]
w=[-1,-2,-3]
P=4
p=1
k=0
e=0
cycle=0
while(1):
    e=0
    cycle=cycle+1
    for i in range(len(y)):
        k=k+1
        net=np.dot(y[i],np.transpose(w))
        o=(1-math.exp(-1*(net)))/(1+math.exp(-1*(net)));
        if(o!=d[i]):
            e=e+0.5*(d[i]-o)**2
            x=0.5*(d[i]-o)*(1-o**2)
            w=list(map(add,np.outer(x,y[i])[0],w))
    if(e<0.0001):
        print 'Final weigth Vector:',w
        print('Number of steps:'+str(k))
        print('Number of tarining cycles:'+str(cycle))
        break
print('OUTPUT CHECKING')
o=[]
for i in range(len(y)):
    net=np.dot(y[i],np.transpose(w))
    o.append((1-math.exp(-1*(net)))/(1+math.exp(-1*(net))));
print(o)
print(d)
