import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix, solvers

np.random.seed(1234)
means1 = [2,2]
means2=[5,5]
cov1 = [[0.5,0],[0,0.5]]
cov2 =[[0.5,0],[0,0.5]]
n_samples=200
x1=np.random.multivariate_normal(means1,cov1,n_samples) #label: 1
x2=np.random.multivariate_normal(means2,cov2,n_samples) #label:-1
X=np.concatenate((x1,x2),axis=0) #data
Y=np.concatenate((np.ones((1,n_samples)),-1*np.ones((1,n_samples))) ,axis=1) #label

V=X*Y.T
P=matrix(np.dot(V,V.T))
q=matrix(-1*np.ones((2*n_samples,1)))
G=matrix(-1*np.eye(2*n_samples))
h=matrix (np.zeros((2*n_samples,1)))
A=matrix(Y)
b=matrix(np.zeros((1,1)))
solvers.options['show_progress']=False
sol = solvers.qp(P,q,G,h,A,b)
l=np.array(sol['x'])

id=(np.where(l>10**-6))[0]
lamda=l[id]
Y_id=Y[:,id]
X_id=X[id,:]
V_id=V[id,:]
w=np.dot(lamda.T,V_id)
b=np.mean(Y_id-np.dot(w,X_id.T))
x1_test=np.arange(1,10,0.5)
x2_test=(-b-w.T[0]*x1_test)/(w.T[1])

plt.plot(x1_test[:],x2_test[:])
plt.plot(x1[:,0],x1[:,1],"ro")
plt.plot (x2[:,0],x2[:,1],'go')
plt.show()
