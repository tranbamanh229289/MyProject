import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=np.array(pd.read_csv("Iris.csv"))

np.random.seed(1234)
np.random.shuffle(data)

data_train=data[:101,:]
data_test=data[101:151,:]
#Standardize test output data
X_test=np.array(data_test[:,1:5],dtype=np.float64)

#Standardize test input data
Y_test=data_test[:,5]
Y_test[np.where(Y_test=="Iris-setosa")]=0
Y_test[np.where(Y_test=="Iris-versicolor")]=1
Y_test[np.where(Y_test=="Iris-virginica")]=2
Y_test=np.array(data_test[:,5],dtype=np.float64)

#Standardize training output data
Y_train = data_train[:,5]
Y_train[np.where(Y_train=="Iris-setosa")]=0
Y_train[np.where(Y_train=="Iris-versicolor")]=1
Y_train[np.where(Y_train=="Iris-virginica")]=2
N=Y_test.shape[0]
#Standardize training input data
X_train=np.array(data_train[:,1:5],dtype=np.float64)

def KNN (X_train ,X_test,Y_train,K):
    loss=[]
    list=[]
    for i in X_test:
        cost= np.sqrt(np.sum( (X_train-i)**2,axis=1))
        loss.append(cost)
        #Take k index as the nearest neighbor of the data point
        index_sort=cost.argsort()[0:K]

        #Class of neighbors:
        y=np.array(Y_train[index_sort],dtype=np.int32)

        #Find the number of layers that appear most in K neighbors
        list.append(np.bincount(y).argmax())
        loss.append(cost)

    return list,loss

def Correct_Ratio (Y_test,list):
    cout=0
    for i in Y_test -list :
        if i!=0:
            cout=cout+1
    return (N-cout)/N*100

list,loss=KNN(X_train,X_test,Y_train,10)

print ("Classes of test data points:",Y_test)
print ("Classification results based on the KNN algorithm:",list)
print ("The accuracy ratio of the algorithm is: :",round(Correct_Ratio(Y_test,list),2),"%")
