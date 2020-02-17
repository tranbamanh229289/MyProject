import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix , solvers

n_samples = 100
C=100
np.random.seed(1234)
means=np.array([[4,4],[6,6]])
covs =np.array([[1,0],[0,1]])
x1= np.random.multivariate_normal(means[0],covs,n_samples) #label -1
x2=np.random.multivariate_normal(means[1],covs,n_samples) #label 1
X=np.concatenate((x1,x2),axis=0) #data
Y=np.concatenate((np.ones((1,n_samples)),-1*np.ones((1,n_samples))) ,axis=1)

V=X*Y.T
P=matrix(np.dot(V,V.T))
q=matrix(-np.ones((n_samples*2,1)))
G=matrix (np.vstack((-np.eye(2*n_samples),np.eye(2*n_samples))))
h=matrix(np.vstack ((np.zeros((2*n_samples,1)),C*np.ones((2*n_samples,1)))))
A=matrix(Y)
b=matrix (np.zeros((1,1)))
solvers.options['show_progress']=False
sol = solvers.qp(P,q,G,h,A,b)
l=np.array(sol['x'])
S=np.where(l>10**-5 )[0]
T=np.where(l<99)[0]
M=np.intersect1d(S,T)

lS=l[S]
YM=Y[:,M]
XM=X[M,:]
VS=V[S,:]
w=np.dot(lS.T,VS)
b=np.mean(YM.T-np.dot(XM,w.T))

plt.subplot(1,2,1)
plt.title("Before classification")
plt.plot(x1[:,0],x1[:,1],'ro')
plt.plot(x2[:,0],x2[:,1],'go')
plt.xlabel("X1")
plt.ylabel("X2")

plt.subplot(1,2,2)
plt.title("After classification")
x1_test=np.arange(1,10,0.5)
x2_test=(-b-w.T[0]*x1_test)/(w.T[1])
plt.plot(x1_test[:],x2_test[:])
plt.plot(x1[:,0],x1[:,1],'ro')
plt.plot(x2[:,0],x2[:,1],'go')
plt.xlabel("X1")
plt.ylabel("X2")

plt.suptitle("My sb")
plt.show()
print (np.dot(X,w.T)+b) # Values >0 : label 1 ; Values <0 : label -1








