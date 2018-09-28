##########CODE FOR THE MLP ##########################
################AKSHAYKUMAR PRAKASH MANTRIWAR###################
#################2015bcs119@sggs.ac.in###################

import numpy as np
import math
from operator import add
emax=0.0001
#input patterns with augumentation
Z=[[0.0,0.0,-1.0],[0.0,1.0,-1.0],[1.0,0.0,-1.0],[1.0,1.0,-1.0]] 

#DESIRE OUTPUTS here only one neuron in output layer
d=[[0.0],[1.0],[1.0],[0.0]]

#here two neurons in hidden layer
V=[np.random.rand(3).tolist(),
np.random.rand(3).tolist()]

#Only one neuron in output layer
W=[np.random.rand(3).tolist()]

#preserving initial weights
V1=V
W1=W
#####

c=0
st=0
E=[] #error values for drawing graph
while True:
  e=0
  c=c+1
  for i in range(len(Z)):
    st=st+1
    Z1=np.array(Z[i])
    V=np.array(V)
    hnet=V.dot(Z1.T).tolist()
    Y=[]
    Fdash=[]
    for j in range(len(V)):
        Y.append(1.0/(1+math.exp(-1.0*hnet[j])))
        Fdash.append((1.0/(1+math.exp(-1.0*hnet[j])))*(1-(1.0/(1+math.exp(-1.0*hnet[j])))))
    Y.append(-1)
    Y=np.array([Y])
    W=np.array(W)
    onet=W.dot(Y.T).tolist()[0]
    O=[]
    for k in range(len(W)):
        O.append(1.0/(1+math.exp(-1.0*onet[k])))
        e=e+0.5*(np.linalg.norm(np.array(d[i])-np.array(O))**2)
    deltao=[]
    for k in range(W.shape[0]):
        deltao.append((d[i][k]-O[k])*O[k]*(1-O[k]))
    sm=0
    deltay=[]
    for j in range(len(V)):
      sm=0
      for k in range(len(W)):
          sm=sm+W.tolist()[k][j]*deltao[k]
      deltay.append(Fdash[j]*sm)
    W=W+np.array([deltao]).dot(np.array(Y))
    V=V+np.array([deltay]).T.dot(np.array([Z1.tolist()]))
  E.append(e)
  if(e<0.0001):
    print 'INITIAL WEIGHTS FOR HIDDEN LAYER'
    print V1
    print 'INITIAL WEIGHTS FOR OUTPUT LAYER'
    print W1
    print 'FINAL WEIGHTS FOR HIDDEN LAYER'
    print V
    print 'FINAL WEIGHTS FOR OUTPUT LAYER'
    print W
    print 'FINAL ERROR: '+str(e)
    print 'TRAINING CYCLES '+str(c)
    print 'No OF STEPS '+str(st)
    break

#######################
#ERROR TRACING GRAPH
import matplotlib.pylab as pt
pt.scatter([i for i in range(len(E))],E)
pt.show()
#######################
