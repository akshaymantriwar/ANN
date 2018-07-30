#ACTIVATION FUNCTION-->BIPOLAR THRESHOLD
import numpy as np
import math
from operator import add
emax=0.0001
y=[[4,4,1],[4,3,1],[4,-3,1],[4,-4,1],[-4,-4,1],[-4,-3,1]]
d=[[1,-1,-1],[1,-1,-1],[-1,1,-1],[-1,1,-1],[-1,-1,1],[-1,-1,1]]
w=[[-1,-1,-1],[-2,-2,-2],[-3,-3,-3]]
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
        for j in range(len(w)):
            net=np.dot(y[i],np.transpose(w[j]))
            if(net>0):
                o=1
            elif(net<0):
                o=-1
            else:
                o=-1*(d[i][j])
            
            e=e+0.5*((d[i][j]-o)**2)
            x=0.5*(d[i][j]-o)
            w[j]=list(map(add,np.outer(x,y[i])[0],w[j]))
     #print(w)
        
    
    if(e==0):
        print 'Final weigth Vector:',w
        print('Number of steps:'+str(k))
        print('Number of tarining cycles:'+str(cycle))
        break 
        
